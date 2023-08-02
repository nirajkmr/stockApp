import math
import time
from flask import jsonify
from .const import HttpStatus

# Data store for trades
trades = []
stocks_data = {
    "TEA": {"name": "TEA Common", "type": "Common", "last_dividend": 0, "fixed_dividend": None, "par_value": 100},
    "POP": {"name": "POP Common", "type": "Common", "last_dividend": 8, "fixed_dividend": None, "par_value": 100},
    "ALE": {"name": "ALE Common", "type": "Common", "last_dividend": 23, "fixed_dividend": None, "par_value": 60},
    "GIN": {"name": "GIN Preferred", "type": "Preferred", "last_dividend": 8, "fixed_dividend": 0.02, "par_value": 100},
    "JOE": {"name": "JOE Common", "type": "Common", "last_dividend": 13, "fixed_dividend": None, "par_value": 250}
}

# Function to calculate the dividend
def calculate_dividend_yield(stock_symbol, price):
    stock = stocks_data.get(stock_symbol)
    if not stock:
        return jsonify({"error": "Stock not found"}), HttpStatus.NOT_FOUND
    if stock and stock["last_dividend"]:
        dividend_yield = stock["last_dividend"] / price
        return dividend_yield
    return None

# Function to calculate P/E Ratio
def calculate_pe_ratio(stock_symbol, price):
    stock = stocks_data.get(stock_symbol)
    if not stock:
        return jsonify({"error": "Stock not found"}), HttpStatus.NOT_FOUND
    if stock and stock["last_dividend"]:
        pe_ratio = price / stock["last_dividend"]
        return pe_ratio
    else:
        return None

# Function to record a trade
def record_trade(stock_symbol, quantity, indicator, price):
    global trades
    trade = {"timestamp": int(time.time()), "stock_symbol": stock_symbol, "quantity": quantity, "indicator": indicator, "price": price}
    trades.append(trade)


# Function to calculate Volume Weighted Stock Price
def calculate_volume_weighted_stock_price(stock_symbol):
    now = int(time.time())
    fifteen_min_before = now - 15 * 60
    total_price_times_quantity = 0
    total_quantity = 0
    for trade in trades:
        if trade["stock_symbol"] == stock_symbol and fifteen_min_before <= trade["timestamp"] <= now:
            total_price_times_quantity += trade["price"] * trade["quantity"]
            total_quantity += trade["quantity"]
    if total_quantity:
        volume_weighted_stock_price = total_price_times_quantity / total_quantity
        return volume_weighted_stock_price
    else:
        return None

# Function to calculate GBCE All Share Index
def calculate_gbce_all_share_index():
    prices = [trade["price"] for trade in trades if trade["price"] > 0]
    if prices:
        geometric_mean = math.exp(math.fsum(math.log(price) for price in prices) / len(prices))
        return float(round(geometric_mean, 2))
    else: return None
