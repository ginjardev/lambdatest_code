from playwright.sync_api import expect
from fixtures.wait_fixture import page, browser, set_test_status

def test_wait_event_navigation(page, set_test_status):
    page.goto("https://ecommerce-playground.lambdatest.io/")
    page.get_by_role("button", name="Shop by Category").click()
    page.get_by_role("link", name="Cameras", exact=True).click()
    # waits for event load to be completed
    page.wait_for_event("domcontentloaded")
    title = page.title()
    if "Cameras" in title:
        set_test_status(status="passed", remark="Title matched")
    else:
        set_test_status(status="failed", remark="Title did not match")
    expect(page).to_have_title("Cameras")
