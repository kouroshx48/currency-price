from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent
class CurrencyPrice:

    def __init__(self):
        options = Options()
        options.add_argument(f"user-agent={UserAgent('chrome').random}")
        chrome_path = '/usr/local/bin/chromedriver'
        services = Service(chrome_path)
        driver = webdriver.Chrome(service=services,options=options)
        self.driver = driver

    @property
    def currency_prices(self):
        self.driver.get('https://www.tgju.org/currency')
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        print(soup.prettify)


CurrencyPrice().currency_prices