#!/usr/bin/env python
# coding: utf-8

# # 변동성 돌파 전략 Volatility breakout
# 
# 가격변동폭 계산 : 전일 고가 - 전일 저가
# 
# 매수 기준 : 당일 시간에서 변동폭 * (k=0.5) 이상 상승시 해당 가격에 매수
# 
# 매도 기준 : 당일 종가에 매도

# In[1]:


from pyupbit import *
import time
import datetime


# In[2]:


def buy_crypto(ticker):
    pass

def sell_crypto(ticker):
    pass


# In[3]:


def get_target_price(ticker,k):
    pd = get_ohlcv(ticker)
    price_diff = pd.iloc[-2]['high'] - pd.iloc[-2]['low']
    target = pd.iloc[-1]['open'] + price_diff * k
    return target


# In[4]:


ticker = "KRW-BTC"
now = datetime.datetime.now()
m_open = datetime.datetime(now.year,now.month,now.day) + datetime.timedelta(1.375)
target = get_target_price(ticker,0.5)
print("[START] Volatility Breakout TRADER")

# for logging
loop = 0

while True:
    try:
        # SELL ALL & update target price when market starts
        now = datetime.datetime.now()
        if m_open < now < m_open + datetime.timedelta(seconds=10):
            sell_crypto(ticker)
            print("[SELL] ", str(datetime.datetime.now()))
            flag = True
            target = get_target_price(ticker,0.5)
            m_open = datetime.datetime(now.year,now.month,now.day) + datetime.timedelta(1.375)

        # BUY if price>target price
        if get_current_price(ticker) > target and flag:
            buy_crypto(ticker)
            print("[BUY] ", str(datetime.datetime.now()))
            print("PRICE: ",get_current_price(ticker)," TARGET",target)
            flag = False
            
        if loop%100 is 0:
            print("[LOG] ",loop,"loops / ",str(datetime.datetime.now()))
            loop+=1
    except:
        print('[ERR] ', str(datetime.datetime.now()))

    time.sleep(1) #prevents overload

