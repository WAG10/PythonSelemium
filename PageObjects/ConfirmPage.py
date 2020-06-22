from selenium.webdriver.common.by import By

class ConfirmPage:
    def __init__(self,driver):
        self.driver = driver

    country_textbox = (By.ID, "country")
    confirm_checkBox = (By.CLASS_NAME, "checkbox-primary")
    purchase_button = (By.XPATH, "//input[@value='Purchase']")

    def get_country_textbox(self):
        return self.driver.find_element(*ConfirmPage.country_textbox)

    def get_confirm_checkbox(self):
        return self.driver.find_element(*ConfirmPage.confirm_checkBox)

    def get_purchase_button(self):
        return self.driver.find_element(*ConfirmPage.purchase_button)

