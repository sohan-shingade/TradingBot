from alpaca_trade_api import REST
from timedelta import Timedelta
from datetime import datetime
from finbert_utils import estimate_sentiment
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
BASE_URL = "https://paper-api.alpaca.markets/v2"

api = REST(base_url=BASE_URL, key_id=API_KEY, secret_key=API_SECRET)

def get_dates(): 
    today = datetime.today().strftime('%Y-%m-%d')
    three_days_prior = (datetime.today() - Timedelta(days=3)).strftime('%Y-%m-%d')
    return today, three_days_prior

def get_sentiment(symbol="SPY"): 
        today, three_days_prior = get_dates()
        news = api.get_news(symbol=symbol, 
                                 start=three_days_prior, 
                                 end=today) 
        news = [ev.__dict__["_raw"]["headline"] for ev in news]
        print(news)
        probability, sentiment = estimate_sentiment(news)
        return probability, sentiment 

def buy_or_sell(probability, sentiment, symbol="SPY"):
    
    if sentiment == "positive" and probability > .999:
        return "buy"
    elif sentiment == "negative" and probability > .999:
        return "sell"
    else:
        return "hold"
    
##prompt the user to enter a symbol
symbol = input("Enter a symbol: ")
##call the get_sentiment function
probability, sentiment = get_sentiment(symbol)
print(probability, sentiment)
##call the buy_or_sell function 
result = buy_or_sell(probability, sentiment, symbol)
##print the result
print(result)
