from flask import Flask,url_for ,request, render_template
import pandas as pd 
import numpy as np 
import investpy



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

    
    
    return render_template('home.html' , stock= stock , start_date=start_date , end_date=end_date )

@app.route('/only' , methods=['GET' , 'POST'])
def only():
    stock = request.form.get('stockName').upper()
    start_date = request.form.get('startDate')
    end_date = request.form.get('endDate')
    
    com_profile = investpy.get_stock_company_profile(stock=stock, country='United States', language='english')
    profile = com_profile['desc']


    return render_template('only.html' , stock= stock , start_date=start_date , end_date=end_date,profile=profile )





if __name__ == '__main__':
    app.run()