from playwright.sync_api import expect
from fixtures.wait_fixture import page, browser, set_test_status
import re


def test_wait_url_navigation(page, set_test_status):
    page.goto("https://ecommerce-playground.lambdatest.io/")
    page.get_by_role("link", name="Blog", exact=True).click()
    # waits for navigated url to match url argument
    page.wait_for_url("**/blog/home")
    title = page.title()
    if "Blog - Poco theme" in title:
        set_test_status(status="passed", remark="Title matched")
    else:
        set_test_status(status="failed", remark="Title did not match")
    expect(page).to_have_url(re.compile(".*/blog/home$"))
