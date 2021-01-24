from financialmodelingprep.decorator import get_json_data

BASE_URL = 'https://financialmodelingprep.com'

class institutional_fund():

    BASE_URL = 'https://financialmodelingprep.com'
    API_KEY = ''

    def __init__(self, API_KEY):
        self.API = API_KEY

    @get_json_data(API_KEY)
    def institutional_holder(ticker: str):
        '''
        Earnings Calendar
        '''
        return f'{self.BASE_URL}/api/v3/institutional-holder/{ticker}?apikey={self.API}'

    @get_json_data(API_KEY)
    def mutual_fund_holder(ticker: str):
        '''
        Earnings Calendar
        '''
        return f'{self.BASE_URL}/api/v3/institutional-holder/{ticker}?apikey={self.API}'

    @get_json_data(API_KEY)
    def etf_holder(ticker: str):
        '''
        Earnings Calendar
        '''
        return f'{self.BASE_URL}/api/v3/etf-holder/{ticker}?apikey={self.API}'

    @get_json_data(API_KEY)
    def etf_sector_weightings(ticker: str):
        '''
        Earnings Calendar
        '''
        return f'{self.BASE_URL}/api/v3/etf-sector-weightings/{ticker}?apikey={self.API}'

    @get_json_data(API_KEY)
    def etf_country_weightings(ticker: str):
        '''
        Earnings Calendar
        '''
        return f'{self.BASE_URL}/api/v3/etf-country-weightings/{ticker}?apikey={self.API}'

    @get_json_data(API_KEY)
    def rss_feeds(ticker: str, limit: int):
        '''
        Earnings Calendar
        '''
        return f'{self.BASE_URL}/api/v3/rss_feeds?limit={limit}?apikey={self.API}'

    @get_json_data(API_KEY)
    def cik_list(ticker: str):
        '''
        Earnings Calendar
        '''
        return f'{self.BASE_URL}/api/v3/cik_list?apikey={self.API}'

    @get_json_data(API_KEY)
    def cik_search(name: str):
        '''
        Earnings Calendar
        '''
        return f'{self.BASE_URL}/api/v3/cik-search/{name}?apikey={self.API}'


    @get_json_data(API_KEY)
    def cik_search(cik: str):
        '''
        Earnings Calendar
        '''
        return f'{self.BASE_URL}/api/v3/cik/{cik}?apikey={self.API}'

    @get_json_data(API_KEY)
    def form_thirteen(cik: str, datetime_cur):
        '''
        Earnings Calendar
        '''
        return f'{self.BASE_URL}/api/v3/form-thirteen/{cik}?date={datetime_cur.strftime("%Y-%m-%d")}?apikey={self.API}'

    @get_json_data(API_KEY)
    def cusip_mapper(cusip: str):
        '''
        Earnings Calendar
        '''
        return f'{self.BASE_URL}/api/v3/cusip/{cusip}?apikey={self.API}'


