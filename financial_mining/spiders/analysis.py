import scrapy
import json
from time import sleep
from ..items import FinancialMiningItem


class AnalysisSpider(scrapy.Spider):

    name = 'analysis'
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
        url = f"https://finance.yahoo.com/quote/AAPL/analysis?p=AAPL"
        yield scrapy.Request(url=url, callback=self.parse, cookies=self.cookies,
                             cb_kwargs=dict(symbol='AAPL'))

        # with open('stocks.json', 'r') as json_file:
        #     for i, stock in enumerate(json.load(json_file)):
        #         if i % 100 == 0 and i != 0:
        #             sleep(3)
        #         url = f"https://finance.yahoo.com/quote/{stock['symbol']}/analysis?p={stock['symbol']}"
        #         yield scrapy.Request(url=url, callback=self.parse, cookies=self.cookies,
        #                              cb_kwargs=dict(symbol=stock['symbol']))

    def parse(self, response, **kwargs):
        items = FinancialMiningItem()

        # 3.1 - Earnings Estimate
        items['earnings_low_est_curr_qtr'] = response.xpath(
            '//*[@id="Main"]//section/table[1]/tbody/tr[3]/td[2]').css(
            '::text').extract_first()
        items['earnings_low_est_next_qtr'] = response.xpath(
            '//*[@id="Main"]//section/table[1]/tbody/tr[3]/td[3]').css(
            '::text').extract_first()
        items['earnings_low_est_curr_yr'] = response.xpath(
            '//*[@id="Main"]//section/table[1]/tbody/tr[3]/td[4]').css(
            '::text').extract_first()
        items['earnings_low_est_next_yr'] = response.xpath(
            '//*[@id="Main"]//section/table[1]/tbody/tr[3]/td[5]').css(
            '::text').extract_first()
        items['earnings_high_est_curr_qtr'] = response.xpath(
            '//*[@id="Main"]//section/table[1]/tbody/tr[4]/td[2]').css(
            '::text').extract_first()
        items['earnings_high_est_next_qtr'] = response.xpath(
            '//*[@id="Main"]//section/table[1]/tbody/tr[4]/td[3]').css(
            '::text').extract_first()
        items['earnings_high_est_curr_yr'] = response.xpath(
            '//*[@id="Main"]//section/table[1]/tbody/tr[4]/td[4]').css(
            '::text').extract_first()
        items['earnings_high_est_next_yr'] = response.xpath(
            '//*[@id="Main"]//section/table[1]/tbody/tr[4]/td[5]').css(
            '::text').extract_first()
        # 3.2 - Revenue Estimate
        items['revenue_low_est_curr_qtr'] = response.xpath(
            '//*[@id="Main"]//section/table[2]/tbody/tr[3]/td[2]').css(
            '::text').extract_first()
        items['revenue_low_est_next_qtr'] = response.xpath(
            '//*[@id="Main"]//section/table[2]/tbody/tr[3]/td[3]').css(
            '::text').extract_first()
        items['revenue_low_est_curr_yr'] = response.xpath(
            '//*[@id="Main"]//section/table[2]/tbody/tr[3]/td[4]').css(
            '::text').extract_first()
        items['revenue_low_est_next_yr'] = response.xpath(
            '//*[@id="Main"]//section/table[2]/tbody/tr[3]/td[5]').css(
            '::text').extract_first()
        items['revenue_high_est_curr_qtr'] = response.xpath(
            '//*[@id="Main"]//section/table[2]/tbody/tr[4]/td[2]').css(
            '::text').extract_first()
        items['revenue_high_est_next_qtr'] = response.xpath(
            '//*[@id="Main"]//section/table[2]/tbody/tr[4]/td[3]').css(
            '::text').extract_first()
        items['revenue_high_est_curr_yr'] = response.xpath(
            '//*[@id="Main"]//section/table[2]/tbody/tr[4]/td[4]').css(
            '::text').extract_first()
        items['revenue_high_est_next_yr'] = response.xpath(
            '//*[@id="Main"]//section/table[2]/tbody/tr[4]/td[5]').css(
            '::text').extract_first()
        items['sales_gwth_est_curr_qtr'] = response.xpath(
            '//*[@id="Main"]//section/table[2]/tbody/tr[6]/td[2]').css(
            '::text').extract_first()
        items['sales_gwth_est_next_qtr'] = response.xpath(
            '//*[@id="Main"]//section/table[2]/tbody/tr[6]/td[3]').css(
            '::text').extract_first()
        items['sales_gwth_est_curr_yr'] = response.xpath(
            '//*[@id="Main"]//section/table[2]/tbody/tr[6]/td[4]').css(
            '::text').extract_first()
        items['sales_gwth_est_next_yr'] = response.xpath(
            '//*[@id="Main"]//section/table[2]/tbody/tr[6]/td[5]').css(
            '::text').extract_first()
        # 3.3 - EPS Trend
        items['eps_trend_curr_qtr'] = response.xpath(
            '//*[@id="Main"]//section/table[4]/tbody/tr[1]/td[2]').css(
            '::text').extract_first()
        items['eps_trend_next_qtr'] = response.xpath(
            '//*[@id="Main"]//section/table[4]/tbody/tr[1]/td[3]').css(
            '::text').extract_first()
        items['eps_trend_curr_yr'] = response.xpath(
            '//*[@id="Main"]//section/table[4]/tbody/tr[1]/td[4]').css(
            '::text').extract_first()
        items['eps_trend_next_yr'] = response.xpath(
            '//*[@id="Main"]//section/table[4]/tbody/tr[1]/td[5]').css(
            '::text').extract_first()
        items['eps_trend_30d_curr_qtr'] = response.xpath(
            '//*[@id="Main"]//section/table[4]/tbody/tr[3]/td[2]').css(
            '::text').extract_first()
        items['eps_trend_30d_next_qtr'] = response.xpath(
            '//*[@id="Main"]//section/table[4]/tbody/tr[3]/td[3]').css(
            '::text').extract_first()
        items['eps_trend_30d_curr_yr'] = response.xpath(
            '//*[@id="Main"]//section/table[4]/tbody/tr[3]/td[4]').css(
            '::text').extract_first()
        items['eps_trend_30d_next_yr'] = response.xpath(
            '//*[@id="Main"]//section/table[4]/tbody/tr[3]/td[5]').css(
            '::text').extract_first()
        items['eps_trend_60d_curr_qtr'] = response.xpath(
            '//*[@id="Main"]//section/table[4]/tbody/tr[4]/td[2]').css(
            '::text').extract_first()
        items['eps_trend_60d_next_qtr'] = response.xpath(
            '//*[@id="Main"]//section/table[4]/tbody/tr[4]/td[3]').css(
            '::text').extract_first()
        items['eps_trend_60d_curr_yr'] = response.xpath(
            '//*[@id="Main"]//section/table[4]/tbody/tr[4]/td[4]').css(
            '::text').extract_first()
        items['eps_trend_60d_next_yr'] = response.xpath(
            '//*[@id="Main"]//section/table[4]/tbody/tr[4]/td[5]').css(
            '::text').extract_first()
        items['eps_trend_90d_curr_qtr'] = response.xpath(
            '//*[@id="Main"]//section/table[4]/tbody/tr[5]/td[2]').css(
            '::text').extract_first()
        items['eps_trend_90d_next_qtr'] = response.xpath(
            '//*[@id="Main"]//section/table[4]/tbody/tr[5]/td[3]').css(
            '::text').extract_first()
        items['eps_trend_90d_curr_yr'] = response.xpath(
            '//*[@id="Main"]//section/table[4]/tbody/tr[5]/td[4]').css(
            '::text').extract_first()
        items['eps_trend_90d_next_yr'] = response.xpath(
            '//*[@id="Main"]//section/table[4]/tbody/tr[5]/td[5]').css(
            '::text').extract_first()
        # 3.4 - Growth Estimates
        items['gwth_est_curr_qtr'] = response.xpath(
            '//*[@id="Main"]//section/table[6]/tbody/tr[1]/td[2]').css(
            '::text').extract_first()
        items['gwth_est_next_qtr'] = response.xpath(
            '//*[@id="Main"]//section/table[6]/tbody/tr[2]/td[2]').css(
            '::text').extract_first()
        items['gwth_est_curr_yr'] = response.xpath(
            '//*[@id="Main"]//section/table[6]/tbody/tr[3]/td[2]').css(
            '::text').extract_first()
        items['gwth_est_next_yr'] = response.xpath(
            '//*[@id="Main"]//section/table[6]/tbody/tr[4]/td[2]').css(
            '::text').extract_first()

        self.results.append(items)

    def close(self, **kwargs):
        print(self.results)
