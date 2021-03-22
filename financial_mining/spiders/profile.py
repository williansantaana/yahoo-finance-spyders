import scrapy
import json
from time import sleep
from ..items import FinancialMiningItem


class ProfileSpider(scrapy.Spider):

    name = 'profile'
    allowed_domains = ['finance.yahoo.com']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.results = []
        self.cookies = [
            {'name': 'A1',
             'value': 'd=AQABBN5kYl8CEBFptOj2tIN8kSJmeGmSmMcFEgABAgHpVGAmYfCdb2UB9iMAAAcI3mRiX2mSmMc&'
                      'S=AQAAAq-iOfByftPFm-EUEKws53E'},
            {'name': 'B', 'value': '2hig711g57dc9&b=3&s=6p'}
        ]

    def start_requests(self):
        url = f"https://finance.yahoo.com/quote/AAPL/profile?p=AAPL"
        yield scrapy.Request(url=url, callback=self.parse, cookies=self.cookies,
                             cb_kwargs=dict(symbol='AAPL'))

        # with open('stocks.json', 'r') as json_file:
        #     for i, stock in enumerate(json.load(json_file)):
        #         if i % 100 == 0 and i != 0:
        #             sleep(3)
        #         url = f"https://finance.yahoo.com/quote/{stock['symbol']}/profile?p={stock['symbol']}"
        #         yield scrapy.Request(url=url, callback=self.parse, cookies=self.cookies,
        #                              cb_kwargs=dict(symbol=stock['symbol']))

    def parse(self, response, **kwargs):
        items = FinancialMiningItem()

        items['asset_sector'] = response.xpath(
            '//*[@id="Main"]//section/div/div/div/p[2]/span[2]').css(
            '::text').extract_first()
        items['asset_industry'] = response.xpath(
            '//*[@id="Main"]//section/div/div/div/p[2]/span[4]').css(
            '::text').extract_first()
        items['asset_description'] = response.xpath(
            '//*[@id="Main"]//section/section[2]/p').css(
            '::text').extract_first()

        self.results.append(items)

    def close(self, **kwargs):
        print(self.results)
