from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://bookings.better.org.uk/")
        page.wait_for_timeout(5000)

        print("Site loaded successfully")

        browser.close()

run()
