from selenium import webdriver
from selenium.webdriver.common.by import By


class EmployeeList:
    employee_add = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']/i"
    employee_header = "//h6[text()='Add Employee']"
    employee_firstName = "firstName"
    employee_lastName = "lastName"
    employee_id = "//form//input[@class='oxd-input oxd-input--active']"
    employee_cancel = "//button[@class='oxd-button oxd-button--medium oxd-button--ghost']"
    employee_save = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def click_addEmployee(self):
        self.driver.find_element(By.XPATH, self.employee_add).click()

    def getEmployeeId(self):
        return self.driver.find_element(By.XPATH, self.employee_id).text

    def verify_employeeHeader(self):
        return self.driver.find_element(By.XPATH, self.employee_header).is_displayed()

    def verify_cancel_Button(self):
        return self.driver.find_element(By.XPATH, self.employee_cancel).is_displayed()

    def enter_firstName(self, name):
        self.driver.find_element(By.NAME, self.employee_firstName).clear()
        self.driver.find_element(By.NAME, self.employee_firstName).send_keys(name)

    def enter_lastName(self, lastname):
        self.driver.find_element(By.NAME, self.employee_lastName).clear()
        self.driver.find_element(By.NAME, self.employee_lastName).send_keys(lastname)

    def click_Save_button(self):
        self.driver.find_element(By.XPATH, self.employee_save).click()
