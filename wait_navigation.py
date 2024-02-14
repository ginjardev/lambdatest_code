import json
import os
import urllib
import subprocess
import re
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


def wait_state_navigation(playwright):
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

    try:
        page.goto("https://ecommerce-playground.lambdatest.io/")

        # wait for load state wait until naviagtion is complete
        page.wait_for_load_state()
        title = page.title()
        expect(page).to_have_title("Your Store")

        print("Title:: ", title)

        if "Your Store" in title:
            set_test_status(page, "passed", "Title matched")
        else:
            set_test_status(page, "failed", "Title did not match")
    except Exception as err:
        print("Error:: ", err)
        set_test_status(page, "failed", str(err))
    browser.close()


def wait_url_navigation(playwright):
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

    try:
        page.goto("https://ecommerce-playground.lambdatest.io/")
        page.get_by_role("link", name="Blog", exact=True).click()

        # waits for navigated url to match url argument
        page.wait_for_url("**/blog/home")
        expect(page).to_have_url(re.compile(".*/blog/home$"))
        page.locator("#mz-article-tab-76210960-0").get_by_label("1 / 10").get_by_text(
            "amet volutpat consequat mauris nunc congue nisi vitae suscipit tellus"
        ).click()
        heading = page.get_by_role(
            "heading",
            name="amet volutpat consequat mauris nunc congue nisi vitae suscipit tellus",
        ).inner_text()
        print("Heading::", heading)
        if "amet volutpat" in heading:
            set_test_status(page, "passed", "Heading matched")
        else:
            set_test_status(page, "failed", "Heading did not match")
    except Exception as err:
        print("Error:: ", err)
        set_test_status(page, "failed", str(err))
    browser.close()


def wait_event_navigation(playwright):
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

    try:
        page.goto("https://ecommerce-playground.lambdatest.io/")
        page.get_by_role("button", name="Shop by Category").click()
        page.get_by_role("link", name="Cameras", exact=True).click()

        # waits for event load to be completed
        page.wait_for_event("domcontentloaded")
        expect(page).to_have_title("Cameras")
        title = page.title()

        print("Title:: ", title)

        if "Cameras" in title:
            set_test_status(page, "passed", "Title matched")
        else:
            set_test_status(page, "failed", "Title did not match")
    except Exception as err:
        print("Error:: ", err)
        set_test_status(page, "failed", str(err))
    browser.close()


def wait_function_navigation(playwright):
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

    try:
        page.goto("https://ecommerce-playground.lambdatest.io/")
        page.get_by_role("link", name="Jolio Balia", exact=True).nth(1).click()
        page.evaluate("() => document.title")

        # waits for function to return truthy value
        page.wait_for_function("title = 'Jolio Balia'; () => document.title === title")
        expect(page).to_have_title("Jolio Balia")
        title = page.title()

        print("Title:: ", title)

        if "Jolio" in title:
            set_test_status(page, "passed", "Title matched")
        else:
            set_test_status(page, "failed", "Title did not match")
    except Exception as err:
        print("Error:: ", err)
        set_test_status(page, "failed", str(err))
    browser.close()


def set_test_status(page, status, remark):
    page.evaluate(
        "_ => {}",
        'lambdatest_action: {"action": "setTestStatus", "arguments": {"status":"'
        + status
        + '", "remark": "'
        + remark
        + '"}}',
    )


with sync_playwright() as playwright:
    wait_state_navigation(playwright)
    wait_url_navigation(playwright)
    wait_event_navigation(playwright)
    wait_function_navigation(playwright)
