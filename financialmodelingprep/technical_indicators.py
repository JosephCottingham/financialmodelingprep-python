from financialmodelingprep.decorator import get_json_data

class technical_indicators():

    BASE_URL = 'https://financialmodelingprep.com'
    API_KEY = ''

    def __init__(self, API_KEY):
        self.API = API_KEY

    @get_json_data(API_KEY)
    def stock_price(ticker: str, interval: str, period: str, indicator_type: str):
        '''
        Earnings Calendar
        interval: | 1min | 5min | 15min | 30min | 1hour | 4hour | daily |
        type: | SMA | EMA | WMA | DEMA | TEMA | williams | RSI | ADX | standardDeviation
        '''
        return f'{self.BASE_URL}/api/v3/technical_indicator/{interval}/{ticker}?period={period}&type={indicator_type}?apikey={self.API}'

    @get_json_data(API_KEY)
    def stock_price(ticker: str, interval: str, period: str, indicator_type: str):
        '''
        Earnings Calendar
        interval: | 1min | 5min | 15min | 30min | 1hour | 4hour | daily |
        type: | SMA | EMA | WMA | DEMA | TEMA | williams | RSI | ADX | standardDeviation
        '''
        return f'{self.BASE_URL}/api/v3/technical_indicator/{interval}/{ticker}?period={period}&type={indicator_type}?apikey={self.API}'