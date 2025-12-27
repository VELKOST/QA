# tests/test_contact_form.py
import pytest
from pages.contact_page import ContactPage

@pytest.mark.ui
def test_contact_form_positive(driver, wait):
    """
    Позитив: заполняем форму валидными данными, отправляем,
    убеждаемся, что на странице есть статус об успешной отправке.
    """
    page = ContactPage(driver, wait).open()
    page.fill_name("Иван Иванов").fill_comment("Тестовое сообщение").submit()

    msg = page.success_text().lower()

    assert "submitted" in msg or "received" in msg


@pytest.mark.ui
def test_contact_form_negative_required_field(driver, wait):
    page = ContactPage(driver, wait).open()

    # Делаем поле обязательным для этой сессии
    page.make_name_required()

    # Пытаемся отправить пустую форму
    page.submit()

    # Теперь нативная валидация должна сработать
    assert page.is_name_valid() is False, "Ожидали, что обязательное поле будет невалидно"
    validation_msg = page.name_validation_message()
    assert validation_msg.strip(), "Должно быть показано нативное сообщение браузера"