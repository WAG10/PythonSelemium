from utilities.utility import baseclass
from PageObjects.HomePage import HomePage


class TestDirectoryInit(baseclass):

    def test_cwd_starts(self, setup):

        log = self.get_logger()

        homepageobj= HomePage(self.driver)
        log.info("homepageobj created")

        confirmPageObj = None

        checkOutPageObj = homepageobj.shop_element()
        log.info("checkOutPageObj created")

        products = checkOutPageObj.get_product_elements()
        log.info(products)
        for product in products:

            if product.find_element_by_xpath(checkOutPageObj.get_product_name()).text == "Blackberry":
                product.find_element_by_xpath(checkOutPageObj.Button_name).click()
                log.info("Blackberry selected")
                break

        checkOutPageObj.get_checkout_button().click()
        log.info("checkout clicked")

        checked_out_products = checkOutPageObj.get_products_final()

        for checked_out_product in checked_out_products:
            assert (checked_out_product.text == "Blackberry")
            confirmPageObj = checkOutPageObj.get_final_checkout_button()
            break

        confirmPageObj.get_country_textbox().send_keys("ind")

        self.wait_until_link_text("India")
        log.info("india selected")

        confirmPageObj.get_confirm_checkbox().click()
        log.info("checkbox clicked")
        confirmPageObj.get_purchase_button().click()
        text_message = self.driver.find_element_by_class_name("alert-success").text
        log.info(text_message)
        assert ("Success" in text_message)
        log.info("assert passed")
        self.driver.get_screenshot_as_file("result.png")
        log.info("screen shot created")



