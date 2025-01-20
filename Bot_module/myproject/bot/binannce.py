# bot/binance_api.py
from binance.client import Client

API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'

client = Client(API_KEY, API_SECRET)

def get_account_info():
    return client.get_account()