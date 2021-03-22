import scrapy
import json
from time import sleep
from ..items import FinancialMiningItem


class SummarySpider(scrapy.Spider):

    name = 'summary'
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
        url = f"https://finance.yahoo.com/quote/AAPL?p=AAPL"
        yield scrapy.Request(url=url, callback=self.parse, cookies=self.cookies,
                             cb_kwargs=dict(symbol='AAPL'))

        # with open('stocks.json', 'r') as json_file:
        #     for i, stock in enumerate(json.load(json_file)):
        #         if i % 100 == 0:
        #             sleep(3)
        #         url = f"https://finance.yahoo.com/quote/{stock['symbol']}?p={stock['symbol']}"
        #         yield scrapy.Request(url=url, callback=self.parse, cookies=cookies,
        #                              cb_kwargs=dict(symbol=stock['symbol']))

    def parse(self, response, **kwargs):
        items = FinancialMiningItem()

        items['intra_day_price'] = response.xpath(
            '//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]').css(
            '::text').extract_first()
        items['price_change'] = response.xpath(
            '//*[@id="quote-header-info"]/div[3]/div[1]/div/span[2]').css(
            '::text').extract_first()
        items['current_timestamp'] = response.xpath(
            '//*[@id="quote-market-notice"]/ span').css(
            '::text').extract_first()
        items['pre_price'] = response.xpath(
            '//*[@id="quote-header-info"]/div[3]/div[1]/p/span[1]').css(
            '::text').extract_first()
        items['pre_change'] = response.xpath(
            '//*[@id="quote-header-info"]/div[3]/div[1]/p/span[2]').css(
            '::text').extract_first()
        items['pre_timestamp'] = response.xpath(
            '//*[@id="quote-header-info"]/div[3]/div[1]/p/span[3]').css(
            '::text').extract()
        items['prev_close'] = response.xpath(
            '//*[@id="quote-summary"]/div[1]/table/tbody/tr[1]/td[2]').css(
            '::text').extract_first()
        items['open'] = response.xpath(
            '//*[@id="quote-summary"]/div[1]/table/tbody/tr[2]/td[2]').css(
            '::text').extract_first()
        items['bid'] = response.xpath(
            '//*[@id="quote-summary"]/div[1]/table/tbody/tr[3]/td[2]/span').css(
            '::text').extract_first()
        items['ask'] = response.xpath(
            '//*[@id="quote-summary"]/div[1]/table/tbody/tr[4]/td[2]/span').css(
            '::text').extract_first()
        items['range_day'] = response.xpath(
            '//*[@id="quote-summary"]/div[1]/table/tbody/tr[5]/td[2]').css(
            '::text').extract_first()
        items['range_52weeks'] = response.xpath(
            '//*[@id="quote-summary"]/div[1]/table/tbody/tr[6]/td[2]').css(
            '::text').extract_first()
        items['volume'] = response.xpath(
            '//*[@id="quote-summary"]/div[1]/table/tbody/tr[7]/td[2]/span').css(
            '::text').extract_first()
        items['volume_avg'] = response.xpath(
            '//*[@id="quote-summary"]/div[1]/table/tbody/tr[8]/td[2]/span').css(
            '::text').extract_first()
        items['market_cap'] = response.xpath(
            '//*[@id="quote-summary"]/div[2]/table/tbody/tr[1]/td[2]/span').css(
            '::text').extract_first()
        items['pe_ratio'] = response.xpath(
            '//*[@id="quote-summary"]/div[2]/table/tbody/tr[3]/td[2]/span').css(
            '::text').extract_first()
        items['eps'] = response.xpath(
            '//*[@id="quote-summary"]/div[2]/table/tbody/tr[4]/td[2]/span').css(
            '::text').extract_first()
        items['earnings_date'] = response.xpath(
            '//*[@id="quote-summary"]/div[2]/table/tbody/tr[5]/td[2]/span[1]').css(
            '::text').extract_first()
        items['est_yr_target'] = response.xpath(
            '//*[@id="quote-summary"]/div[2]/table/tbody/tr[8]/td[2]/span').css(
            '::text').extract_first()

        self.results.append(items)

    def close(self, **kwargs):
        print(self.results)
