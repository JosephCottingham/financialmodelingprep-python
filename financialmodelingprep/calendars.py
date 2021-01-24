from financialmodelingprep.decorator import get_json_data

BASE_URL = 'https://financialmodelingprep.com'
class calendars():

    BASE_URL = 'https://financialmodelingprep.com'
    API_KEY = ''

    def __init__(self, API_KEY):
        self.API = API_KEY

    @get_json_data(API_KEY)
    def earning_calendar(self):
        '''
        Earnings Calendar
        '''
        return f'{self.BASE_URL}/api/v3/earning_calendar?apikey={self.API}'

    @get_json_data(API_KEY)
    def earning_calendar_period(self, datetime_from, datetime_to):
        '''
        Earnings Calendar with period
        '''
        return f'{self.BASE_URL}/api/v3/earning_calendar?from={datetime_from.strftime("%Y-%m-%d")}&to={datetime_to.strftime("%Y-%m-%d")}?apikey={self.API}'

    @get_json_data(API_KEY)
    def company_historical_earnings_calender(self, ticker: str, limit: int):
        '''
        Earnings Calendar with period
        '''
        return f'{self.BASE_URL}/api/v3/earning_calendar/{ticker}?limit={str(limit)}?apikey={self.API}'


    @get_json_data(API_KEY)
    def company_historical_earnings_calender(self, datetime_from, datetime_to):
        '''
        Earnings Calendar with period
        '''
        return f'{self.BASE_URL}/api/v3/ipo_calendar?from={datetime_from.strftime("%Y-%m-%d")}&to={datetime_to.strftime("%Y-%m-%d")}?apikey={self.API}'

    @get_json_data(API_KEY)
    def ipo_calendar(self, datetime_from, datetime_to):
        '''
        Earnings Calendar with period
        '''
        return f'{self.BASE_URL}/api/v3/ipo_calendar?from={datetime_from.strftime("%Y-%m-%d")}&to={datetime_to.strftime("%Y-%m-%d")}?apikey={self.API}'

    @get_json_data(API_KEY)
    def stock_split_calendar(self, datetime_from, datetime_to):
        '''
        Earnings Calendar with period
        '''
        return f'{self.BASE_URL}/api/v3/stock_split_calendar?from={datetime_from.strftime("%Y-%m-%d")}&to={datetime_to.strftime("%Y-%m-%d")}?apikey={self.API}'

    @get_json_data(API_KEY)
    def stock_dividend_calendar(self, datetime_from, datetime_to):
        '''
        Earnings Calendar with period
        '''
        return f'{self.BASE_URL}/api/v3/stock_dividend_calendar?from={datetime_from.strftime("%Y-%m-%d")}&to={datetime_to.strftime("%Y-%m-%d")}?apikey={self.API}'

    @get_json_data(API_KEY)
    def economic_calendar(self, datetime_from, datetime_to):
        '''
        Earnings Calendar with period
        '''
        return f'{self.BASE_URL}/api/v3/economic_calendar?from={datetime_from.strftime("%Y-%m-%d")}&to={datetime_to.strftime("%Y-%m-%d")}?apikey={self.API}'

    @get_json_data(API_KEY)
    def economic_calendar(self, datetime_from, datetime_to):
        '''
        Earnings Calendar with period
        '''
        return f'{self.BASE_URL}/api/v3/economic_calendar?from={datetime_from.strftime("%Y-%m-%d")}&to={datetime_to.strftime("%Y-%m-%d")}?apikey={self.API}'