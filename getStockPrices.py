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

watchList = [aapl, goog, tsla, nvda, pypl, abnb, snow, shop, sq, rblx, u, docu, coin, fubo]
testArray = {}
consoleDecor = '****************************************************'
print('\n')

for url in watchList:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    ### Title & validation
    title = soup.find('h1', {'class':'D(ib) Fz(18px)'}).text
    print(consoleDecor, '\n'+title)
    earningsDate = soup.find('td', {'data-test':'EARNINGS_DATE-value'}).text
    print("Earnings Date:", earningsDate)

    ### End of day closing price
    closingPrice = soup.find('fin-streamer', {'data-test':"qsp-price" }).text
    print("Closing Price: $", closingPrice)

    ### P/E Ratio
    currentPE = soup.find('td', {'data-test':'PE_RATIO-value'}).text
    print("Current P/E (TTM): ", currentPE)

    ### % change off avg vol; in-either direction

    # convert str of today's volume to int
    volume = soup.find('td', {'data-test':'TD_VOLUME-value'}).text
    vol = int(volume.replace(",",""))
    # average volume next
    averageVolume = soup.find('td', {'data-test': 'AVERAGE_VOLUME_3MONTH-value'}).text
    avgVol = int(averageVolume.replace(",",""))
    # round and print
    percentageOffAvgVol = round((((vol - avgVol)/avgVol)*100), 2);
    print("Deviation from Avg-vol:", percentageOffAvgVol,"%\n\n")





    ####
    ## Find marketcap to print to me a reorganized array of value

    # marketCap = soup.find('td', {'data-test':'MARKET_CAP-value'}).text
    # if(marketCap[-1] == 'T'):
    #     marketCap = float(marketCap[:-1]) * 1_000_000_000_000
    # elif(marketCap[-1] == 'B'):
    #     marketCap = float(marketCap[:-1]) * 1_000_000_000
    # elif(marketCap[-1] == 'M'):
    #     marketCap = float(marketCap[:-1]) * 1_000_000

    # testArray[marketCap] = title

#### Use only to sort hard coded values/URLS/Stock picks

# testFinal = sorted(testArray)
# for stock in testFinal:
#     print(testArray[stock])
    