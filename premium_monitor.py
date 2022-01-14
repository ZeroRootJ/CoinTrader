#!/usr/bin/env python
# coding: utf-8

# In[12]:


import requests
import json
import ccxt
import pyupbit
import datetime
import time


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def upbit_get_usd_krw():
    url = 'https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWUSD'
    exchange =requests.get(url, headers=headers).json()
    return exchange[0]['basePrice']

def get_premium_XLM():
    binance = ccxt.binance()
    EXR = upbit_get_usd_krw()
    orderbook_us = binance.fetch_order_book('XLM/USDT')

    us_ask = orderbook_us['asks'][0][0]*EXR
    orderbook_kr = pyupbit.get_orderbook('KRW-XLM')

    kr_bid = orderbook_kr['orderbook_units'][0]['bid_price']
    prem = (kr_bid-us_ask)/kr_bid
    
    return (prem,kr_bid,us_ask)

flag = False
prem = 0.02
while(True):
    past = prem
    prem = get_premium_XLM()[0]
    if flag is False and prem < -0.02:
        print('*****BUY*****')
        flag = True
    elif flag and prem > 0:
        print('*****SELL*****')
        flag = False
        
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), prem)
    time.sleep(10)

