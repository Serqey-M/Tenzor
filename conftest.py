# import logging
import pytest
import yaml
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
from chromedriver_py import binary_path

with open("D:\Tensor\\testdata.yaml", encoding="utf-8") as f:
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


# @pytest.fixture(scope="session")
# def browser():
#     driver = webdriver.Chrome(executable_path="./chromedriver")
#     yield driver
#     driver.quit()


# @pytest.fixture(scope='session')
# def browser():
#     service = Service(executable_path=ChromeDriverManager().install())
#     options = webdriver.ChromeOptions()
#     driver = webdriver.Chrome(service=service, options=options)
#     driver.implicitly_wait(testdata['implicitly_wait'])
#     driver.maximize_window()
#     yield driver
#     driver.quit()
