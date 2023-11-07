import json
import os
import statistics

import redis
from fastapi import HTTPException
from collections import defaultdict

redis_host = os.getenv("REDIS_HOST")
redis_port = os.getenv("REDIS_PORT")

redis_client = redis.Redis(host=redis_host, port=redis_port)
berry_stats_key = "berry_stats"


def check_berry_stats():
    """
    Checks for berry data in Redis.

    Checks if the statistics of berry data are available in the Redis cache. If the data exists,
    it is retrieved and returned as a dictionary. If the data is not found, None is returned.

    Returns:
        dict or None: A dictionary containing berry statistics or None if the data is not in Redis.
    """
    berry_stats = redis_client.get(berry_stats_key)
    if berry_stats is not None:
        return json.loads(berry_stats)
    else:
        return None


def set_berry_stats(data):
    """
    Sets berry statistics in Redis.

    Calculates and processes statistics for berry data and stores the results in Redis.
    The function computes statistics like minimum growth time, median growth time, maximum growth time,
    variance, mean, and frequency of growth times.

    Args:
        data (list): A list of berry data dictionaries.

    Returns:
        dict: A dictionary containing computed berry statistics.
    """
    growth_times = []
    frequency_growth_time = defaultdict(int)

    for berry in data:
        growth_time = berry["growth_time"]
        growth_times.append(growth_time)
        frequency_growth_time[growth_time] += 1

    if not growth_times:
        return {
            "berries_names": [],
            "min_growth_time": "",
            "median_growth_time": "",
            "max_growth_time": "",
            "variance_growth_time": "",
            "mean_growth_time": "",
            "frequency_growth_time": {}
        }

    return {
        "berries_names": [berry["name"] for berry in data],
        "min_growth_time": min(growth_times),
        "median_growth_time": statistics.median(growth_times),
        "max_growth_time": max(growth_times),
        "variance_growth_time": statistics.variance(growth_times),
        "mean_growth_time": statistics.mean(growth_times),
        "frequency_growth_time": dict(frequency_growth_time)
    }


def save_berry_stats(data):
    """
    Saves berry statistics in Redis.

    Converts the berry statistics data to a JSON format and stores it in Redis. In case of any errors
    during the storage process, an HTTPException with a status code of 500 is raised.

    Args:
        data (dict): A dictionary containing berry statistics.

    Raises:
        HTTPException: Raised in case of an error while saving data in Redis.
    """
    try:
        data_json = json.dumps(data)
        redis_client.set(berry_stats_key, data_json)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error saving data in Redis")
