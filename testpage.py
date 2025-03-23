import logging
from BaseApp import BasePage
from selenium.webdriver.common.by import By
import yaml

# Поиск локаторов
class Locators:
    ids = dict()
    with open("D:\Tensor\locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators['XPATH'].keys():
        ids[locator] = (By.XPATH, locators['XPATH'][locator])
    for locator in locators['CSS_SELECTOR'].keys():
        ids[locator] = (By.CSS_SELECTOR, locators['CSS_SELECTOR'][locator])


class OperationsHelper(BasePage):

    # Ввод текста
    # def enter_login(self, word):
    #     self.enter_terxt_into_field(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'], word, description = 'login form')

    # клик

    def click_link_contacts(self):
        self.click_button(
           Locators.ids["LOCATOR_LINK_CONTACTS"],
            description="ссылка контакты",
        )

    def click_link_offices_in_region(self):
        self.click_button(
           Locators.ids["LOCATOR_OFFICES_IN_REGION"],
            description="ссылка офисы в регине",
        )

    def click_banner_tenzor(self):
        self.click_button(
            Locators.ids["LOCATOR_BANNER_TENZOR"],
            description = "баннер Тензор",
        )

    def click_block_strength_in_people_detailed(self):
        self.find_element(
            Locators.ids["LOCATOR_BLOCK_STRENGTH_IN_PEOPLE_DETAILED"],
            description = "ссылка 'подроднее' в блоке 'Сила в людях'",
        )

    # получить
    # def get_name_block_strength_in_people(self):
    #     return self.find_element(
    #         Locators.ids["LOCATOR_NAME_BLOCK_STRENGTH_IN_PEOPLE"], description='zzz'
    #     ).text
