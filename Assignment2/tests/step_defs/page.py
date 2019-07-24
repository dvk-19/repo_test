from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import logging


def set_search(driver,phrase):
    driver.find_element_by_name('q').send_keys(phrase)
    driver.find_element_by_name('q').send_keys(Keys.RETURN)

def click_link(driver):
    driver.find_element(By.CSS_SELECTOR, ".bkWMgd > .g .LC20lb").click()

def click_download(driver):
    click_element = driver.find_element_by_link_text("Download in another language")
    click_element.click()



