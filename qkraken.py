#! /usr/bin/env python
# Get current trading info on listed coins on Kraken.
#
import datetime
import requests


# list of coins to report on - just add more if you want to see them
#coins = ["XBTUSD","ETHUSD","ZECUSD","DOGEUSD"]
coins = ["XBTUSD"]

for c in coins:
    # collect info and date info for each coin in the list
    qstring = "https://api.kraken.com/0/public/Ticker?pair=" + c
    resp = requests.get(qstring)
    resptime = requests.get('https://api.kraken.com/0/public/Time')
    unixtime = resptime.json()["result"]["unixtime"]
    now2 = datetime.datetime.fromtimestamp(unixtime).strftime('%Y-%m-%d %H:%M:%S')
    jresponse = resp.json()
    jresult = jresponse["result"]

    # print it out
    for k1, v1 in jresult.items():
    #    jbtc = jresult["XETHZUSD"] 
        print("\nKraken Price For",c,"at",now2,"\n")
        for k, v in v1.items():
            if (k == "a"):  # Most recent asking price, whole lot volume, lot volume
                price = "${:,.2f}".format(float(v[0]))
                print ("Ask: ",price,": WLVol ", v[1], ": LVol ", v[2])
            if (k == "b"):  # Most recent bid price, whole lot volume, lot volume
                price = "${:,.2f}".format(float(v[0]))
                print ("Bid: ",price,": WLVol ", v[1], ": LVol ", v[2])
            if (k == "c"):  # Last trade closed price, lot volume
                price = "${:,.2f}".format(float(v[0]))
                print ("Last: ",price,": LVol ", v[1])
            if (k == "o"):   # Today's opening price
                vtoday = "${:,.2f}".format(float(v))
                print ("Open: Today",vtoday)
            if (k == "l"):   # Today's low, last 24 hours
                vtoday = "${:,.2f}".format(float(v[0]))
                last24 = "${:,.2f}".format(float(v[1]))
                print ("Low: Today",vtoday,": Last24",last24)
            if (k == "h"):   # Today's high, last 24 hours
                vtoday = "${:,.2f}".format(float(v[0]))
                last24 = "${:,.2f}".format(float(v[1]))
                print ("High: Today",vtoday,": Last24",last24)
            if (k == "v"):   # Volume today and last 24 hours
                vtoday = "{:,.2f}".format(float(v[0]))
                last24 = "{:,.2f}".format(float(v[1]))
                print ("Vol: Today",vtoday,": Last24",last24)
            if (k == "p"):   # Volume Weighted Average today, last 24 hours
                vtoday = "{:,.2f}".format(float(v[0]))
                last24 = "{:,.2f}".format(float(v[1]))
                print ("Vol Avg: Today",vtoday,": Last24",last24)
            if (k == "t"):   # Number of trades today, last 24 hours
                vtoday = "{:,.2f}".format(float(v[0]))
                last24 = "{:,.2f}".format(float(v[1]))
                print ("Trades: Today",vtoday,": Last24",last24)
