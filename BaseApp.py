import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import yaml

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = testdata['address']

    # Переход по указанному url
    def go_to_site(self, url = testdata["address"]):
        try:
            start_browsing = self.driver.get(url) 
            logging.info(f"Открытие страницы {url}")
        except:
            logging.exception(f"Ошибка при открытии страницы {url}")
            start_browsing = None
        return start_browsing

    # Поиск элемента
    def find_element(self, locator, time=testdata["implicitly_wait"], description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                message=f'Не удается найти элемент "{element_name}"',
            )
            logging.info(f'Элемент "{element_name}" найден')
        except:
            logging.exception(f'Элемент "{element_name}" не найден')
            element = None
        return element

    # Поиск нескольких элементов
    def find_elements(self, locator, time=testdata["implicitly_wait"], description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        try:
            element = WebDriverWait(self.driver, time).until(
                EC.presence_of_all_elements_located(locator),
                message=f'Не удается найти элементы в "{element_name}"',
            )
            logging.info(f'Элементы в "{element_name}" найдены')
        except:
            logging.exception(f'Элементы в "{element_name}" не найден')
            element = None
        return element

    # Получаем свойство элемента
    def get_element_property(self, locator, property, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        try:
            element = self.find_element(locator, description = description)
            logging.info(
                f'Свойство "{property}" у элемента "{element_name}" равно "{element.value_of_css_property(property)}"'
            )
        except:
            logging.exception(f'Свойство "{property}" у элемента "{element_name}" не найдено')
            return None
        return element.value_of_css_property(property)

    # Переход по вкладкам
    def go_to_tab(self, tab, description=None):
        if description:
            element_name = description
        else:
            element_name = tab
        try:
            self.driver.switch_to.window(self.driver.window_handles[tab])
            logging.info(f'Переход на вкладку "{element_name}"')
        except:
            logging.exception(f'Ошибка при переходе на вкладку "{element_name}"')

    # Клик по элементу
    def click_button(self, locator, description = None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator, description=description)
        if not button:
            logging.exception(f'Кнопка "{element_name}" не найдена')
            return False
        try:
            button.click()
            logging.info(f'Клик по кнопке "{element_name}"')
        except:
            logging.exception(f'Ошибка при клике по кнопке "{element_name}"')

    # Получение текста из элемента
    def get_text_from_element(self, locator, description = None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=testdata["implicitly_wait"], description = description)
        if not field:
            logging.exception(f'Элемент "{element_name}" не найден')
            return None
        try:
            text = field.text
            logging.info(f'Получаем текст "{text}" из элемента "{element_name}"')
        except:
            logging.exception(f'Ошибка при получении текста из элемента "{element_name}"')
            return None
        return text

    # Получение текущего url
    def get_url(self):
        try:
            current_url = self.driver.current_url
            logging.info(f'Получен url страницы {current_url}')
        except:
            logging.exception("Ошибка при получении url страницы")
            current_url = None
        return current_url

    # Получение текущего title
    def get_title(self):
        try:
            title = self.driver.title
            logging.info(f'Получен title страницы "{title}"')
        except:
            logging.exception("Ошибка при получении title страницы")
            title = None
        return title

    # Получение списка вкладок
    def get_list_tabs(self, description=None):
        try:
            self.driver.window_handles
            logging.info('Получен список вкладок')
        except:
            logging.exception("Не получен список вкладок")
