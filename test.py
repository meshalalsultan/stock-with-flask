import investpy
import pandas as pd
import numpy as np 

print ('ok')

profile = investpy.get_stock_company_profile(stock='AAPL', country='United States', language='english')

print (profile['desc'])