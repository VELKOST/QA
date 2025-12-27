import re
import requests
from jsonschema import validate

GET_USER_SCHEMA = {
    "type": "object",
    "required": ["id", "name", "username", "email", "address", "company"],
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "username": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "address": {
            "type": "object",
            "required": ["street", "suite", "city", "zipcode", "geo"],
            "properties": {
                "street": {"type": "string"},
                "suite": {"type": "string"},
                "city": {"type": "string"},
                "zipcode": {"type": "string"},
                "geo": {
                    "type": "object",
                    "required": ["lat", "lng"],
                    "properties": {
                        "lat": {"type": "string"},
                        "lng": {"type": "string"},
                    },
                },
            },
        },
        "phone": {"type": "string"},
        "website": {"type": "string"},
        "company": {
            "type": "object",
            "required": ["name"],
            "properties": {"name": {"type": "string"}},
        },
    },
}

EMAIL_RE = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")

def test_get_user_1(base_url):
    resp = requests.get(f"{base_url}/users/1", timeout=10)
    assert resp.status_code == 200
    data = resp.json()
    # схема
    validate(instance=data, schema=GET_USER_SCHEMA)
    # конкретные значения
    assert data["id"] == 1
    assert EMAIL_RE.match(data["email"])

def test_post_user(base_url):
    payload = {
        "name": "Ada Lovelace",
        "username": "ada",
        "email": "ada@example.com",
    }
    resp = requests.post(f"{base_url}/users", json=payload, timeout=10)
    # JSONPlaceholder возвращает 201 и отзеркаливает тело + добавляет id
    assert resp.status_code == 201
    data = resp.json()
    for k, v in payload.items():
        assert data[k] == v
    assert "id" in data  # обычно число (фиктивное), значение проверять не обязательно

def test_put_user_1(base_url):
    payload = {
        "id": 1,
        "name": "Ada L.",
        "username": "ada",
        "email": "ada@example.com",
    }
    resp = requests.put(f"{base_url}/users/1", json=payload, timeout=10)
    assert resp.status_code == 200
    data = resp.json()
    # JSONPlaceholder возвращает объединение того, что вы отправили
    assert data["id"] == 1
    assert data["name"] == "Ada L."
    assert data["username"] == "ada"
    assert data["email"] == "ada@example.com"
