from selenium.webdriver.common.by import By
from PageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    def __init__(self,driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class = 'card h-100']")
    product_name = "div/h4/a"
    Button_name = "div[2]/button"
    checkout_Button = (By.XPATH, "//a[contains(text(),'Checkout')]")
    checked_out_products = (By.XPATH, "//tbody/tr/td/div/div/h4")
    final_checkout_button = (By.XPATH, "//button[contains(text(),'Checkout')]")

    def get_product_elements(self):
        return self.driver.find_elements(*CheckOutPage.products)

    def get_product_name(self):
        return self.product_name

    def get_ButtonName(self):
        return self.Button_name

    def get_checkout_button(self):
        return self.driver.find_element(*CheckOutPage.checkout_Button)

    def get_products_final(self):
        return self.driver.find_elements(*CheckOutPage.checked_out_products)

    def get_final_checkout_button(self):
        self.driver.find_element(*CheckOutPage.final_checkout_button).click()
        confirmPageObj = ConfirmPage(self.driver)
        return confirmPageObj





