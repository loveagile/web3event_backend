from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webDriver import getWebDriver

def mGetPopularEventList():
    driver = getWebDriver()
    driver.get('https://lu.ma/discover')
    WebDriverWait(driver, 4).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.can-divide")))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    event_sections = soup.find_all('div', attrs={'class': 'can-divide'})

    popular_event_a_elements = event_sections[0].find_all('a')
    popular_event_href_values = ['https://lu.ma' + a_element.get('href') for a_element in popular_event_a_elements]

    featured_calendar_a_elements = event_sections[1].find_all('a')
    featured_calendar_href_values = ['https://lu.ma' + a_element.get('href') for a_element in featured_calendar_a_elements]


    list_luma = []
    event_sections = driver.find_elements(By.CSS_SELECTOR, 'div.can-divide')
    city_event_elements = event_sections[0].find_elements(By.TAG_NAME, 'a')
    calender_event_elements = event_sections[1].find_elements(By.TAG_NAME, 'a')
    city_event_href_values = [element.get_attribute('href') for element in city_event_elements]
    calender_event_href_values = [element.get_attribute('href') for element in calender_event_elements]
    print(calender_event_href_values)


    # soup = BeautifulSoup(driver.page_source, 'html-parser')
    # print(soup)
