import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@when('Navigate to leave page')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//span[text()='Leave']").click()
    time.sleep(3)
@then('leave page should display')
def step_impl(context):
    pass

@when('Navigate to Time page')
def step_impl(context):
    pass

@then('Time page should display')
def step_impl(context):
    pass