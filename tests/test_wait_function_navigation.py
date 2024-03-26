from playwright.sync_api import expect
from fixtures.wait_fixture import page, browser, set_test_status

def test_wait_function_navigation(page, set_test_status):
	page.goto("https://ecommerce-playground.lambdatest.io/")
	page.get_by_role("link", name="Jolio Balia", exact=True).nth(1).click()
	page.evaluate("() => document.title")
	# waits for function to return truthy value
	page.wait_for_function("title = 'Jolio Balia'; () => document.title === title")
	title = page.title()
	if "Jolio Balia" in title:
		set_test_status(status="passed", remark="Title matched")
	else:
		set_test_status(status="failed", remark="Title did not match")
	expect(page).to_have_title("Jolio Balia")
	