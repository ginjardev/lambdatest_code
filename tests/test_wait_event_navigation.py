from playwright.sync_api import expect
from fixtures.wait_fixture import page, browser

def test_wait_event_navigation(page):
	page.goto("https://ecommerce-playground.lambdatest.io/")
	page.get_by_role("button", name="Shop by Category").click()
	page.get_by_role("link", name="Cameras", exact=True).click()
	# waits for event load to be completed
	page.wait_for_event("domcontentloaded")
	expect(page).to_have_title("Cameras")
