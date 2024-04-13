from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

from utility import is_contain_keyword
from webDriver import getWebDriver
from bs4 import BeautifulSoup
import time

def getPopularCityEvents(site_url):
    driver = getWebDriver()
    driver.get(site_url)
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.main-content-wrapper")))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    card_wrappers = soup.find_all('div', attrs={'class': 'card-wrapper'})

    events_list = []
    try:
        for card_wrapper in card_wrappers:
            try:
                href_element = card_wrapper.find('a', attrs={'class': 'event-link content-link'})
                event_url = 'https://lu.ma' + href_element.get('href')

                title_element = card_wrapper.find('h3', attrs={'class': 'jsx-3851280986'})
                event_title = title_element.text

                company_elements = card_wrapper.find_all('div', attrs={'class': 'jsx-3575689807 text-ellipses'})
                organizer_element = company_elements[0]
                event_organizer = organizer_element.text
                location_element = company_elements[1]
                event_location = location_element.text

                image_element = card_wrapper.find('img')
                event_img_url = image_element.get('src')

                if (is_contain_keyword(event_title)):
                    events_list.append({
                        'event_url': event_url,
                        'event_title': event_title,
                        'event_organizer': event_organizer,
                        'event_location': event_location,
                        'event_img_url': event_img_url
                    })

            except NoSuchElementException:
                print("Unable to locate elements in card-wrapper")

    except TimeoutException:
        print("Timed out waiting for time line to load")
    except Exception as e:
        print(f'error: {e}')

    return events_list