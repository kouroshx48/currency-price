from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent
class CurrencyPrice:

    def __init__(self):
        options = Options()
        options.add_argument(f'user-agent={UserAgent("chrome").random}')
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        self.driver = driver

    @property
    def currency_prices(self):
        self.driver.get('https://www.tgju.org/currency')
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        cells = soup.find('div', {'class':'fs-row'}).find_all('div', {'class' : 'fs-cell'})
        # print(cells)
        # print(len(cells))
        info = {}
        for cell in cells :
            currencies = cell.find('tbody').find_all('tr')
            # print(currencies)
            # print(len(currencies))
            for currency in currencies:
                currency_id = currency['data-market-nameslug']
                currency_name = currency.find('th').text.strip()
                currency_price = currency.find('td', {'class':'nf'}).text.strip()
                all_info = currency.find_all('td')
                min_price_today = all_info[2].text.strip()
                max_price_todoy = all_info[3].text.strip()
                price_date = all_info[4].text.strip()
                currency_info= {'name':currency_name,
                                'price': currency_price,
                                'date': price_date,
                                'min-price':min_price_today,
                                'max-price':max_price_todoy}
                info[currency_id] = currency_info
        return info


print(CurrencyPrice().currency_prices)
print(len(list(CurrencyPrice().currency_prices)))