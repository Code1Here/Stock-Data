import requests
from bs4 import BeautifulSoup

tsla = 'https://finance.yahoo.com/quote/TSLA'
fubo = 'https://finance.yahoo.com/quote/FUBO'
docu = 'https://finance.yahoo.com/quote/DOCU'
rblx = 'https://finance.yahoo.com/quote/RBLX'
abnb = 'https://finance.yahoo.com/quote/ABNB'
goog = 'https://finance.yahoo.com/quote/GOOG'
aapl = 'https://finance.yahoo.com/quote/AAPL'
pypl = 'https://finance.yahoo.com/quote/PYPL'
nvda = 'https://finance.yahoo.com/quote/NVDA'
snow = 'https://finance.yahoo.com/quote/SNOW'
shop = 'https://finance.yahoo.com/quote/SHOP'
u = 'https://finance.yahoo.com/quote/U'
sq = 'https://finance.yahoo.com/quote/SQ'
coin = 'https://finance.yahoo.com/quote/COIN'

watchList = [tsla, fubo, docu, rblx, abnb, goog, aapl, pypl, nvda, snow, shop, u, sq, coin]

for url in watchList:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    earningsDate = soup.find('td', {'data-test':'EARNINGS_DATE-value'}).text
    print(soup.title.text)
    print("Earnings Date:", earningsDate)

    # convert str of today's volume to int
    volume = soup.find('td', {'data-test':'TD_VOLUME-value'}).text
    vol = int(volume.replace(",",""))
    # average volume next
    averageVolume = soup.find('td', {'data-test': 'AVERAGE_VOLUME_3MONTH-value'}).text
    avgVol = int(averageVolume.replace(",",""))

    percentageOffAvgVol = round((((vol - avgVol)/avgVol)*100), 2);
    print("Percentage off Avg-vol:", percentageOffAvgVol,"%\n")
