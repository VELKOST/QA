
# Selenium + Pytest Demo (Chrome/Firefox via webdriver-manager)

## Setup
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

## Quick smoke
```bash
pytest -q tests/test_open_close.py
```
or
```bash
python scripts/open_close.py
```

## Login test
```bash
pytest -q tests/test_login.py --browser=chrome --headless
```
Default site: https://the-internet.herokuapp.com/login  
Creds: `tomsmith` / `SuperSecretPassword!`

### Options
- `--browser=chrome|firefox` (default chrome)
- `--headless`

### Env vars (optional)
`DEMO_USERNAME`, `DEMO_PASSWORD` to override creds.

## Если хотите видеть больше подробностей:

### Вербозный режим:
```bash
pytest -v tests/test_login.py
```
### Печатать вывод/принты:
```bash
pytest -s tests/test_login.py
```
### Запустить в «головном» режиме (видеть окно браузера):
```bash
pytest tests/test_login.py --browser=chrome
```

## Запуски V2:

Позитив/негатив только этой формы:
```bash
pytest -q tests/test_contact_form.py
```
В хедлесс/другом браузере:
```bash
pytest tests/test_contact_form.py --browser=firefox --headless
```