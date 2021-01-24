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

_session = requests.session()
_headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/json',
    'platform': 'web',
    'ver': '3.21.14',
    'User-Agent': '*'
}

API_KEY = ''

def set_api_key(self, API_KEY):
    API_KEY = API_KEY