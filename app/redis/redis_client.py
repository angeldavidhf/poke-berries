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
    Check for berry data in Redis.
    """
    berry_stats = redis_client.get(berry_stats_key)
    if berry_stats is not None:
        return berry_stats.decode("utf-8")
    else:
        return None


def set_berry_stats(data):
    """
    Setting stats for berry data in Redis.
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
    Save for berry data in Redis.
    """
    try:
        data_json = json.dumps(data)
        redis_client.set(berry_stats_key, data_json)

    except Exception as e:
        raise HTTPException(status_code=500, detail="Error saving data in Redis")
