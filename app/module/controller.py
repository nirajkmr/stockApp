from flask import Flask, request, jsonify
from .const import HttpStatus
from .models import calculate_dividend_yield, calculate_pe_ratio, record_trade, calculate_volume_weighted_stock_price, \
    calculate_gbce_all_share_index

app = Flask(__name__)


@app.route('/dividend_yield', methods=['POST'])
def dividend_yield():
    data = request.get_json()
    stock_symbol = data.get('stock_symbol')
    price = data.get('price')
    dividend_yield = calculate_dividend_yield(stock_symbol, price)
    return jsonify({"dividend_yield": dividend_yield}), HttpStatus.OK


@app.route('/pe_ratio', methods=['POST'])
def pe_ratio():
    data = request.get_json()
    stock_symbol = data.get('stock_symbol')
    price = data.get('price')
    pe_ratio = calculate_pe_ratio(stock_symbol, price)
    return jsonify({"pe_ratio": float(round(pe_ratio,2))}), HttpStatus.OK


@app.route('/record_trade', methods=['POST'])
def record_trade_route():
    data = request.get_json()
    stock_symbol = data.get('stock_symbol')
    quantity = data.get('quantity')
    indicator = data.get('indicator')
    price = data.get('price')
    record_trade(stock_symbol, quantity, indicator, price)
    return jsonify({"message": "Trade recorded successfully!"}), HttpStatus.OK


@app.route('/volume_weighted_stock_price', methods=['POST'])
def volume_weighted_stock_price():
    data = request.get_json()
    stock_symbol = data.get('stock_symbol')
    if not stock_symbol:
        return jsonify({"error": "Stock not found"}), HttpStatus.NOT_FOUND
    volume_weighted_stock_price = calculate_volume_weighted_stock_price(stock_symbol)
    return jsonify({"volume_weighted_stock_price": volume_weighted_stock_price}), HttpStatus.OK


@app.route('/gbce_all_share_index', methods=['GET'])
def gbce_all_share_index():
    gbce_index = calculate_gbce_all_share_index()
    return jsonify({"gbce_all_share_index": gbce_index}), HttpStatus.OK


if __name__ == '__main__':
    app.run(debug=True)
