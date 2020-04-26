#!/usr/bin/env python

import sys
import urllib.parse
import requests
from bs4 import BeautifulSoup

URL_BASE = 'https://www.roguefitness.com'
# description : link to the search screen, set the inStock filter before copying the link
URL_ADDONS = {
    'SQUAT_STANDS'  : 'strength-equipment/squat-stands?is_salable[0]=1'
}

for key in URL_ADDONS:
    searchUrl = urllib.parse.urljoin(URL_BASE, URL_ADDONS[key])
    r = requests.get(searchUrl)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')

    products = soup.find_all('ul', class_='products-grid')
    print (len(products))
    for product in products:
        print(len(product.text))


