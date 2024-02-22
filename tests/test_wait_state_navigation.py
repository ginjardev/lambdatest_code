from playwright.sync_api import expect
from fixtures.wait_fixture import page, browser

# page = fixtures.wait_fixture.page
def test_wait_state_navigation(page):
	page.goto("https://ecommerce-playground.lambdatest.io/")
    # wait for load state wait until naviagtion is complete
	page.wait_for_load_state()
	expect(page).to_have_title("Your Store")
