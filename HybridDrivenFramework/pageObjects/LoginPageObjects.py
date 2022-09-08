from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPages:
    user_name = "username"
    password_password = "password"
    login_button = "//button[text()=' Login ']"
    logout_xpath = "//p[contains(text(),'Paul Collings')]"
    logout_click_xpath = "//a[text()='Logout']"
    emp_list = "//a[text()='Employee List']"

    def __init__(self, driver):
        self.driver = driver

    def set_user_name(self, user):
        self.driver.find_element(By.NAME,self.user_name).clear()
        self.driver.find_element(By.NAME,self.user_name).send_keys(user)

    def set_user_password(self, pwd):
        self.driver.find_element(By.NAME,self.password_password).clear()
        self.driver.find_element(By.NAME,self.password_password).send_keys(pwd)

    def click_login_button(self):
        self.driver.find_element(By.XPATH,self.login_button).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH,self.logout_xpath).click()
        dis = self.driver.find_element(By.XPATH,self.logout_click_xpath)
        if dis.is_displayed() is True:
            self.driver.find_element(By.XPATH,self.logout_click_xpath).click()

    def get_emp_is_Displayed(self):
        emplist = self.driver.find_element(By.XPATH,self.emp_list).is_displayed()
        return emplist
