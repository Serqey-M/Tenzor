import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import yaml

with open("D:\Tensor\\testdata.yaml") as f:
    testdata = yaml.safe_load(f)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = testdata['address']

    # Поиск элемента
    def find_element(self, locator, time=10, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        try:
            element = WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located(locator),
                message=f"Не удается найти элемент {element_name}",
            )
        except:
            logging.info(f"Элемент {element_name} не найден")
            element = None
        return element

    # Получаем свойство элемента
    def get_element_property(self, locator, el_property):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(el_property)
        else:
            logging.error(f'Свойство {property} не найдено в элементе с локатором {locator}')
            return None

    # Переход по указанному url
    def go_to_site(self):
        try:
            start_browsing = self.driver.get(self.base_url)   
        except:
            logging.exception("Ошибка при открытии сайта")
            start_browsing = None
        return start_browsing

    # Получаем текст предупреждения(alert)
    def get_alert_text(self):
        try:
            alert = self.driver.switch_to.alert
            logging.exception(f"Получаем предупреждение(alert) {alert.text}")
            return alert.text
        except:
            logging.exception("Ошибка при чтении предупреждения(alert)")
            return None

    # Ввод текста в поле
    def enter_text_into_field(self, locator, word, description = None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'Вводим {word} в элемент {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f"Элемент {element_name} не найдей")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Ошибка при вводе текста в {element_name}")
            return False
        return True

    # Клик по элементу
    def click_button(self, locator, description = None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception('Ошибка при клике по кнопке')
            return False
        logging.debug(f'Клик по кнопке {element_name}')
        return True

    # Получение текста из элемента
    def get_text_from_element(self, locator, description = None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            logging.exception(f"Элемент {element_name} не найден")
            return None
        try:
            text = field.text()
            logging.exception(f"Текст элемента {element_name} {text}")
        except:
            logging.exception(f'Ошибка при получении текста из элемента {element_name}')
            return None
        logging.debug(f'Получаем текст {text} из элемента {element_name}')
        return text
