
def test_open_close(driver):
    driver.get("https://example.com/")
    assert "Example" in driver.title
