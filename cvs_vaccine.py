import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime
import json
import os

URL = 'https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.ca.json?vaccineinfo'
url_wi = "https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.wi.json?vaccineinfo"
headers = {
    # 'accept': '*/*',
    # 'accept-encoding': 'gzip, deflate, br',
    # 'accept-language': 'en-US,en;q=0.9',
    # 'cookie': response_cookies,
    "referer": "https://www.cvs.com/immunizations/covid-19-vaccine",
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-fetch-dest': 'empty',
    # 'sec-fetch-mode': 'cors',
    # 'sec-fetch-site': 'same-origin',
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
}
my_headers = {
    'referer': 'https://www.cvs.com/immunizations/covid-19-vaccine',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}

response = requests.get(URL, headers=my_headers)
print(response.status_code)
print(response.text)

response = requests.get(URL, headers=headers)
print(response.status_code)
print(response.text)

response = requests.get(url_wi, headers=headers)
print(response.status_code)
print(response.text)