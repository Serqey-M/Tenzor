import pytest
import yaml
from selenium import webdriver

from chromedriver_py import binary_path

with open("testdata.yaml", encoding="utf-8") as f:
    testdata = yaml.safe_load(f)

# Инициализация webdriver
@pytest.fixture(scope="session")
def browser():
    svc = webdriver.ChromeService(executable_path=binary_path)
    driver = webdriver.Chrome(service=svc)
    driver.implicitly_wait(testdata["implicitly_wait"])
    driver.maximize_window()
    yield driver
    driver.quit()