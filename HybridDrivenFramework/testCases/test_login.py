import pytest
from selenium import webdriver
from pageObjects.LoginPageObjects import LoginPages
import time
from utilities.readProperty import ReadConfig
from utilities.customLogger import LogGen

#grouping-----  pytest -s -v -m "sanity"  --html=./Reports/report.html -n=2 testCases/ --browser chrome

class Test_001_login:
    base_url = ReadConfig.getBaseURL()
    user = ReadConfig.getUserName()
    pwd = ReadConfig.getPwd()
    logger = LogGen.loggen()

    def test_page_title(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.logger.info("******************test_page_title*********")
        actua_title = self.driver.title
        if actua_title == "OrangeHRM":
            self.driver.close()
            self.logger.info("******************test_page_title*********")
            self.logger.info("******************Title is verified Test case is PASS*********")
            assert True
        else:
            self.driver.close()
            self.logger.info("******************Title is verified Test case is Fail*********")
            assert False

    def test_login_test(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(3)
        self.obj = LoginPages(self.driver)
        self.obj.set_user_name(self.user)
        self.obj.set_user_password(self.pwd)
        self.obj.click_login_button()
        self.logger.info("**************test_login_test*************")
        emp_verify = self.obj.get_emp_is_Displayed()
        self.obj.click_logout()
        self.driver.close()
        assert emp_verify is True
        self.logger.info("******************Title is verified Test case is Pass*********")
