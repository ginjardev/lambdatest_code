from playwright.sync_api import expect
from fixtures.wait_fixture import page, browser
import re


def test_wait_url_navigation(page):
	page.goto("https://ecommerce-playground.lambdatest.io/")
	page.get_by_role("link", name="Blog", exact=True).click()
    # waits for navigated url to match url argument
	page.wait_for_url("**/blog/home")
	expect(page).to_have_url(re.compile(".*/blog/home$"))
