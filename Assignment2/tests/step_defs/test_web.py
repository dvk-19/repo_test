import _pytest.fixtures
from pytest_bdd import given, parsers, when, then, scenario
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import page
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


google_page = 'https://google.co.in'
file_path = '../features/web.feature'
# better not to hardcode the path,
# instead can be fetched using os.path

@_pytest.fixtures.fixture()
def driver():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    return browser

@scenario(file_path,'When I search google, to download firefox')
def test_searchresults():

    """Search the phrase 'Firefox' and the results displayed are for Firefox """

@given('Google Search Engine')
def search_Firefox(driver):
    driver.get(google_page)

@when(parsers.parse('I enter {phrase}'))
def search(driver, phrase):
    page.set_search(driver, phrase)
    page.click_link(driver)
    page.click_download(driver)


@then("Results for Firefox are found")
def select_dropdown(driver):
    driver.find_element(By.ID, "select_desktop_release_language").click()
    dropdown = Select(driver.find_element(By.ID, "select_desktop_release_language"))
    print (str(len(dropdown.options)))

    for i in dropdown:
        print(i.text)

def tearDown(driver):
    driver.close()











