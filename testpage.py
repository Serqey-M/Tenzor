import logging
from BaseApp import BasePage
from selenium.webdriver.common.by import By
import yaml

# Поиск локаторов
class Locators:
    ids = dict()
    with open("locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators['XPATH'].keys():
        ids[locator] = (By.XPATH, locators['XPATH'][locator])
    for locator in locators["CLASS_NAME"].keys():
        ids[locator] = (By.CLASS_NAME, locators["CLASS_NAME"][locator])


class OperationsHelper(BasePage):

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
        self.click_button(
            Locators.ids["LOCATOR_BLOCK_STRENGTH_IN_PEOPLE_DETAILED"],
            description="ссылка 'подроднее' в блоке 'Сила в людях'")

    def click_name_region(self):
        self.click_button(Locators.ids['LOCATOR_REGION'], description='Название региона')

    def click_Kamchatka(self):
        self.click_button(Locators.ids["LOCATOR_KAMCHATKA"], description='Камчатка')

    # получить
    def get_name_block_strength_in_people(self):
        return self.get_text_from_element(Locators.ids["LOCATOR_NAME_BLOCK_STRENGTH_IN_PEOPLE"], description='Название блока "Сила в людях"')

    def get_height_img1(self):
        return self.get_element_property(Locators.ids["LOCATOR_IMG1"], 'height', description='Изображение 1')

    def get_width_img1(self):
        return self.get_element_property(Locators.ids["LOCATOR_IMG1"], "width", description='Изображение 1')

    def get_height_img2(self):
        return self.get_element_property(Locators.ids["LOCATOR_IMG2"], "height", description='Изображение 2')

    def get_width_img2(self):
        return self.get_element_property(Locators.ids["LOCATOR_IMG2"], "width", description='Изображение 2')

    def get_height_img3(self):
        return self.get_element_property(Locators.ids["LOCATOR_IMG3"], "height", description='Изображение 3')

    def get_width_img3(self):
        return self.get_element_property(Locators.ids["LOCATOR_IMG3"], "width", description='Изображение 3')

    def get_height_img4(self):
        return self.get_element_property(Locators.ids["LOCATOR_IMG4"], "height", description='Изображение 4')

    def get_width_img4(self):
        return self.get_element_property(Locators.ids["LOCATOR_IMG4"], "width", description='Изображение 4')

    def get_name_region(self):
        return self.get_text_from_element(Locators.ids["LOCATOR_REGION"], description='Название региона')
    
    def get_contacts_list(self):
        return self.find_elements(Locators.ids['LOCATOR_CONTACT_LIST'], description= 'Cписок контактов')