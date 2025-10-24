from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional

import requests

from dataclasses import dataclass
from typing import List, Optional
geo_data = requests.get("http://ip-api.com/json/").json()

latitude = geo_data["lat"]
longitude = geo_data["lon"]
timezone_id = geo_data["timezone"]
language_code = geo_data["countryCode"].lower()  # e.g., 'us' -> 'en-US'
def is_stream_online(username):
    """
    Returns True if the Twitch stream is online, False otherwise.
    Uses the public frontend Client-ID (no OAuth).
    """
    url = f"https://www.twitch.tv/{username}"
    headers = {
        "Client-ID": "kimne78kx3ncx6brgo4mv6wki5h1ko",  # Publicly known Client-ID
    }
    resp = requests.get(url, headers=headers)
    return "isLiveBroadcast" in resp.text

with SB(uc=True, test=True,locale=f"{language_code.upper()}") as isjy09y2tg4:
    isjy09y2tg4.execute_cdp_cmd(
        "Emulation.setGeolocationOverride",
        {
            "latitude": latitude,
            "longitude": longitude,
            "accuracy": 100
        }
    )
    isjy09y2tg4.execute_cdp_cmd(
        "Emulation.setTimezoneOverride",
        {"timezoneId": timezone_id}
    )
    url = "https://www.twitch.tv/brutalles"
    isjy09y2tg4.uc_open_with_reconnect(url, 4)
    isjy09y2tg4.sleep(40)
    if is_stream_online("brutalles"):
        url = "https://www.twitch.tv/brutalles"
        isjy09y2tg4.uc_open_with_reconnect(url, 5)
        if isjy09y2tg4.is_element_present('button:contains("Accept")'):
            isjy09y2tg4.uc_click('button:contains("Accept")', reconnect_time=4)
        if True:
            isjy09y2tg = isjy09y2tg4.get_new_driver(undetectable=True)
            isjy09y2tg.uc_open_with_reconnect(url, 5)
            isjy09y2tg4.sleep(10)
            if isjy09y2tg.is_element_present('button:contains("Accept")'):
                isjy09y2tg.uc_click('button:contains("Accept")', reconnect_time=4)
            while is_stream_online("brutalles"):
                isjy09y2tg4.sleep(10)
            isjy09y2tg4.quit_extra_driver()
    isjy09y2tg4.sleep(1)
