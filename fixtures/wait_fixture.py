import json
import os
import urllib
import subprocess
import re
import pytest
from dotenv import load_dotenv

load_dotenv(".env", override=True)

from playwright.sync_api import sync_playwright, expect, Playwright

capabilities = {
    "browserName": "Chrome",  # Browsers allowed: `Chrome`, `MicrosoftEdge`, `pw-chromium`, `pw-firefox` and `pw-webkit`
    "browserVersion": "latest",
    "LT:Options": {
        "platform": "Windows 10",
        "build": "Waits in Playwright Python Build",
        "name": "Playwright Wait Navigation Python",
        "user": os.getenv("LT_USERNAME"),
        "accessKey": os.getenv("LT_ACCESS_KEY"),
        "network": True,
        "video": True,
        "console": True,
        "tunnel": False,  # Add tunnel configuration if testing locally hosted webpage
        "tunnelName": "",  # Optional
        "geoLocation": "",  # country code can be fetched from https://www.lambdatest.com/capabilities-generator/
    },
}

@pytest.fixture
def browser_operation(playwright):
    playwrightVersion = (
        str(subprocess.getoutput("playwright --version")).strip().split(" ")[1]
    )
    capabilities["LT:Options"]["playwrightClientVersion"] = playwrightVersion
    lt_cdp_url = (
        "wss://cdp.lambdatest.com/playwright?capabilities="
        + urllib.parse.quote(json.dumps(capabilities))
    )
    browser = playwright.chromium.connect(lt_cdp_url, timeout=30000)
    page = browser.new_page()
    yield page
    browser.close()
