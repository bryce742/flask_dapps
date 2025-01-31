from flask import Blueprint
from flask import render_template
import requests
import json

home_bp = Blueprint('home', __name__, template_folder='templates', static_folder='static')

def fetch_price_info(chainId,pairId):
    endpoint = f"https://api.dexscreener.com/latest/dex/pairs/{chainId}/{pairId}"
    response = requests.get(
        endpoint,
        headers={}
    )
    return response.json()

def bonding_percentage():
    ...



@home_bp.route('/', methods=['GET'])
@home_bp.route('/home', methods=['GET'])
def home():
    price_info = fetch_price_info('solana','22Ff6B7Hr6CJwCxSBromFtBfwva88QhwNMZqZgjwojR4')
    volume = price_info['pairs'][0]['volume']
    market_Cap = price_info['pairs'][0]['marketCap']

    percent_bond = (float(market_Cap) / 99209) * 100
    percent_bond = f"{percent_bond:.2f}"
    fraction_bonded = float(percent_bond) / 100
    fraction_remaining = 1 - fraction_bonded


    price_info_parsed = {
        "marketCap": market_Cap,
        "volume": {
            "hr24": volume['h24'],
            "hr6": volume['h6'],
            "hr1": volume['h1'],
            "m5": volume['m5']
        },
        "percent_bond": percent_bond,
        "fraction_bonded": fraction_bonded,
        "fraction_remaining": fraction_remaining
    }
    content = {
        "page_name": "Home",
        "page_subtitle": "Who will finish their hotdog first?"
    }

    return render_template('home.html', title='Home', content=content, price_info_parsed=price_info_parsed)