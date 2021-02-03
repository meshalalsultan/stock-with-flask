import investpy
import pandas as pd
import numpy as np 
import datetime
from datetime import datetime
from keras.models import Sequential
from keras .layers import Dense , LSTM ,Conv2D, Flatten
import tensorflow as tf
import re
import time
from keras.models import Sequential
from keras .layers import Dense , LSTM ,Conv2D, Flatten
import math
from sklearn.preprocessing import MinMaxScaler

from keras.models import load_model
import os
from keras.models import model_from_json
from tensorflow.keras.models import load_model
'''
print ('ok')

profile = investpy.get_stock_company_profile(stock='AAPL', country='United States', language='english')

print (profile['desc'])

data = investpy.get_stock_financial_summary(stock='AAPL', country='United States', summary_type='income_statement', period='annual')
print(len(data))
#print(data.columns)
print(data['Gross Profit'])
#print(data['Gross Profit'].index[0])
#data = investpy.get_stock_historical_data(stock='bbva', country='spain', from_date='01/01/2010', to_date='01/01/2019')

start = '2021-02-03'
start_date = datetime.strptime(start, "%Y-%m-%d").strftime("%d/%m/%Y")
print('The Start Date is')
print(start_date)
print('------------------------')
print('The Type is ')
print(type(start_date))
print('------------------------')

df.drop('Currency',axis=1,inplace=True)


from tensorflow.keras.models import load_model

model = load_model('model.h5')

print('ok')
'''
c = 'kuwait'
data = investpy.get_stock_historical_data(stock='zain', country=c, from_date='01/01/2010', to_date='01/01/2019')
print(data.head())