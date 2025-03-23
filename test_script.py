from datetime import datetime
import logging
import time
import pytest
import yaml
from testpage import OperationsHelper


with open("D:\Tensor\\testdata.yaml", encoding="utf-8") as f:
    testdata = yaml.safe_load(f)


def test_script1(browser):
    logging.info('Test1 Starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.click_link_contacts()
    testpage.click_link_offices_in_region()
    testpage.click_banner_tenzor()
    testpage.click_block_strength_in_people_detailed()
    time.sleep(testdata['sleep_time'])


if __name__ == '__main__':
    pytest.main(['-v'])
