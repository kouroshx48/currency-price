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
        self.__driver = driver

    def get_soup(self):
        soup = BeautifulSoup(self.__driver.page_source, 'html.parser')
        return soup

    @property
    def currency_prices(self):
        self.__driver.get('https://www.tgju.org/currency')
        soup = self.get_soup()
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
    
    @property
    def gold_prices(self):
        self.__driver.get('https://www.tgju.org/gold-chart')
        soup = self.get_soup()
        cells_all = soup.find('div', {'class':'fs-row'}).find_all('div', {'class':'fs-cell'})
        # print(len(cells))
        cells = [cells_all[2], cells_all[3]]
        info = {}
        for cell in cells:
            tables = cell.find_all('table', {'class':'data-table'})
            for table in tables:
                pieces = table.find('tbody').find_all('tr')
                for piece in pieces:
                    piece_id = piece['data-market-nameslug']
                    piece_name = piece.th.text.strip()
                    piece_price = piece.find('td', {'class':'nf'}).text.strip()
                    price_info = piece.find_all('td')
                    lowest_price = price_info[2].text.strip()
                    highest_price = price_info[3].text.strip()
                    time = price_info[4]

                    piece_info_dic = {'name':piece_name,
                                      'price': piece_price,
                                      'min-price': lowest_price,
                                      'max-price': highest_price,
                                      'price-time': time}
                    info[piece_id] = piece_info_dic
        return info 
    
    @property
    def coin_prices(self):
        self.__driver.get('https://www.tgju.org/coin')
        soup = self.get_soup()
        cells= soup.find('div', {'class':'fs-row'}).find_all('div', {'class':'fs-cell'})
        del cells[1]
        info = {}
        for cell in cells:
            coins = cell.table.tbody.find_all('tr')
            for coin in coins:
                coin_id = coin['data-market-nameslug']
                coin_name = coin.th.text.strip()
                coin_info = coin.find_all('td')
                coin_price = coin_info[0].text.strip()
                lowest_price = coin_info[2].text.strip()
                highest_price = coin_info[3].text.strip()
                time = coin_info[4].text.strip()
                coin_info_dict = {'name':coin_name,
                                  'price':coin_price,
                                  'min-price':lowest_price,
                                  'max-price':highest_price,
                                  'time':time}
                info[coin_id] = coin_info_dict
        return info

print(CurrencyPrice().coin_prices)  
        