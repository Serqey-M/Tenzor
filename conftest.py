import os
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from chromedriver_py import binary_path

with open("testdata.yaml", encoding="utf-8") as f:
    testdata = yaml.safe_load(f)

# Инициализация webdriver
@pytest.fixture(scope="session")
def browser():
    svc = webdriver.ChromeService(executable_path=binary_path)
    chrome_options = Options()
    chrome_options.add_experimental_option(
        "prefs",
        {
            "download.default_directory": os.path.abspath("\Tensor"),
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
        },
    )
    driver = webdriver.Chrome(service=svc, options=chrome_options)
    driver.implicitly_wait(testdata["implicitly_wait"])
    driver.maximize_window()
    yield driver
    driver.quit()
