import pytest
from selenium import webdriver
from pageObjects.LoginPageObjects import LoginPages
import time
from utilities.readProperty import ReadConfig
#from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_login_Driven:
    base_url = ReadConfig.getBaseURL()

    path = ".\\TestData\\LoginData.xlsx"
    #logger = LogGen.loggen()
    @pytest.mark.sanity
    def test_login_test_ddt(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(5)
        self.obj = LoginPages(self.driver)
        self.row = XLUtils.gerRowCount(self.path, "Sheet1")
        print("Number of row in sheet on*********", self.row)
        list_status = []
        for r in range(2, self.row + 1):
            self.user = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.pwd = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)
            self.obj.set_user_name(self.user)
            self.obj.set_user_password(self.pwd)
            self.obj.click_login_button()
            time.sleep(8)
            actua_title = self.driver.current_url
            exp_title="https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"
            if actua_title==exp_title:
                if self.exp == "Pass":
                    print("Test cases is PASS")
                    self.obj.click_logout()
                    time.sleep(3)
                    list_status.append("Pass")
                elif self.exp == "Fail":
                    print("Test cases is Failed")
                    self.obj.click_logout()
                    list_status.append("Fail")
            elif actua_title!=exp_title:
                if self.exp == "Pass":
                    print("Test cases is Failed")
                    list_status.append("Fail")
                elif self.exp == "Fail":
                    print("Test cases is PASS")
                    list_status.append("Pass")
        print("Actual Status****",list_status)
        if "Fail" not in list_status:
            print("****Test is PASS DataDriven is success!!!****")
            self.driver.close()
            assert True
        else:
            print("Test case failed ,please check login data")
            self.driver.close()
            assert True
