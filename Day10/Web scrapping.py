import urllib.request
from bs4 import BeautifulSoup as bs
import re
import pandas as pd
page = urllib.request.urlopen("https://www.horoscope.com/us/index.aspx")
soup = bs(page)

names = soup.body.findAll('a')
function_names = re.findall('id="src-hp-.\w+"',str(names))
function_names = [item[11:] for item in function_names]
function_names = [item[:-1] for item in function_names]
function_names.remove('dpo')
description = soup.body.findAll('p')
function_usage =[]

for item in description:
    item = item.text
    function_usage.append(item)

#print(len(function_names))
#print(len(function_usage[:12]))
data = pd.DataFrame({'Zodiac': function_names, 'Date': function_usage[:12]})
print(data)