from playwright.sync_api import expect
from fixtures.wait_fixture import page, browser, set_test_status


# page = fixtures.wait_fixture.page
def test_wait_state_navigation(page, set_test_status):
    page.goto("https://ecommerce-playground.lambdatest.io/")
    # wait for load state wait until naviagtion is complete
    page.wait_for_load_state() # load by default
    title = page.title()
    if "Your Store" in title:
        set_test_status(status="passed", remark="Title matched")
    else:
        set_test_status(status="failed", remark="Title did not match")
    expect(page).to_have_title("Your Store")
