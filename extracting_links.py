# -*- coding: utf-8 -*-
"""Extracting links.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16EfE5UCH0y8rEduS7erXp9Wznodhsbj7
"""

import requests
from bs4 import BeautifulSoup

url = 'https://www.huddle01.com/docs'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

links = [f'"https://www.huddle01.com{link.get("href")}"' for link in soup.find_all('a')]

print(",".join(links))