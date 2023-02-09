from fastapi import FastAPI, Query
from enum import Enum
from datetime import datetime
import time
import pytz
import os
import requests

os.environ["TZ"] = "Etc/UTC"

api_key = "27b3e2642590d540b19560a7d69ccc45"


class Measures(str, Enum):
    POA = "POA"
    TEMP = "TEMP"


app = FastAPI()


@app.get("/data")
async def read_item(
    item_name: Measures = Query(
        default="POA",
        title="Name of the Measure:",
        description="Select the measure to read data between available values",
    ),
    start_date: datetime = Query(
        default="2023-01-01T00:00:00-03:00", title="Start Date"
    ),
    end_date: datetime = Query(default="2023-01-02T00:00:00-03:00", title="End Date"),
    latitude: float = Query(default=-15.795904, title="Latitude"),
    longitude: float = Query(default=-47.875925, title="Longitude"),
):
    item = {
        "item_id": item_name,
        "start_date": start_date.astimezone(pytz.UTC),
        "end_date": end_date.astimezone(pytz.UTC),
        "start_unix_timestamp": int(
            time.mktime(start_date.astimezone(pytz.UTC).timetuple())
        ),
        "end_unix_timestamp": int(
            time.mktime(end_date.astimezone(pytz.UTC).timetuple())
        ),
        "latitude": latitude,
        "longitude": longitude,
    }
    params = {
        "lat": item["latitude"],
        "lon": item["longitude"],
        "start": item["start_unix_timestamp"],
        "end": item["end_unix_timestamp"],
        "appid": api_key,
    }

    res = requests.get(
        "http://api.openweathermap.org/data/2.5/solar_radiation/history", params=params
    )

    return item, res.text
