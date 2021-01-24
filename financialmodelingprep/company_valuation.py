BASE_URL = 'https://financialmodelingprep.com'

#Company Profile

@get_json_data
@staticmethod
def company_profile(ticker: str):
    '''
    Company profile
    '''
    return get_jsonparsed_data(f'{self.BASE_URL}/api/v3/profile/{ticker}')

#Company Quote

@get_json_data
@staticmethod
def company_quote(ticker: str):
    '''
    Company quote
    '''
    return f'{self.BASE_URL}/api/v3/quote/{ticker}'

#Key Executives
C['pay']
@get_json_data
@staticmethod
def key_executives(ticker: str):
    '''
    Key Executives
    '''
    return f'{self.BASE_URL}/api/v3/key-executives/{ticker}'

#Ticker Search

@get_json_data
@staticmethod
def search(query: str, limit: int, exchange: str):
    '''
    Search
    Values for exchange parameter are: ETF | MUTUAL_FUND | COMMODITY | INDEX | CRYPTO | FOREX | TSX | AMEX | NASDAQ | NYSE | EURONEXT
    '''
    return f'{self.BASE_URL}/api/v3/search?query={query}&limit={str(limit)}&exchange={exchange}'

#Ticker Search

@get_json_data
@staticmethod
def ticker_search(query: str, limit: int, exchange: str):
    '''
    Ticker Search
    Values for exchange parameter are: ETF | MUTUAL_FUND | COMMODITY | INDEX | CRYPTO | FOREX | TSX | AMEX | NASDAQ | NYSE | EURONEXT
    '''
    return f'{self.BASE_URL}/api/v3/search-ticker?query={query}&limit={str(limit)}&exchange={exchange}'

#Company Financial Statements
)
@get_json_data
@staticmethod
def annual_income_statement(ticker: str, limit: int):
    '''
    Annual Income Statement
    '''
    return f'{self.BASE_URL}/api/v3/income-statement/{ticker}?limit={str(limit)}'

@get_json_data
@staticmethod
def quarterly_income_statement(ticker: str, limit: int):
    '''
    Quarterly Income Statement
    '''
    return f'{self.BASE_URL}/api/v3/income-statement/{ticker}?period=quarter&limit={str(limit)}'

@get_json_data
@staticmethod
def annual_balance_sheet_statement(ticker: str, limit: int):
    '''
    Annual Balance Sheet statement
    '''
    return f'{self.BASE_URL}/api/v3/balance-sheet-statement/{ticker}?limit={str(limit)}'

@get_json_data
@staticmethod
def quarterly_balance_sheet_statement(ticker: str, limit: int):
    '''
    Quarterly Balance Sheet Statement
    '''
    return f'{self.BASE_URL}/api/v3/balance-sheet-statement/{ticker}?period=quarter&limit={str(limit)}'

@get_json_data
@staticmethod
def annual_cash_flow_statement(ticker: str, limit: int):
    '''
    Annual Cash Flow statement
    '''
    return f'{self.BASE_URL}/api/v3/cash-flow-statement/{ticker}?limit={str(limit)}'

@get_json_data
@staticmethod
def quarterly_cash_flow_statement(ticker: str, limit: int):
    '''
    Quarterly Cash Flow Statement
    '''
    return f'{self.BASE_URL}/api/v3/cash-flow-statement/{ticker}?period=quarter&limit={str(limit)}'

#Financial Statements Growth

@get_json_data
@staticmethod
def financial_statements_list():
    '''
    Financial Statements List
    '''
    return f'{self.BASE_URL}/api/v3/financial-statement-symbol-lists'

@get_json_data
@staticmethod
def annual_income_statement_growth(ticker: str, limit: int):
    '''
    Annual Income Statement Growth
    '''
    return f'{self.BASE_URL}/api/v3/income-statement-growth/{ticker}?limit={str(limit)}'

@get_json_data
@staticmethod
def annual_balance_sheet_statement_growth(ticker: str, limit: int):
    '''
    Annual Balance Sheet Statement Growth
    '''
    return f'{self.BASE_URL}/api/v3/balance-sheet-statement-growth/{ticker}?limit={str(limit)}'

@get_json_data
@staticmethod
def annual_cash_flow_statement_growth(ticker: str, limit: int):
    '''
    Annual Cash Flow Statement Growth
    '''
    return f'{self.BASE_URL}/api/v3/cash-flow-statement-growth/{ticker}?limit={str(limit)}'

# International Filings

@get_json_data
@staticmethod
def international_filings(ticker: str, limit: int):
    '''
    International Filings
    Values for international filings are: TO | PA | DE | NS | L | ME | HK | AX | OL | SW

    '''
    return f'{self.BASE_URL}/api/v3/income-state/RY.TO?limit=100{ticker}?limit={str(limit)}'

#Company Financial Statements As Reported

@get_json_data
@staticmethod
def annual_income_statements(ticker: str, limit: int):
    '''
    Annual Income Statements
    '''
    return f'{self.BASE_URL}/api/v3/income-statement-as-reported/{ticker}?limit={str(limit)}'

@get_json_data
@staticmethod
def quarterly_income_statements(ticker: str, limit: int):
    '''
    Quarterly Income Statements
    '''
    return f'{self.BASE_URL}/api/v3/income-statement-as-reported/{ticker}?period=quarter&limit={str(limit)}'

@get_json_data
@staticmethod
def annual_balance_sheet_statements(ticker: str, limit: int):
    '''
    Annual Balance Sheet Statements
    '''
    return f'{self.BASE_URL}/api/v3/balance-sheet-statement-as-reported/{ticker}?limit={str(limit)}'

@get_json_datas
@staticmethod
def quarterly_balance_sheet_statements(ticker: str, limit: int):
    '''
    Quarterly cash flow statements
    '''
    return f'{self.BASE_URL}/api/v3/balance-sheet-statement-as-reported/{ticker}?period=quarter&limit={str(limit)}'

@get_json_data
@staticmethod
def annual_cash_flow_statements(ticker: str, limit: int):
    '''
    Annual Cash Flow Statements
    '''
    return f'{self.BASE_URL}/api/v3/cash-flow-statement-as-reported/{ticker}?limit={str(limit)}'

@get_json_datas
@staticmethod
def quarterly_cash_flow_statements(ticker: str, limit: int):
    '''
    Quarterly cash flow statements
    '''
    return f'{self.BASE_URL}/api/v3/cash-flow-statement-as-reported/{ticker}?period=quarter&limit={str(limit)}'

@get_json_data
@staticmethod
def annual_full_financial_statement(ticker: str, limit: int):
    '''
    Annual Full Financial Statements
    '''
    return f'{self.BASE_URL}/api/v3/financial-statement-full-as-reported/{ticker}?limit={str(limit)}'

@get_json_datas
@staticmethod
def quarterly_full_financial_statements(ticker: str, limit: int):
    '''
    Quarterly Full Financial Statements
    '''
    return f'{self.BASE_URL}/api/v3/financial-statement-full-as-reported/{ticker}?period=quarter&limit={str(limit)}'

#Company Financial Ratios
@get_json_data
@staticmethod
def company_TTM_ratios(ticker: str, limit: int):
    '''
    Company TTM Ratios
    '''
    return f'{self.BASE_URL}/api/v3/ratios-ttm/{ticker}?limit={str(limit)}'

@get_json_data
@staticmethod
def company_financial_ratios(ticker: str, limit: int):
    '''
    Company Financial Ratios
    '''
    return f'{self.BASE_URL}/api/v3/ratios/{ticker}?limit={str(limit)}'

@get_json_data
@staticmethod
def company_quarterly_financial_ratios(ticker: str, limit: int):
    '''
    Company Quarterly Financial Ratios
    '''
    return f'{self.BASE_URL}/api/v3/ratios/{ticker}?period=quarter&limit={str(limit)}'

#Company Enterprise Value
@get_json_data
@staticmethod
def company_annual_enterprise_value(ticker: str, limit: int):
    '''
    Company Annual Enterprise Value
    '''
    return f'{self.BASE_URL}/api/v3/enterprise-values/{ticker}?limit={str(limit)}'

#Company Enterprise Value
@get_json_data
@staticmethod
def company_quarterly_enterprise_value(ticker: str, limit: int):
    '''
    Company Quarterly Enterprise Value
    '''
    return f'{self.BASE_URL}/api/v3/enterprise-values/{ticker}?period=quarter&limit={str(limit)}'

#Company Key Metrics
@get_json_data
@staticmethod
def company_TTM_key_metrics(ticker: str, limit: int):
    '''
    Company TTM Key Metrics
    '''
    return f'{self.BASE_URL}/api/v3/key-metrics-ttm/{ticker}?limit={str(limit)}'

@get_json_data
@staticmethod
def company_annual_key_metrics(ticker: str, limit: int):
    '''
    Company Annual Key Metrics
    '''
    return f'{self.BASE_URL}/api/v3/key-metrics-ttm/{ticker}?limit={str(limit)}'

@get_json_data
@staticmethod
def company_quarterly_company_key_metrics(ticker: str, limit: int):
    '''
    Company Annual Key Metrics
    '''
    return f'{self.BASE_URL}/api/v3/key-metrics/{ticker}?period=quarter&limit={str(limit)}'

#Company Financial Growth
@get_json_data
@staticmethod
def company_annual_financial_statement_growth(ticker: str, limit: int):
    '''
    Company Annual Financial Statement Growth
    '''
    return f'{self.BASE_URL}/api/v3/financial-growth/{ticker}?limit={str(limit)}'

@get_json_data
@staticmethod
def company_quarterly_financial_statement_growth(ticker: str, limit: int):
    '''
    Company Quarterly Financial Statement Growth
    '''
    return f'{self.BASE_URL}/api/v3/financial-growth/{ticker}?period=quarter&limit={str(limit)}'

#Company Rating
@get_json_data
@staticmethod
def companies_rating(ticker: str, limit: int):
    '''
    Companies Rating
    '''
    return f'{self.BASE_URL}/api/v3/rating/{ticker}'

@get_json_data
@staticmethod
def historical_companies_rating(ticker: str, limit: int):
    '''
    Historical Companies Rating
    '''
    return f'{self.BASE_URL}/api/v3/historical-rating/{ticker}?limit={str(limit)}'

#Company Discounted Cash Flow Value
@get_json_data
@staticmethod
def companies_discounted_cash_flow_value(ticker: str, limit: int):
    '''
    Companies Discounted Cash Flow Value (Intrinsic Value)
    '''
    return f'{self.BASE_URL}/api/v3/discounted-cash-flow/{ticker}?limit={str(limit)}'

@get_json_data
@staticmethod
def companies_historical_discounted_cash_flow_value(ticker: str, limit: int):
    '''
    Companies Historical Discounted Cash Flow Value (Intrinsic Value)
    '''
    return f'{self.BASE_URL}/api/v3/historical-discounted-cash-flow/{ticker}'

@get_json_data
@staticmethod
def companies_historical_discounted_cash_flow_value(ticker: str, limit: int):
    '''
    Companies Historical Discounted Cash Flow Value (Intrinsic Value)
    '''
    return f'{self.BASE_URL}/api/v3/historical-discounted-cash-flow/{ticker}?period=quarter'

@get_json_data
@staticmethod
def companies_historical_discounted_cash_flow_value(ticker: str, limit: int):
    '''
    Companies Daily Discounted Cash Flow Value (Intrinsic Value)
    '''
    return f'{self.BASE_URL}/api/v3/historical-daily-discounted-cash-flow/{ticker}?limit={str(limit)}'

#Market Capitalization
@get_json_data
@staticmethod
def market_capitalization(ticker: str, limit: int):
    '''
    Market Capitalization
    '''
    return f'{self.BASE_URL}/api/v3/market-capitalization/{ticker}'

@get_json_data
@staticmethod
def historical_market_capitalization(ticker: str, limit: int):
    '''
    Historical Market Capitalization
    '''
    return f'{self.BASE_URL}/api/v3/historical-market-capitalization/{ticker}?limit={str(limit)}'

#Symbols List
@get_json_data
@staticmethod
def all_ticker_symbols(ticker: str, limit: int):
    '''
    All Ticker Symbols
    '''
    return f'{self.BASE_URL}/api/v3/stock/list'

#Batch Request Stock Companies Price
@get_json_data
@staticmethod
def multiple_companies_prices(ticker_list):
    '''
    Multiple Companies Prices
    '''
    ticker_string = ''
    for ticker in ticker_list:
        ticker_string += ticker + ','
    return f'{self.BASE_URL}/api/v3/quote/{ticker_string}'

#Stock Screener
@get_json_data
@staticmethod
def stock_screener(marketCapMoreThan=None, marketCapLowerThan=None, priceMoreThan=None, priceLowerThan=None, betaMoreThan=None, betaLowerThan=None, volumeMoreThan=None, volumeLowerThan=None, dividendMoreThan=None, dividendLowerThan=None, limit:int,
    sector=None):
    '''
    Stock Screener
    Sectors: Consumer Cyclical | Energy | Technology | Industrials | Financial Services | Basic Materials | Communication Services | Consumer Defensive | Healthcare | Real Estate | Utilities | Industrial Goods | Conglomerates
    Industry: Autos | Banks | Banks Diversified | Software | Banks Regional | Beverages Alcoholic | Beverages Brewers | Beverages Non-Alcoholic
    Exchange: nyse | nasdaq | amex | euronex | tsx | etf | mutual_fund 
    '''
    query_string='?'
    if marketCapMoreThan:
        query_string += f'marketCapMoreThan={marketCapMoreThan}&'
    if marketCapLowerThan:
        query_string += f'marketCapLowerThan={marketCapLowerThan}&'
    if priceMoreThan:
        query_string += f'priceMoreThan={priceMoreThan}&'
    if priceLowerThan:
        query_string += f'priceLowerThan={priceLowerThan}&'
    if betaMoreThan:
        query_string += f'betaMoreThan={betaMoreThan}&'
    if betaLowerThan:
        query_string += f'betaLowerThan={betaLowerThan}&'
    if volumeMoreThan:
        query_string += f'volumeMoreThan={volumeMoreThan}&'
    if volumeLowerThan:
        query_string += f'volumeLowerThan={volumeLowerThan}&'
    if dividendMoreThan:
        query_string += f'dividendMoreThan={dividendMoreThan}&'
    if dividendLowerThan:
        query_string += f'dividendLowerThan={dividendLowerThan}&'
    return f'{self.BASE_URL}/api/v3/stock/list{query_string}'



    