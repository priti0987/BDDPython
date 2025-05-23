import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I launch Chrome browser')
def launch(context):
    context.driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")


@when('I open orange hrm Homepage')
def openUrl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    context.driver.maximize_window()
    time.sleep(2)
    status = context.driver.find_element(By.XPATH,"//div[@class='orangehrm-login-branding']/img").is_displayed()
    assert status is True

@when('Enter username "{username}" and password "{pwd}"')
def addcredentials(context,username,pwd):
    context.driver.find_element(By.XPATH,"//input[@name='username']").send_keys(username)
    context.driver.find_element(By.XPATH,"//input[@name='password']").send_keys(pwd)

@when('Click on login button')
def clickButton(context):
    context.driver.find_element(By.XPATH,"//button[@type='submit']").click()
    time.sleep(6)

@then('User must successfully login to the Dashboard page')
def loginVerify(context):
    try:
        text_D = context.driver.find_element(By.XPATH,"//div[contains(@class,'title')]").text
    except:
        context.driver.close()
        assert False,"Test Fail"
    if text_D == "Dashboard":
        context.driver.close()
        assert True,"Test Passed"
