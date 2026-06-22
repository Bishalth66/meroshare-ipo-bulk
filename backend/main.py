import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, TimeoutError 

load_dotenv()

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto(os.getenv("BASE_URL"))
        try:
           page.wait_for_selector(".select2-selection", timeout=5000)
           page.click(".select2-selection")
           page.wait_for_selector(".select2-search__field", timeout=5000)
           page.fill(".select2-search__field", str(os.getenv("DP")))
           page.keyboard.press("Enter")
           page.fill("#username", os.getenv("USER"))
           page.fill("#password", os.getenv("PASSWORD"))
           page.click('button[type="submit"]')
        except TimeoutError:
            pass        
    

if __name__ == "__main__":
    main()
