# pages/contact_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class ContactPage(BasePage):
    # Демо-форма из официальной документации Selenium:
    URL = "https://www.selenium.dev/selenium/web/web-form.html"

    # Локаторы (простые и стабильные)
    NAME     = (By.NAME, "my-text")       # обязательное поле
    COMMENT  = (By.NAME, "my-textarea")   # произвольный текст
    SUBMIT   = (By.CSS_SELECTOR, "button")  # единственная кнопка
    MESSAGE  = (By.ID, "message")         # статус после отправки

    def open(self):
        return super().open(self.URL)

    # действия
    def fill_name(self, value: str):
        self.type(self.NAME, value)
        return self

    def fill_comment(self, value: str):
        self.type(self.COMMENT, value)
        return self

    def submit(self):
        self.click(self.SUBMIT)
        return self

    # проверки/данные
    def success_text(self) -> str:
        return self.wait_present(self.MESSAGE).text

    # валидация HTML5 (для негативного кейса)
    def is_name_valid(self) -> bool:
        el = self.find(self.NAME)
        return self.js("return arguments[0].checkValidity()", el)

    def name_validation_message(self) -> str:
        el = self.find(self.NAME)
        # показать нативное сообщение браузера и вернуть его текст
        self.js("arguments[0].reportValidity()", el)
        return self.js("return arguments[0].validationMessage", el)

    def make_name_required(self):
        el = self.find(self.NAME)
        self.js("arguments[0].setAttribute('required','')", el)
        return self