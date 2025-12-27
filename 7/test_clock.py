# test_clock.py
# Автотест Appium: открывает Google Clock и жмет FAB "Добавить будильник".

from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

APP_PACKAGE = "com.google.android.deskclock"
APP_ACTIVITY = "com.android.deskclock.DeskClock"  # полное имя активити

def make_driver():
    opts = UiAutomator2Options()
    # Базовые капы
    opts.platform_name = "Android"
    opts.automation_name = "UiAutomator2"
    opts.device_name = "Android Emulator"  # имя из `adb devices` тоже OK
    opts.new_command_timeout = 180
    opts.no_reset = True
    opts.auto_grant_permissions = True
    # Пакет/активити приложения
    opts.set_capability("appPackage", APP_PACKAGE)
    opts.set_capability("appActivity", APP_ACTIVITY)
    return webdriver.Remote("http://127.0.0.1:4723", options=opts)

def wait_activity(driver, activity, timeout=20):
    try:
        WebDriverWait(driver, timeout).until(
            lambda d: d.current_activity.endswith(activity.split(".")[-1])
        )
    except TimeoutException:
        pass

def goto_alarm_tab(driver):
    for acc in ("Alarm", "Будильник"):
        try:
            el = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, acc))
            )
            el.click()
            sleep(1)
            return
        except Exception:
            continue
    try:
        el = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, "//*[contains(@text,'Будильник') or contains(@text,'Alarm')]")
            )
        )
        el.click()
        sleep(1)
    except Exception:
        pass

def tap_fab_add_alarm(driver):
    try_ids = [
        f"{APP_PACKAGE}:id/fab",
        "com.android.deskclock:id/fab",
    ]
    for rid in try_ids:
        try:
            el = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((AppiumBy.ID, rid))
            )
            el.click()
            return True
        except Exception:
            continue
    xpaths = [
        "//*[@content-desc[contains(.,'Add alarm')]]",
        "//*[@content-desc[contains(.,'Добавить будильник')]]",
        "//*[contains(@text,'Добавить') or contains(@text,'Add')]",
        "//*[@resource-id[contains(.,'fab')]]",
    ]
    for xp in xpaths:
        try:
            el = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, xp))
            )
            el.click()
            return True
        except Exception:
            continue
    return False

def close_optional_dialogs(driver):
    for t in ("Отмена", "Cancel", "Не сейчас", "No thanks"):
        try:
            el = driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().textContains("{t}")'
            )
            el.click()
            sleep(0.5)
            return
        except Exception:
            continue

def main():
    driver = make_driver()
    try:
        wait_activity(driver, APP_ACTIVITY, timeout=20)
        goto_alarm_tab(driver)

        if not tap_fab_add_alarm(driver):
            raise RuntimeError("Не найден/не нажат FAB добавления будильника")

        sleep(2)
        close_optional_dialogs(driver)

        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, "//*[contains(@text,'Будильник') or contains(@text,'Alarm')]")
                )
            )
        except TimeoutException:
            pass

        try:
            driver.back()
            sleep(1)
        except Exception:
            pass

        print("OK: Тап по FAB выполнен.")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
