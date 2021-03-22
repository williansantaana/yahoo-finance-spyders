import scrapy
import json
from time import sleep
from ..items import FinancialMiningItem


class StatisticsSpider(scrapy.Spider):

    name = 'statistics'
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
        url = f"https://finance.yahoo.com/quote/AAPL/key-statistics?p=AAPL"
        yield scrapy.Request(url=url, callback=self.parse, cookies=self.cookies,
                             cb_kwargs=dict(symbol='AAPL'))

        # with open('stocks.json', 'r') as json_file:
        #     for i, stock in enumerate(json.load(json_file)):
        #         if i % 100 == 0 and i != 0:
        #             sleep(3)
        #         url = f"https://finance.yahoo.com/quote/{stock['symbol']}/key-statistics?p={stock['symbol']}"
        #         yield scrapy.Request(url=url, callback=self.parse, cookies=self.cookies,
        #                              cb_kwargs=dict(symbol=stock['symbol']))

    def parse(self, response, **kwargs):
        items = FinancialMiningItem()

        # 2.1 - Valuation Measures
        items['ent_value'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[1]/div/div[1]//table/tbody/tr[2]/td[2]').css(
            '::text').extract_first()
        items['trailing_pe'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[1]/div/div[1]//table/tbody/tr[3]/td[2]').css(
            '::text').extract_first()
        items['fwd_pe'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[1]/div/div[1]//table/tbody/tr[4]/td[2]').css(
            '::text').extract_first()
        items['peg_ratio'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[1]/div/div[1]//table/tbody/tr[5]/td[2]').css(
            '::text').extract_first()
        items['price_sales_ttm'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[1]/div/div[1]//table/tbody/tr[6]/td[2]').css(
            '::text').extract_first()
        items['price_book_mrq'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[1]/div/div[1]//table/tbody/tr[7]/td[2]').css(
            '::text').extract_first()
        items['ent_value_revenue'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[1]/div/div[1]//table/tbody/tr[8]/td[2]').css(
            '::text').extract_first()
        items['ent_value_ebitda'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[1]/div/div[1]//table/tbody/tr[9]/td[2]').css(
            '::text').extract_first()
        # 2.2 - Fiscal Year
        items['fiscal_yr_ends'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[3]/div/div[1]//table/tbody/tr[1]/td[2]').css(
            '::text').extract_first()
        items['most_recent_qtr'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[3]/div/div[1]//table/tbody/tr[2]/td[2]').css(
            '::text').extract_first()
        # 1.3 - Profitability
        items['profit_margin'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[3]/div/div[2]//table/tbody/tr[1]/td[2]').css(
            '::text').extract_first()
        items['operating_margin_ttm'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[3]/div/div[2]//table/tbody/tr[2]/td[2]').css(
            '::text').extract_first()
        # 2.4 - Management Effectiveness
        items['return_on_assets_ttm'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[3]/div/div[3]//table/tbody/tr[1]/td[2]').css(
            '::text').extract_first()
        items['return_equity_ttm'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[3]/div/div[3]//table/tbody/tr[2]/td[2]').css(
            '::text').extract_first()
        # 2.5 - Income Statement
        items['revenue_ttm'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[3]/div/div[4]//table/tbody/tr[1]/td[2]').css(
            '::text').extract_first()
        items['revenue_per_share_ttm'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[3]/div/div[4]//table/tbody/tr[2]/td[2]').css(
            '::text').extract_first()
        items['qtr_revenue_gwth_yoy'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[3]/div/div[4]//table/tbody/tr[3]/td[2]').css(
            '::text').extract_first()
        items['gross_profit_ttm'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[3]/div/div[4]//table/tbody/tr[4]/td[2]').css(
            '::text').extract_first()
        items['ebitda'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[3]/div/div[4]//table/tbody/tr[5]/td[2]').css(
            '::text').extract_first()
        items['diluted_eps_ttm'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[3]/div/div[4]//table/tbody/tr[7]/td[2]').css(
            '::text').extract_first()
        items['qtr_earnings_gwth'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[3]/div/div[4]//table/tbody/tr[8]/td[2]').css(
            '::text').extract_first()
        # 2.6 = Balance Sheet
        items['total_cash_mrq'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[3]/div/div[5]//table/tbody/tr[1]/td[2]').css(
            '::text').extract_first()
        items['total_cash_per_share_mrq'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[3]/div/div[5]//table/tbody/tr[2]/td[2]').css(
            '::text').extract_first()
        items['total_debt_mrq'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[3]/div/div[5]//table/tbody/tr[3]/td[2]').css(
            '::text').extract_first()
        items['total_debt_equity_mrq'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[3]/div/div[5]//table/tbody/tr[4]/td[2]').css(
            '::text').extract_first()
        items['current_ratio_mrq'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[3]/div/div[5]//table/tbody/tr[5]/td[2]').css(
            '::text').extract_first()
        items['book_value_per_share_mrq'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[3]/div/div[5]//table/tbody/tr[6]/td[2]').css(
            '::text').extract_first()
        # 2.7 Cash Flow Statement
        items['operating_cash_flow_ttm'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[3]/div/div[6]//table/tbody/tr[1]/td[2]').css(
            '::text').extract_first()
        items['levered_free_cash_flow_ttm'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[3]/div/div[6]//table/tbody/tr[2]/td[2]').css(
            '::text').extract_first()
        # 2.8 Stock Price History
        items['beta_5yr_monthly'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[2]/div/div[1]//table/tbody/tr[1]/td[2]').css(
            '::text').extract_first()
        items['change_52week'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[2]/div/div[1]//table/tbody/tr[2]/td[2]').css(
            '::text').extract_first()
        items['sp500_52week_change'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[2]/div/div[1]//table/tbody/tr[3]/td[2]').css(
            '::text').extract_first()
        items['high_52week'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[2]/div/div[1]//table/tbody/tr[4]/td[2]').css(
            '::text').extract_first()
        items['low_52week'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[2]/div/div[1]//table/tbody/tr[5]/td[2]').css(
            '::text').extract_first()
        items['moving_average_50day'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[2]/div/div[1]//table/tbody/tr[6]/td[2]').css(
            '::text').extract_first()
        items['moving_average_200day'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[2]/div/div[1]//table/tbody/tr[7]/td[2]').css(
            '::text').extract_first()
        # 2.9 - Share Statistics
        items['avg_volume_3month'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[2]/div/div[2]//table/tbody/tr[1]/td[2]').css(
            '::text').extract_first()
        items['avg_volume_10day'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[2]/div/div[2]//table/tbody/tr[2]/td[2]').css(
            '::text').extract_first()
        items['shares_outstanding'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[2]/div/div[2]//table/tbody/tr[3]/td[2]').css(
            '::text').extract_first()
        items['float'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[2]/div/div[2]//table/tbody/tr[4]/td[2]').css(
            '::text').extract_first()
        items['held_by_insiders'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[2]/div/div[2]//table/tbody/tr[5]/td[2]').css(
            '::text').extract_first()
        items['held_by_institutions'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[2]/div/div[2]//table/tbody/tr[6]/td[2]').css(
            '::text').extract_first()
        # 2.10 - Dividends & Splits
        items['fwd_div_rate'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[2]/div/div[3]//table/tbody/tr[1]/td[2]').css(
            '::text').extract_first()
        items['fwd_div_yield'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[2]/div/div[3]//table/tbody/tr[2]/td[2]').css(
            '::text').extract_first()
        items['trailing_div_rate'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[2]/div/div[3]//table/tbody/tr[3]/td[2]').css(
            '::text').extract_first()
        items['trailing_div_yield'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[2]/div/div[3]//table/tbody/tr[4]/td[2]').css(
            '::text').extract_first()
        items['avg_div_yield_5yr'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[2]/div/div[3]//table/tbody/tr[5]/td[2]').css(
            '::text').extract_first()
        items['payout_ratio'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[2]/div/div[3]//table/tbody/tr[6]/td[2]').css(
            '::text').extract_first()
        items['div_date'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[2]/div/div[3]//table/tbody/tr[7]/td[2]').css(
            '::text').extract_first()
        items['exp_div_date'] = response.xpath(
            '//*[@id="Main"]//section/div[2]/div[2]/div/div[3]//table/tbody/tr[8]/td[2]').css(
            '::text').extract_first()

        self.results.append(items)

    def close(self, **kwargs):
        print(self.results)
