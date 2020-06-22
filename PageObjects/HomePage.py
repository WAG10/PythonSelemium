from selenium.webdriver.common.by import By
from PageObjects.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    gender = (By.ID, "exampleFormControlSelect1")
    studentOrEmployed = (By.ID, "inlineRadio1")
    bday = (By.NAME, "bday")
    submit = (By.XPATH, "//input[@type='submit']")
    success_msg = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")


    def shop_element(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPageObj = CheckOutPage(self.driver)
        return checkoutPageObj

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_password(self):
        return self.driver.find_element(*HomePage.password)

    def get_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def get_status(self):
        return self.driver.find_element(*HomePage.studentOrEmployed)

    def get_bday(self):
        return self.driver.find_element(*HomePage.bday)

    def get_submit(self):
        return self.driver.find_element(*HomePage.submit)

    def get_success_message(self):
        return self.driver.find_element(*HomePage.success_msg)



