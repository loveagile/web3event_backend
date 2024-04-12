from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import urllib

def getWebDriver():
    options = Options()
    options.add_argument('--disable-extensions')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--no-headless")
    options.add_argument('--disable-plugins-discovery')
    options.add_argument('--profile-directory=Default')
    options.add_argument('--disable-logging')
    options.add_argument('--enable-features=NetworkServiceInProcess')
    options.add_argument('--disable-domain-reliability')
    options.add_argument('--log-level=0')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
    options.add_experimental_option("prefs", prefs)
    try:
        driver = webdriver.Chrome(options=options)
    except ValueError :
        latest_chromedriver_version_url = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
        latest_chromedriver_version = urllib.request.urlopen(latest_chromedriver_version_url).read().decode('utf-8')
        service = Service(ChromeDriverManager(driver_version=latest_chromedriver_version).install())
        driver = webdriver.Chrome(service=service, options=options)

    return driver