# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 14:37:27 2021

@author: Anjum Khan
"""


from flask import Flask, render_template, url_for, request, jsonify, Response
import json
import yfinance as yf
import datetime
from datetime import date 
from datetime import datetime
from json import dumps
from time import gmtime, strftime
app = Flask(__name__)

# http://127.0.0.1:5000/?stock_name=ABEV3.SA&number_share=12&date_bought=2020-03-02
@app.route("/")
def home():
    stock_name = request.args.get("stock_name")
    number_share =int(request.args.get("number_share",0, type=int))
    date_bought = request.args.get("date_bought")
    today_date= datetime.now()
    today_date=today_date.strftime("%Y-%m-%d")
    if stock_name and number_share and date_bought:
        
       # print(today_date)
        date_bought= date_bought.replace('/','-')
        date_bought= datetime.strptime(date_bought,"%Y-%m-%d").strftime("%Y-%m-%d")
        print(date_bought)
       
        msft = yf.Ticker(stock_name)
        print(msft)
        try:
            df_start_date=msft.history(start=date_bought)
            old_price=int(df_start_date['Close'][0])
            
            df_end_date= msft.history(start=today_date)
            today_price= int(df_end_date['Close'][0])
            
            old_total_price= int(old_price)*int(number_share)
            
            
            today_total_price= int(today_price)*int(number_share)
            
            
            if old_total_price >today_total_price:  
                loss=(old_total_price)-(today_total_price)
                response = {'results': {'status': 200,
                                    'message': 'Loss Incurred : '+str(loss), 'Stock Name': stock_name, 'Number of Share': number_share, 'share bought date':date_bought,'Today date':today_date,'Old share price':old_price,'current share price':today_price}}
            elif old_total_price==today_total_price:
                response = {'results': {'status': 200,
                                    'message': 'No Profit and Loss', 'Stock Name': stock_name, 'Number of Share': number_share, 'share bought date':date_bought,'Today date':today_date,'Old share price':old_price,'current share price':today_price}}
                
            else:
                profit=(today_total_price)-(old_total_price)
                response = {'results': {'status': 200,
                                    'message': 'Profit Earned : '+str(profit), 'Stock Name': stock_name, 'Number of Share': number_share, 'share bought date':date_bought,'Today date':today_date,'Old share price':old_price,'current share price':today_price}}
        except:
            response = {'results': {'status': 200, 'message': 'Invalid Stock'}}
            
    else:
        response = {'results': {'status': 200, 'message': 'Invalid url'}}
   
            
    return Response(json.dumps(response,indent=4, sort_keys=False , default=str), status=200)
  
    
 # def is_date(string, fuzzy=False):
    #     try: 
    #         parse(string, fuzzy=fuzzy)
    #         return True

    #     except ValueError:
    #         return False
    # date_bought=is_date(date_bought)
    # #print(date_bought)
    # today_date=is_date(today_date)
    # print(today_date)
    

@app.route('/sd')
def specificDate():
    data = yf.download("ABEV3.SA", start="2020-03-01", end="2020-03-30")
    # bought_date = 'asdfeasdfasdf -> invalid date
    # bought_date = '2020/03/11' -> python date format change
    # current_date = format change -> 2021-03-20
    # data = yf.download(stock_name, start=date_bought, end=current_date)
    # df
    # old_price = df[0]['Close']
    # today_price = df[last_position]['Close']
    # Stock Name: stock_name
    # Stock bought: bought_date
    # Number of shares: number_stock
    # Bought price: old_price
    # Total bought price: old_price*number_stock
    # Todays stock price: today_price
    # if old_price (14.72) < today_price (12.49)
    # profit = old_price+today_price
    # profit_earned = profit*number_stock
    # Profit earned: profit_earned
    # else
    # loss = old_price-today_price
    # loss_incured = loss*number_stock
    # Loss incured: loss_incured
    print(data)
    return Response('Okay', status=200)



if __name__ == '__main__':
    app.run()
    # app.run(host="0.0.0.0", port=5002)
