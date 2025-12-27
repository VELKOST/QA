
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions

def main():
    options = ChromeOptions()
    options.add_argument("--window-size=1280,900")
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    try:
        driver.get("https://example.com/")
        print("Title:", driver.title)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
