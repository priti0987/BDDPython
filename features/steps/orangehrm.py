import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch chrome browser')
def launch_chrome_browser(context):
    context.driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")


@when('open orange hrm homepage')
def open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    context.driver.maximize_window()
    time.sleep(3)

@then('verify that the logo present on page')
def verify(context):
    status = context.driver.find_element(By.XPATH,"//div[@class='orangehrm-login-branding']/img").is_displayed()
    assert status is True
@then('close browser')
def close_page(context):
    context.driver.close()