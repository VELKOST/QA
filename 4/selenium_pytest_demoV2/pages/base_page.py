from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait

    def open(self, url: str):
        self.driver.get(url)
        return self

    # --- find/click/type ---
    def find(self, locator):
        return self.driver.find_element(*locator)

    def finds(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        return self

    def type(self, locator, text: str, clear=True, submit=False):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        if clear:
            el.clear()
        el.send_keys(text)
        if submit:
            el.submit()
        return el

    # --- waits & utils ---
    def wait_visible(self, locator, timeout=None):
        w = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        return w.until(EC.visibility_of_element_located(locator))

    def wait_present(self, locator, timeout=None):
        w = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        return w.until(EC.presence_of_element_located(locator))

    def url_contains(self, text: str):
        return self.wait.until(EC.url_contains(text))

    def js(self, script: str, *args):
        return self.driver.execute_script(script, *args)
