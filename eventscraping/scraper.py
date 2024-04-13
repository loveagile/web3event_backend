from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

from webDriver import getWebDriver
from cityEventDetails import getPopularCityEvents
from featuredCalendarDetails import getFeaturedCalendars
from constant import backend_url

def discover_event_list(site_url):
    driver = getWebDriver()
    driver.get(site_url)
    WebDriverWait(driver, 4).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.can-divide")))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    event_sections = soup.find_all('div', attrs={'class': 'can-divide'})

    popular_city_elements = event_sections[0].find_all('a')
    popular_city_hrefs = ['https://lu.ma' + city_element.get('href') for city_element in popular_city_elements]
    new_event_path = backend_url + 'api/v1/web3events/new/'

    for popular_city_href in popular_city_hrefs:
        popular_city_events = getPopularCityEvents(popular_city_href)
        for event in popular_city_events:
            requests.post(new_event_path, {
                "event_url": event['event_url'],
                "event_title": event['event_title'],
                "event_organizer": event['event_organizer'],
                "event_location": event['event_location'],
                "event_img_url":  event['event_img_url'],
            })

    featured_calendar_elements = event_sections[1].find_all('a')
    featured_calendar_hrefs = ['https://lu.ma' + calendar_element.get('href') for calendar_element in featured_calendar_elements]
    for featured_calendar_href in featured_calendar_hrefs:
        featured_calendar_events = getFeaturedCalendars(featured_calendar_href)
        for event in featured_calendar_events:
            requests.post(new_event_path, {
                "event_url": event['event_url'],
                "event_title": event['event_title'],
            })


if __name__ == '__main__':
    discover_event_list('https://lu.ma/discover')
    # backgroundScheduler = BackgroundScheduler()
    # backgroundScheduler.add_job(discover_event_list, 'interval', minutes = 1, start_date = datetime.now())
    # backgroundScheduler.start()