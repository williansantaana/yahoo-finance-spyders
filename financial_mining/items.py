# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FinancialMiningItem(scrapy.Item):
    # define the fields for your item here like:

    # 1.0 - Summary
    intra_day_price = scrapy.Field()
    price_change = scrapy.Field()
    current_timestamp = scrapy.Field()
    pre_price = scrapy.Field()
    pre_change = scrapy.Field()
    pre_timestamp = scrapy.Field()
    prev_close = scrapy.Field()
    open = scrapy.Field()
    bid = scrapy.Field()
    ask = scrapy.Field()
    range_day = scrapy.Field()
    range_52weeks = scrapy.Field()
    volume = scrapy.Field()
    volume_avg = scrapy.Field()
    market_cap = scrapy.Field()
    pe_ratio = scrapy.Field()
    eps = scrapy.Field()
    earnings_date = scrapy.Field()
    est_yr_target = scrapy.Field()

    # 2.0 - Statistics
    # 2.1 - Valuation Measures
    ent_value = scrapy.Field()
    trailing_pe = scrapy.Field()
    fwd_pe = scrapy.Field()
    peg_ratio = scrapy.Field()
    price_sales_ttm = scrapy.Field()
    price_book_mrq = scrapy.Field()
    ent_value_revenue = scrapy.Field()
    ent_value_ebitda = scrapy.Field()
    # 2.2 - Fiscal Year
    fiscal_yr_ends = scrapy.Field()
    most_recent_qtr = scrapy.Field()
    # 1.3 - Profitability
    profit_margin = scrapy.Field()
    operating_margin_ttm = scrapy.Field()
    # 2.4 - Management Effectiveness
    return_on_assets_ttm = scrapy.Field()
    return_equity_ttm = scrapy.Field()
    # 2.5 - Income Statement
    revenue_ttm = scrapy.Field()
    revenue_per_share_ttm = scrapy.Field()
    qtr_revenue_gwth_yoy = scrapy.Field()
    gross_profit_ttm = scrapy.Field()
    ebitda = scrapy.Field()
    diluted_eps_ttm = scrapy.Field()
    qtr_earnings_gwth = scrapy.Field()
    # 2.6 = Balance Sheet
    total_cash_mrq = scrapy.Field()
    total_cash_per_share_mrq = scrapy.Field()
    total_debt_mrq = scrapy.Field()
    total_debt_equity_mrq = scrapy.Field()
    current_ratio_mrq = scrapy.Field()
    book_value_per_share_mrq = scrapy.Field()
    # 2.7 Cash Flow Statement
    operating_cash_flow_ttm = scrapy.Field()
    levered_free_cash_flow_ttm = scrapy.Field()
    # 2.8 Stock Price History
    beta_5yr_monthly = scrapy.Field()
    change_52week = scrapy.Field()
    sp500_52week_change = scrapy.Field()
    high_52week = scrapy.Field()
    low_52week = scrapy.Field()
    moving_average_50day = scrapy.Field()
    moving_average_200day = scrapy.Field()
    # 2.9 - Share Statistics
    avg_volume_3month = scrapy.Field()
    avg_volume_10day = scrapy.Field()
    shares_outstanding = scrapy.Field()
    float = scrapy.Field()
    held_by_insiders = scrapy.Field()
    held_by_institutions = scrapy.Field()
    # 2.10 - Dividends & Splits
    fwd_div_rate = scrapy.Field()
    fwd_div_yield = scrapy.Field()
    trailing_div_rate = scrapy.Field()
    trailing_div_yield = scrapy.Field()
    avg_div_yield_5yr = scrapy.Field()
    payout_ratio = scrapy.Field()
    div_date = scrapy.Field()
    exp_div_date = scrapy.Field()

    # 3.0 - Analysis
    # 3.1 - Earnings Estimate
    earnings_low_est_curr_qtr = scrapy.Field()
    earnings_low_est_next_qtr = scrapy.Field()
    earnings_low_est_curr_yr = scrapy.Field()
    earnings_low_est_next_yr = scrapy.Field()
    earnings_high_est_curr_qtr = scrapy.Field()
    earnings_high_est_next_qtr = scrapy.Field()
    earnings_high_est_curr_yr = scrapy.Field()
    earnings_high_est_next_yr = scrapy.Field()
    # 3.2 - Revenue Estimate
    revenue_low_est_curr_qtr = scrapy.Field()
    revenue_low_est_next_qtr = scrapy.Field()
    revenue_low_est_curr_yr = scrapy.Field()
    revenue_low_est_next_yr = scrapy.Field()
    revenue_high_est_curr_qtr = scrapy.Field()
    revenue_high_est_next_qtr = scrapy.Field()
    revenue_high_est_curr_yr = scrapy.Field()
    revenue_high_est_next_yr = scrapy.Field()
    sales_gwth_est_curr_qtr = scrapy.Field()
    sales_gwth_est_next_qtr = scrapy.Field()
    sales_gwth_est_curr_yr = scrapy.Field()
    sales_gwth_est_next_yr = scrapy.Field()
    # 3.3 - EPS Trend
    eps_trend_curr_qtr = scrapy.Field()
    eps_trend_next_qtr = scrapy.Field()
    eps_trend_curr_yr = scrapy.Field()
    eps_trend_next_yr = scrapy.Field()
    eps_trend_30d_curr_qtr = scrapy.Field()
    eps_trend_30d_next_qtr = scrapy.Field()
    eps_trend_30d_curr_yr = scrapy.Field()
    eps_trend_30d_next_yr = scrapy.Field()
    eps_trend_60d_curr_qtr = scrapy.Field()
    eps_trend_60d_next_qtr = scrapy.Field()
    eps_trend_60d_curr_yr = scrapy.Field()
    eps_trend_60d_next_yr = scrapy.Field()
    eps_trend_90d_curr_qtr = scrapy.Field()
    eps_trend_90d_next_qtr = scrapy.Field()
    eps_trend_90d_curr_yr = scrapy.Field()
    eps_trend_90d_next_yr = scrapy.Field()
    # 3.4 - Growth Estimates
    gwth_est_curr_qtr = scrapy.Field()
    gwth_est_next_qtr = scrapy.Field()
    gwth_est_curr_yr = scrapy.Field()
    gwth_est_next_yr = scrapy.Field()

    # 4.0 - Profile
    asset_sector = scrapy.Field()
    asset_industry = scrapy.Field()
    asset_description = scrapy.Field()
