from flask import Flask,url_for ,request, render_template
import pandas as pd 
import numpy as np 
import investpy
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

from tensorflow.keras.models import load_model

model = load_model('model.h5')



app = Flask(__name__)

@app.route('/')
def home():
    return "Hello From The Flask"

@app.route('/index',methods=['GET'])
def index():
    stock = request.args.get('stock')
    stock = stock.upper()
    return 'Your Stock Is ' + stock + " OK"

@app.route('/temp' , methods=['GET' , 'POST'])
def temp():
    stock = request.form.get('stockName')
    start_date = request.form.get('startDate')
    end_date = request.form.get('endDate')
    country = request.form.get('countryName')



    
    
    return render_template('home.html')

@app.route('/only' , methods=['GET' , 'POST'])
def only():
    stock = request.form.get('stockName').upper()
    start = request.form.get('startDate')
    end = request.form.get('endDate')
    country = request.form.get('countryName')
    model = load_model('model.h5')


    start_date = datetime.strptime(start, "%Y-%m-%d").strftime("%d/%m/%Y")
    end_date = datetime.strptime(end, "%Y-%m-%d").strftime("%d/%m/%Y")
    df = investpy.get_stock_historical_data(stock=stock, country=country, from_date=start_date, to_date=end_date)
    df.drop('Currency',axis=1,inplace=True)
    data = df.filter(['Close'])
    dataset = data.values
    scaler = MinMaxScaler(feature_range =(0,1))
    scaled_data = scaler.fit_transform(dataset)

    df = investpy.get_stock_historical_data(stock=stock, country=country, from_date=start_date, to_date=end_date)
    df.drop('Currency' ,axis=1,inplace=True)
    pred_data = df.filter(['Close'])

    last_60_days = pred_data[-60:].values

    last_60_days_scaled = scaler.fit_transform(last_60_days)
    X_test = []
    X_test.append(last_60_days_scaled)
    X_test = np.array(X_test)
    X_test = np.reshape(X_test , (X_test.shape[0] , X_test.shape[1] , 1))

    pred_price = model.predict(X_test)
    pred_price = scaler.inverse_transform(pred_price)
    print(pred_price)

    com_profile = investpy.get_stock_company_profile(stock=stock, country=country, language='english')
    profile = com_profile['desc']


    return render_template('only.html' , stock= stock , start_date=start_date , end_date=end_date,profile=profile , pred_price=pred_price  )





if __name__ == '__main__':
    app.run()