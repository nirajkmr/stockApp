# Super Simple Stock Market
Building a super simple stock market assignment in Python Flask.

## Application Requirements

The project fulfills the following requirements:

1. Calculate the Dividend Yield for a given stock and price.
2. Calculate the P/E Ratio for a given stock and price.
3. Record a trade with the timestamp, quantity of shares, buy or sell indicator, and traded price.
4. Calculate the Volume Weighted Stock Price based on trades in the past 15 minutes.
5. Calculate the GBCE All Share Index using the geometric mean of prices for all stocks.

## API Endpoints

- `POST /calculate_dividend_yield`: Calculate the dividend yield for a given stock and price.
- `POST /pe_ratio`: Calculate the P/E Ratio for a given stock and price.
- `POST /record_trade`: Record a trade with timestamp, quantity, buy/sell indicator, and traded price.
- `POST /volume_weighted_stock_price`: Calculate the Volume Weighted Stock Price based on trades in the past 15 minutes.
- `GET /calculate_gbce_all_share_index`: Calculate the GBCE All Share Index.
  



**Installation**

The commands below to install the application and its dependencies:

    $ git clone https://github.com/nirajkmr/stockApp.git
    $ cd stockApp
    $ python3 -m venv .venv
    $ .venv\Scripts\activate (windows) / . .venv/bin/activate (macOS/Linux)
    (venv) pip install -r requirements.txt 

## Running the Application

1. Once the installation is completed, Run the application by executing `python run.py` in your terminal.
2. The application will start in development mode at `http://localhost:8000/`.
