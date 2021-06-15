import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime
import json
import os

url_ca = 'https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.ca.json?vaccineinfo'
url_wi = "https://www.cvs.com/immunizations/covid-19-vaccine.vaccine-status.wi.json?vaccineinfo"

my_headers = {
    'referer': 'https://www.cvs.com/immunizations/covid-19-vaccine',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}

response = requests.get(url_ca, headers=my_headers)
print(response.status_code)
print(response.text)

response = requests.get(url_wi, headers=my_headers)
print(response.status_code)
print(response.text)