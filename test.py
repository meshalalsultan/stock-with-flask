import investpy
import pandas as pd
import numpy as np 
import datetime
from datetime import datetime
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
'''
start = '2021-02-03'
start_date = datetime.strptime(start, "%Y-%m-%d").strftime("%d/%m/%Y")
print('The Start Date is')
print(start_date)
print('------------------------')
print('The Type is ')
print(type(start_date))
print('------------------------')


