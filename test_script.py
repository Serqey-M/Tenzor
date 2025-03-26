import logging
import time
import pytest
import yaml
from testpage import OperationsHelper


with open("testdata.yaml", encoding="utf-8") as f:
    testdata = yaml.safe_load(f)

    # def test_script1(browser):
    #     logging.info("Сценарий 1 запущен")
    #     testpage = OperationsHelper(browser)
    #     testpage.go_to_site()
    #     testpage.click_link_contacts()
    #     testpage.click_link_offices_in_region()
    #     testpage.click_banner_tenzor()
    #     testpage.go_to_tab(1)
    #     time.sleep(testdata['sleep_time'])
    #     assert testpage.get_name_block_strength_in_people() == testdata['power_in_people'], 'Тест 1'
    #     testpage.click_block_strength_in_people_detailed()
    #     height_img1 = testpage.get_height_img1()
    #     width_img1 = testpage.get_width_img1()
    #     height_img2 = testpage.get_height_img2()
    #     width_img2 = testpage.get_width_img2()
    #     height_img3 = testpage.get_height_img3()
    #     width_img3 = testpage.get_width_img3()
    #     height_img4 = testpage.get_height_img4()
    #     width_img4 = testpage.get_width_img4()
    #     assert height_img1 == height_img2 == height_img3 == height_img4, 'тест 2'
    #     assert width_img1 == width_img2 == width_img3 == width_img4, "тест 3"
    #     logging.info("Сценарий 1 завершен")

    # def test_script2(browser):
    #     logging.info("Сценарий 2 запущен")
    #     testpage = OperationsHelper(browser)
    #     testpage.go_to_site()
    #     testpage.click_link_contacts()
    #     testpage.click_link_offices_in_region()
    #     assert testpage.get_name_region() == testdata['Nizhny_Novgorod_region'], "Тест 1"
    #     list_partners_1 = testpage.get_list_partners()
    #     testpage.click_name_region()
    #     testpage.click_Kamchatka()
    #     time.sleep(testdata["sleep_time"])
    #     assert testpage.get_name_region() == testdata['Kamchatka_Region'], "Тест 2"
    #     assert testpage.get_list_partners() != list_partners_1, "Тест 3"
    #     assert testpage.get_url() == testdata["url_Kamchatka"], "Тест 4"
    #     assert testpage.get_title() == testdata["title_Kamchatka"], "Тест 5"
    #     logging.info("Сценарий 2 завершен")

    def test_script3(browser):
        logging.info("Сценарий 3 запущен")
        testpage = OperationsHelper(browser)
        testpage.go_to_site()
        testpage.click_download_local_versions()
        time.sleep(testdata["sleep_time"])
        logging.info(testpage.get_url())
        logging.info(len(testpage.get_list_tabs()))
        testpage.click_download()
        time.sleep(testdata["sleep_time"])


if __name__ == "__main__":
    pytest.main(["-v"])
