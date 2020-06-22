import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class test_test:
    def test_demo(self):
        driver = webdriver.Chrome(executable_path="E:\\Selenium\\chromedriver_win32\\chromedriver.exe")
        driver.get('https://rahulshettyacademy.com/angularpractice/')

        driver.maximize_window()
        driver.find_element_by_name("name").send_keys("shashi")
        driver.find_element_by_name("email").send_keys("shashi.mar31@gmail.com")
        driver.find_element_by_id("exampleInputPassword1").send_keys("xxxxxx")

        select_gender = Select(driver.find_element_by_id("exampleFormControlSelect1"))
        select_gender.select_by_visible_text("Female")

        driver.find_element_by_id("inlineRadi").click() #driver.find_element_by_id("inlineRadio1").click()
        driver.find_element_by_name("bday").send_keys("30/11/1989")
        driver.find_element_by_xpath("//input[@type='submit']").click()

        print(driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text)