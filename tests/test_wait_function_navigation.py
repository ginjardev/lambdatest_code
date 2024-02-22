from playwright.sync_api import expect
from fixtures.wait_fixture import page, browser

def test_wait_function_navigation(page):
	page.goto("https://ecommerce-playground.lambdatest.io/")
	page.get_by_role("link", name="Jolio Balia", exact=True).nth(1).click()
	page.evaluate("() => document.title")
	# waits for function to return truthy value
	page.wait_for_function("title = 'Jolio Balia'; () => document.title === title")
	expect(page).to_have_title("Jolio Balia")