from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

from utility import is_contain_keyword
from webDriver import getWebDriver
from bs4 import BeautifulSoup
import time

def getFeaturedCalendars(site_url):
    driver = getWebDriver()
    driver.get(site_url)
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.page-content")))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    topic = soup.find('h1', attrs={'class': 'jsx-1125610248 mb-0'}).text
    card_wrappers = soup.find_all('div', attrs={'class': 'card-wrapper'})

    calendars_list = []
    try:
        for card_wrapper in card_wrappers:
            try:
                href_element = card_wrapper.find('a', attrs={'class': 'event-link content-link'})
                event_url = 'https://lu.ma' + href_element.get('href')

                title_element = card_wrapper.find('h3', attrs={'class': 'jsx-3851280986'})
                event_title = title_element.text

                if (is_contain_keyword(topic) or is_contain_keyword(event_title)):
                    calendars_list.append({
                        'event_url': event_url,
                        'event_title': event_title,
                    })

            except NoSuchElementException:
                print("Unable to locate elements in card-wrapper")

    except TimeoutException:
        print("Timed out waiting for time line to load")
    except Exception as e:
        print(f'error: {e}')

    return calendars_list