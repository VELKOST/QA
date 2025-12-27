from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions

APP_PACKAGE  = "com.google.android.deskclock"
APP_ACTIVITY = "com.android.deskclock.DeskClock"

opts = AppiumOptions()
opts.load_capabilities({
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "Android Emulator",
    "appium:appPackage": APP_PACKAGE,
    "appium:appActivity": APP_ACTIVITY,
    "appium:appWaitActivity": "*",
    "appium:noReset": True,
    "appium:newCommandTimeout": 300
})

d = webdriver.Remote("http://127.0.0.1:4723", options=opts)

# 1) Сохраним полную разметку
open("page_source.xml", "w", encoding="utf-8").write(d.page_source)

# 2) Выведем все кликабельные элементы с id/desc/text
els = d.find_elements(AppiumBy.XPATH, "//*[@clickable='true' or @resource-id or @content-desc]")
for e in els:
    rid = e.get_attribute("resource-id")
    desc = e.get_attribute("contentDescription")
    txt  = e.get_attribute("text")
    if any(s in (rid or "") for s in ("deskclock", "alarm", "fab")) or any(t for t in (desc, txt) if t):
        print(rid, "| desc:", desc, "| text:", txt)
d.quit()
print("Saved to page_source.xml")
