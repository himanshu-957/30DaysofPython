from fastapi import FastAPI
from enum import Enum
app = FastAPI()

class Signs(str, Enum):
    aries = "aries"
    taur = "taur"
    gem = "gem"
    canc = "canc"
    leo = "leo"
    virgo = "virgo"
    lib = "lib"
    scpo = "scpo"
    sag = "sag"
    cap = "cap"
    aqua = "aqua"
    pisc = "pisc"
@app.get("/horoscope/{name}")
async def horoscope(name:Signs):
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
    s = 0

    for i in range(0,12):
        if function_names[i] == name:
            s = i

#print(len(function_names))
#print(len(function_usage[:12]))
    date = function_usage[:12]
    data = {'Zodiac': function_names[s], 'Date': date[s]}
    return data