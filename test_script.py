import logging
import time
import pytest
import yaml
from testpage import OperationsHelper


with open("D:\Tensor\\testdata.yaml", encoding="utf-8") as f:
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
#     assert testpage.get_name_block_strength_in_people() == 'Сила в людях', 'Тест 1'
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


def test_script2(browser):
    logging.info("Сценарий 2 запущен")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.click_link_contacts()
    testpage.click_link_offices_in_region()
    assert testpage.get_name_region() == 'Нижегородская обл.', 'Тест 1'
    list_of_partners_1 = testpage.get_list_of_partners()
    testpage.click_name_region()
    testpage.click_Kamchatka()
    assert testpage.get_name_region() == "Камчатский край", "Тест 2"
    time.sleep(testdata["sleep_time"])


if __name__ == "__main__":
    pytest.main(["-v"])
