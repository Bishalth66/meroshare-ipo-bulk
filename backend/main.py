from playwright.sync_api import sync_playwright


BASE_URL = "https://meroshare.cdsc.com.np/#/login" 

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto(BASE_URL)
        print(page.title())
        browser.close()         


if __name__ == "__main__":
    main()
