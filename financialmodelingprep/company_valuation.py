from financialmodelingprep.decorator import get_json_data

BASE_URL = 'https://financialmodelingprep.com'

class company_valuation():

    BASE_URL = 'https://financialmodelingprep.com'  
    API_KEY = ''
    
    def __init__(self, API_KEY):
        self.API = API_KEY

    #Company Profile

    @get_json_data(API_KEY)
    def company_profile(self, ticker: str):
        '''
        Company profile
        '''
        return f'{self.BASE_URL}/api/v3/profile/{ticker}?apikey={self.API}'

    #Company Quote

    @get_json_data(API_KEY)
    def company_quote(self, ticker: str):
        '''
        Company quote
        '''
        return f'{self.BASE_URL}/api/v3/quote/{ticker}?apikey={self.API}'

    #Key Executives
    @get_json_data(API_KEY)
    def key_executives(self, ticker: str):
        '''
        Key Executives
        '''
        return f'{self.BASE_URL}/api/v3/key-executives/{ticker}?apikey={self.API}'

    #Ticker Search

    @get_json_data(API_KEY)
    def search(self, query: str, limit: int, exchange: str):
        '''
        Search
        Values for exchange parameter are: ETF | MUTUAL_FUND | COMMODITY | INDEX | CRYPTO | FOREX | TSX | AMEX | NASDAQ | NYSE | EURONEXT
        '''
        return f'{self.BASE_URL}/api/v3/search?query={query}&limit={str(limit)}&exchange={exchange}?apikey={self.API}'

    #Ticker Search

    @get_json_data(API_KEY)
    def ticker_search(self, query: str, limit: int, exchange: str):
        '''
        Ticker Search
        Values for exchange parameter are: ETF | MUTUAL_FUND | COMMODITY | INDEX | CRYPTO | FOREX | TSX | AMEX | NASDAQ | NYSE | EURONEXT
        '''
        return f'{self.BASE_URL}/api/v3/search-ticker?query={query}&limit={str(limit)}&exchange={exchange}?apikey={self.API}'

    #Company Financial Statements
    
    @get_json_data(API_KEY)
    def annual_income_statement(self, ticker: str, limit: int):
        '''
        Annual Income Statement
        '''
        return f'{self.BASE_URL}/api/v3/income-statement/{ticker}?limit={str(limit)}?apikey={self.API}'

    @get_json_data(API_KEY)
    def quarterly_income_statement(self, ticker: str, limit: int):
        '''
        Quarterly Income Statement
        '''
        return f'{self.BASE_URL}/api/v3/income-statement/{ticker}?period=quarter&limit={str(limit)}?apikey={self.API}'

    @get_json_data(API_KEY)
    def annual_balance_sheet_statement(self, ticker: str, limit: int):
        '''
        Annual Balance Sheet statement
        '''
        return f'{self.BASE_URL}/api/v3/balance-sheet-statement/{ticker}?limit={str(limit)}?apikey={self.API}'

    @get_json_data(API_KEY)
    def quarterly_balance_sheet_statement(self, ticker: str, limit: int):
        '''
        Quarterly Balance Sheet Statement
        '''
        return f'{self.BASE_URL}/api/v3/balance-sheet-statement/{ticker}?period=quarter&limit={str(limit)}?apikey={self.API}'

    @get_json_data(API_KEY)
    def annual_cash_flow_statement(self, ticker: str, limit: int):
        '''
        Annual Cash Flow statement
        '''
        return f'{self.BASE_URL}/api/v3/cash-flow-statement/{ticker}?limit={str(limit)}?apikey={self.API}'

    @get_json_data(API_KEY)
    def quarterly_cash_flow_statement(self, ticker: str, limit: int):
        '''
        Quarterly Cash Flow Statement
        '''
        return f'{self.BASE_URL}/api/v3/cash-flow-statement/{ticker}?period=quarter&limit={str(limit)}?apikey={self.API}'

    #Financial Statements Growth

    @get_json_data(API_KEY)
    def financial_statements_list(self):
        '''
        Financial Statements List
        '''
        return f'{self.BASE_URL}/api/v3/financial-statement-symbol-lists?apikey={self.API}'

    @get_json_data(API_KEY)
    def annual_income_statement_growth(self, ticker: str, limit: int):
        '''
        Annual Income Statement Growth
        '''
        return f'{self.BASE_URL}/api/v3/income-statement-growth/{ticker}?limit={str(limit)}?apikey={self.API}'

    @get_json_data(API_KEY)
    def annual_balance_sheet_statement_growth(self, ticker: str, limit: int):
        '''
        Annual Balance Sheet Statement Growth
        '''
        return f'{self.BASE_URL}/api/v3/balance-sheet-statement-growth/{ticker}?limit={str(limit)}?apikey={self.API}'

    @get_json_data(API_KEY)
    def annual_cash_flow_statement_growth(self, ticker: str, limit: int):
        '''
        Annual Cash Flow Statement Growth
        '''
        return f'{self.BASE_URL}/api/v3/cash-flow-statement-growth/{ticker}?limit={str(limit)}?apikey={self.API}'

    # International Filings

    @get_json_data(API_KEY)
    def international_filings(self, ticker: str, limit: int):
        '''
        International Filings
        Values for international filings are: TO | PA | DE | NS | L | ME | HK | AX | OL | SW

        '''
        return f'{self.BASE_URL}/api/v3/income-state/RY.TO?limit=100{ticker}?limit={str(limit)}?apikey={self.API}'

    #Company Financial Statements As Reported

    @get_json_data(API_KEY)
    def annual_income_statements(self, ticker: str, limit: int):
        '''
        Annual Income Statements
        '''
        return f'{self.BASE_URL}/api/v3/income-statement-as-reported/{ticker}?limit={str(limit)}?apikey={self.API}'

    @get_json_data(API_KEY)
    def quarterly_income_statements(self, ticker: str, limit: int):
        '''
        Quarterly Income Statements
        '''
        return f'{self.BASE_URL}/api/v3/income-statement-as-reported/{ticker}?period=quarter&limit={str(limit)}?apikey={self.API}'

    @get_json_data(API_KEY)
    def annual_balance_sheet_statements(self, ticker: str, limit: int):
        '''
        Annual Balance Sheet Statements
        '''
        return f'{self.BASE_URL}/api/v3/balance-sheet-statement-as-reported/{ticker}?limit={str(limit)}?apikey={self.API}'

    @get_json_data(API_KEY)
    def quarterly_balance_sheet_statements(self, ticker: str, limit: int):
        '''
        Quarterly cash flow statements
        '''
        return f'{self.BASE_URL}/api/v3/balance-sheet-statement-as-reported/{ticker}?period=quarter&limit={str(limit)}?apikey={self.API}'

    @get_json_data(API_KEY)
    def annual_cash_flow_statements(self, ticker: str, limit: int):
        '''
        Annual Cash Flow Statements
        '''
        return f'{self.BASE_URL}/api/v3/cash-flow-statement-as-reported/{ticker}?limit={str(limit)}?apikey={self.API}'

    @get_json_data(API_KEY)
    def quarterly_cash_flow_statements(self, ticker: str, limit: int):
        '''
        Quarterly cash flow statements
        '''
        return f'{self.BASE_URL}/api/v3/cash-flow-statement-as-reported/{ticker}?period=quarter&limit={str(limit)}?apikey={self.API}'

    @get_json_data(API_KEY)
    def annual_full_financial_statement(self, ticker: str, limit: int):
        '''
        Annual Full Financial Statements
        '''
        return f'{self.BASE_URL}/api/v3/financial-statement-full-as-reported/{ticker}?limit={str(limit)}?apikey={self.API}'

    @get_json_data(API_KEY)
    def quarterly_full_financial_statements(self, ticker: str, limit: int):
        '''
        Quarterly Full Financial Statements
        '''
        return f'{self.BASE_URL}/api/v3/financial-statement-full-as-reported/{ticker}?period=quarter&limit={str(limit)}?apikey={self.API}'

    #Company Financial Ratios
    @get_json_data(API_KEY)
    def company_TTM_ratios(self, ticker: str, limit: int):
        '''
        Company TTM Ratios
        '''
        return f'{self.BASE_URL}/api/v3/ratios-ttm/{ticker}?limit={str(limit)}?apikey={self.API}'

    @get_json_data(API_KEY)
    def company_financial_ratios(self, ticker: str, limit: int):
        '''
        Company Financial Ratios
        '''
        return f'{self.BASE_URL}/api/v3/ratios/{ticker}?limit={str(limit)}?apikey={self.API}'

    @get_json_data(API_KEY)
    def company_quarterly_financial_ratios(self, ticker: str, limit: int):
        '''
        Company Quarterly Financial Ratios
        '''
        return f'{self.BASE_URL}/api/v3/ratios/{ticker}?period=quarter&limit={str(limit)}?apikey={self.API}'

    #Company Enterprise Value
    @get_json_data(API_KEY)
    def company_annual_enterprise_value(self, ticker: str, limit: int):
        '''
        Company Annual Enterprise Value
        '''
        return f'{self.BASE_URL}/api/v3/enterprise-values/{ticker}?limit={str(limit)}?apikey={self.API}'

    #Company Enterprise Value
    @get_json_data(API_KEY)
    def company_quarterly_enterprise_value(self, ticker: str, limit: int):
        '''
        Company Quarterly Enterprise Value
        '''
        return f'{self.BASE_URL}/api/v3/enterprise-values/{ticker}?period=quarter&limit={str(limit)}?apikey={self.API}'

    #Company Key Metrics
    @get_json_data(API_KEY)
    def company_TTM_key_metrics(self, ticker: str, limit: int):
        '''
        Company TTM Key Metrics
        '''
        return f'{self.BASE_URL}/api/v3/key-metrics-ttm/{ticker}?limit={str(limit)}?apikey={self.API}'

    @get_json_data(API_KEY)
    def company_annual_key_metrics(self, ticker: str, limit: int):
        '''
        Company Annual Key Metrics
        '''
        return f'{self.BASE_URL}/api/v3/key-metrics-ttm/{ticker}?limit={str(limit)}?apikey={self.API}'

    @get_json_data(API_KEY)
    def company_quarterly_company_key_metrics(self, ticker: str, limit: int):
        '''
        Company Annual Key Metrics
        '''
        return f'{self.BASE_URL}/api/v3/key-metrics/{ticker}?period=quarter&limit={str(limit)}?apikey={self.API}'

    #Company Financial Growth
    @get_json_data(API_KEY)
    def company_annual_financial_statement_growth(self, ticker: str, limit: int):
        '''
        Company Annual Financial Statement Growth
        '''
        return f'{self.BASE_URL}/api/v3/financial-growth/{ticker}?limit={str(limit)}?apikey={self.API}'

    @get_json_data(API_KEY)
    def company_quarterly_financial_statement_growth(self, ticker: str, limit: int):
        '''
        Company Quarterly Financial Statement Growth
        '''
        return f'{self.BASE_URL}/api/v3/financial-growth/{ticker}?period=quarter&limit={str(limit)}?apikey={self.API}'

    #Company Rating
    @get_json_data(API_KEY)
    def companies_rating(self, ticker: str, limit: int):
        '''
        Companies Rating
        '''
        return f'{self.BASE_URL}/api/v3/rating/{ticker}?apikey={self.API}'

    @get_json_data(API_KEY)
    def historical_companies_rating(self, ticker: str, limit: int):
        '''
        Historical Companies Rating
        '''
        return f'{self.BASE_URL}/api/v3/historical-rating/{ticker}?limit={str(limit)}?apikey={self.API}'

    #Company Discounted Cash Flow Value
    @get_json_data(API_KEY)
    def companies_discounted_cash_flow_value(self, ticker: str, limit: int):
        '''
        Companies Discounted Cash Flow Value (Intrinsic Value)
        '''
        return f'{self.BASE_URL}/api/v3/discounted-cash-flow/{ticker}?limit={str(limit)}?apikey={self.API}'

    @get_json_data(API_KEY)
    def companies_historical_discounted_cash_flow_value(self, ticker: str, limit: int):
        '''
        Companies Historical Discounted Cash Flow Value (Intrinsic Value)
        '''
        return f'{self.BASE_URL}/api/v3/historical-discounted-cash-flow/{ticker}?apikey={self.API}'

    @get_json_data(API_KEY)
    def companies_historical_discounted_cash_flow_value(self, ticker: str, limit: int):
        '''
        Companies Historical Discounted Cash Flow Value (Intrinsic Value)
        '''
        return f'{self.BASE_URL}/api/v3/historical-discounted-cash-flow/{ticker}?period=quarter?apikey={self.API}'

    @get_json_data(API_KEY)
    def companies_historical_discounted_cash_flow_value(self, ticker: str, limit: int):
        '''
        Companies Daily Discounted Cash Flow Value (Intrinsic Value)
        '''
        return f'{self.BASE_URL}/api/v3/historical-daily-discounted-cash-flow/{ticker}?limit={str(limit)}?apikey={self.API}'

    #Market Capitalization
    @get_json_data(API_KEY)
    def market_capitalization(self, ticker: str, limit: int):
        '''
        Market Capitalization
        '''
        return f'{self.BASE_URL}/api/v3/market-capitalization/{ticker}?apikey={self.API}'

    @get_json_data(API_KEY)
    def historical_market_capitalization(self, ticker: str, limit: int):
        '''
        Historical Market Capitalization
        '''
        return f'{self.BASE_URL}/api/v3/historical-market-capitalization/{ticker}?limit={str(limit)}?apikey={self.API}'

    #Symbols List
    @get_json_data(API_KEY)
    def all_ticker_symbols(self, ticker: str, limit: int):
        '''
        All Ticker Symbols
        '''
        return f'{self.BASE_URL}/api/v3/stock/list?apikey={self.API}'

    #Batch Request Stock Companies Price
    @get_json_data(API_KEY)
    def multiple_companies_prices(self, ticker_list):
        '''
        Multiple Companies Prices
        '''
        ticker_string = ''
        for ticker in ticker_list:
            ticker_string += ticker + ','
        return f'{self.BASE_URL}/api/v3/quote/{ticker_string}?apikey={self.API}'

    #Stock Screener
    @get_json_data(API_KEY)
    def stock_screener(self, marketCapMoreThan=None, marketCapLowerThan=None, priceMoreThan=None, priceLowerThan=None, betaMoreThan=None, betaLowerThan=None, volumeMoreThan=None, volumeLowerThan=None, dividendMoreThan=None, dividendLowerThan=None, sector=None):
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
        return f'{self.BASE_URL}/api/v3/stock-screener{query_string}?apikey={self.API}'



        