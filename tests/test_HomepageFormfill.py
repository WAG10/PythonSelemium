from utilities.utility import baseclass
from PageObjects.HomePage import HomePage
from testData.homepageData import homepage_data
import pytest


class TestDirectoryInit(baseclass):

    def test_cwd_starts(self,data_provider):
        homepageobj = HomePage(self.driver)
        homepageobj.get_name().send_keys(data_provider["name"])
        homepageobj.get_email().send_keys(data_provider["email"])
        homepageobj.get_password().send_keys("xxxxxx")
        self.selectoption_By_visible_text(homepageobj.get_gender(), data_provider["Gender"])
        homepageobj.get_status().click()
        homepageobj.get_bday().send_keys("30/11/1989")
        homepageobj.get_submit().click()
        alert_msg = homepageobj.get_success_message().text
        assert ("Success" in alert_msg)
        self.driver.get_screenshot_as_file("result.png")



    @pytest.fixture(params= baseclass.get_data_from_excel("test1"))
    def data_provider(self, request):
        return request.param









