BASE_URL = 'https://financialmodelingprep.com'

@get_json_data
@staticmethod
def company_profile(ticker: str):
    '''
    Company profile
    '''
    return get_jsonparsed_data(f'{self.BASE_URL}/api/v3/profile/{ticker}')

@get_json_data
@staticmethod
def company_qoute(ticker: str):
    '''
    Company quote
    '''
    return f'{self.BASE_URL}/api/v3/quote/{ticker}'

@get_json_data
@staticmethod
def key_executives(ticker: str):
    '''
    Key Executives
    '''
    return f'{self.BASE_URL}/api/v3/key-executives/{ticker}'

@get_json_data
@staticmethod
def search(query: str, limit: int, exchange: str):
    '''
    Search
    Values for exchange parameter are: ETF | MUTUAL_FUND | COMMODITY | INDEX | CRYPTO | FOREX | TSX | AMEX | NASDAQ | NYSE | EURONEXT
    '''
    return f'{self.BASE_URL}/api/v3/search?query={query}&limit={str(limit)}&exchange={exchange}'

@get_json_data
@staticmethod
def ticker_search(query: str, limit: int, exchange: str):
    '''
    Ticker Search
    Values for exchange parameter are: ETF | MUTUAL_FUND | COMMODITY | INDEX | CRYPTO | FOREX | TSX | AMEX | NASDAQ | NYSE | EURONEXT
    '''
    return f'{self.BASE_URL}/api/v3/search-ticker?query={query}&limit={str(limit)}&exchange={exchange}'

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