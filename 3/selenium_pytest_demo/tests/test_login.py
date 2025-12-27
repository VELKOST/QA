
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_login_success(driver, wait, base_url, creds):
    driver.get(f"{base_url}/login")

    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "username").send_keys(creds["username"])
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(creds["password"])
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    # URL contains /secure
    wait.until(lambda d: "/secure" in d.current_url)

    # Flash message and Logout link
    flash = wait.until(lambda d: d.find_element(By.ID, "flash"))
    assert "You logged into a secure area!" in flash.text

    logout = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/logout']")))
    assert logout.is_displayed()
