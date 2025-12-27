
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="chrome or firefox")
    parser.addoption("--headless", action="store_true", help="Run in headless mode")

@pytest.fixture
def base_url():
    return "https://the-internet.herokuapp.com"

@pytest.fixture
def creds():
    return {
        "username": os.getenv("DEMO_USERNAME", "tomsmith"),
        "password": os.getenv("DEMO_PASSWORD", "SuperSecretPassword!"),
    }

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser").lower()
    headless = request.config.getoption("--headless")

    if browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        drv = webdriver.Firefox(service=service, options=options)
    else:
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1280,900")
        service = ChromeService(executable_path=ChromeDriverManager().install())
        drv = webdriver.Chrome(service=service, options=options)

    drv.implicitly_wait(2)
    yield drv
    drv.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)
