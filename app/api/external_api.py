import os

import requests
from fastapi import HTTPException


def call_external_api():
    base_url = os.getenv("POKEAPI_BASE_URL")
    berries_endpoint = os.getenv("POKEAPI_BERRIES_ENDPOINT")

    url = f"{base_url}{berries_endpoint}"
    berries_data = []

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if "count" in data:
            total_berries = data["count"]

            for berry_id in range(1, total_berries + 1):
                berry_url = f"{url}/{berry_id}/"
                try:
                    berry_response = requests.get(berry_url)
                    berry_response.raise_for_status()
                    berry_data = berry_response.json()

                    extracted_data = {
                        "growth_time": berry_data["growth_time"],
                        "id": berry_data["id"],
                        "name": berry_data["name"],
                        "max_harvest": berry_data["max_harvest"],
                        "size": berry_data["size"],
                        "smoothness": berry_data["smoothness"],
                        "soil_dryness": berry_data["soil_dryness"],
                        "natural_gift_power": berry_data["natural_gift_power"]
                    }

                    berries_data.append(extracted_data)
                except requests.exceptions.RequestException as e:
                    raise HTTPException(status_code=500, detail=f"Error when obtaining the berry {berry_id}: {e}")
        else:
            print("The total amount of berries could not be obtained.")
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error calling external API: {e}")

    return berries_data
