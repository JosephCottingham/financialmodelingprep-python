from financialmodelingprep.decorator import get_json_data

BASE_URL = 'https://financialmodelingprep.com'

class stock_time_series():

    BASE_URL = 'https://financialmodelingprep.com'
    API_KEY = ''

    def __init__(self, API_KEY):
        self.API = API_KEY

    @get_json_data(API_KEY)
    def stock_price(ticker: str):
        '''
        Earnings Calendar
        '''
        return f'{self.BASE_URL}/api/v3/quote-short/{ticker}?apikey={self.API}'

    @get_json_data(API_KEY)
    def stock_price_list(exchange: str):
        '''
        Earnings Calendar
        '''
        return f'{self.BASE_URL}/api/v3/quotes/{exchange}?apikey={self.API}'

    @get_json_data(API_KEY)
    def stock_price_list(interval: str, ticker: str):
        '''
        Earnings Calendar
        interval: 1min | 5min | 15min | 30min | 1hour | 4hour
        '''
        return f'{self.BASE_URL}/api/v3/historical-chart/{interval}/{ticker}?apikey={self.API}'

    @get_json_data(API_KEY)
    def stock_historical_daily_prices(ticker: str, datetime_from=None, datetime_to=None):
        '''
        Earnings Calendar
        '''
        if datetime_to and datetime_from:
            return f'{self.BASE_URL}/api/v3/historical-price-full/{ticker}?from={datetime_from.strftime("%Y-%m-%d")}&to={datetime_to.strftime("%Y-%m-%d")}?apikey={self.API}'
        return f'{self.BASE_URL}/api/v3/historical-price-full/{ticker}?apikey={self.API}'

    @get_json_data(API_KEY)
    def stock_historical_daily_prices_timeseries(ticker: str, timeseries: int):
        '''
        Earnings Calendar
        '''
        return f'{self.BASE_URL}/api/v3/historical-price-full/{ticker}?timeseries={str(timeseries)}?apikey={self.API}'

    @get_json_data(API_KEY)
    def stock_historical_daily_prices_timeseries(ticker_list):
        '''
        Earnings Calendar
        '''
        ticker_string = ''
        for ticker in ticker_list:
            ticker_string += ticker + ','
        return f'{self.BASE_URL}/api/v3/historical-price-full/{ticker_string}?apikey={self.API}'

    @get_json_data(API_KEY)
    def stock_historical_dividends(ticker: str):
        '''
        Earnings Calendar
        '''
        return f'{self.BASE_URL}/api/v3/historical-price-full/stock_dividend/{ticker}?apikey={self.API}'

    @get_json_data(API_KEY)
    def historical_stock_splits(ticker: str):
        '''
        Earnings Calendar
        '''
        return f'{self.BASE_URL}/api/v3/historical-price-full/stock_split/{ticker}?apikey={self.API}'