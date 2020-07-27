#!/usr/bin/env python3
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

#Only works with US stocks at the moment
api_key = 'ENTER YOUR API KEY HERE' # To get a key go here - https://www.alphavantage.co

def get_price():
    print('Enter the stocks ticker')
    ticker = input()

    ts = TimeSeries(key=api_key, output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=ticker,interval = '1min', outputsize='compact')
    close_data = data['4. close']
    last_change = close_data[-1]

    #print(data)
    print('$',last_change)

    repeat = input('Would you like to enter another ticker? ').lower()
    if repeat == 'yes':
        get_price()
    else:
        print('Thanks for using the app ' )

get_price()
