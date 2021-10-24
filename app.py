# import yfinance, pandas and os
import yfinance as yf
import pandas as pd
import requests
from flask import Flask, request,render_template, url_for

app = Flask(__name__)

#Scrape Tickers for Companies from Wikipedia
def getticker():
    wiki_page = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies').text
    sp_data = pd.read_html(wiki_page)
    ticker_df = sp_data[0]
    ticker_options = ticker_df['Symbol']
    return ticker_options


# Retrieve
# Yahoo! Finance Sustainability Scores for each ticker
#We're only doing like 10 right now because scraping is slow. :'(

def cleanData():
    data = webScrapper()
    return data

def webScrapper():
    tickers = getticker()
    i_y = yf.Ticker('KO')
    esg_data = pd.DataFrame.transpose(i_y.sustainability)
    esg_data['company_ticker'] = str(i_y.ticker)
    # print(columns)
    for i in range(0, 10):
        print(tickers[i])
        i_y = yf.Ticker(tickers[i])
        try:
            if i_y.sustainability is not None:
                temp = pd.DataFrame.transpose(i_y.sustainability)
                temp['company_ticker'] = str(i_y.ticker)
                # print(temp)
                esg_data = esg_data.append(temp)
        except IndexError:
            pass
        #data = cleanData(esg_data)
        return esg_data

@app.route('/',methods = ['GET','POST'])
def homepage(result=None):
    #data = webScrapper()
    #Need to connect data to html
    return render_template('main.html')

if __name__ == '__main__':
   app.run(debug=True)