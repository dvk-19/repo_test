import _pytest.fixtures
import pytest_bdd
from pytest_bdd import given, parsers, when, then, scenario
from selenium import webdriver
import selenium.webdriver.common.keys
from webdriver_manager.chrome import ChromeDriverManager

file_path = '../features/web.feature'


@_pytest.fixtures.fixture()
def browser():
    print('Initiating Chrome browser')
    browser_obj = webdriver.Chrome(ChromeDriverManager().install())
    return browser_obj


@scenario(file_path, 'Basic Google Search')
def test_search():
    """Basic google search"""



@given('The Google Search Page is displayed')
def getsearchpage(browser):
    browser.get('https://www.google.co.in/')


@when(parsers.parse('The user searches for {phrase}'))
def searchFirefox(browser, phrase):
    browser.find_element_by_name('q').send_keys(phrase)
    browser.find_element_by_name('q').send_keys(selenium.webdriver.common.keys.Keys.RETURN)


@then(parsers.parse('the results are shown for {phrase}'))
def resultsFirefox(browser):
    xpath = '//*[@id="rso"]/div[1]/div/div/div/div[1]/a'
    browser.find_element_by_xpath(xpath).click()
    assert isinstance (browser.title,str)
    assert "https://www.mozilla.org" in browser.current_url


def tearDown(browser):
    browser.close()