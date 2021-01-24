import argparse
import collections
import getpass
import hashlib
import json
import os
import pickle
import requests
import time
import uuid

from financialmodelingprep import calendars, company_valuation, institutional_fund, stock_time_series, technical_indicators

class financialmodelingprep:


    def __init__(self, API_KEY):

        self._session = requests.session()
        self._headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/json',
            'platform': 'web',
            'ver': '3.21.14',
            'User-Agent': '*'
        }

        self.API_KEY = API_KEY

        self.calendars = calendars.calendars(API_KEY)
        self.company_valuation = company_valuation.company_valuation(API_KEY)
        self.institutional_fund = institutional_fund.institutional_fund(API_KEY)
        self.stock_time_series = stock_time_series.stock_time_series(API_KEY)
        self.technical_indicators = technical_indicators.technical_indicators(API_KEY)