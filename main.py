
import candlestick_plotting as cp
import multi_ticker_plotting as mtp
# import pandas as pd
# from datetime import datetime

if __name__ == "__main__":

    tickers = ["AAPL", "VOO", "MSFT", "GOOGL", "AMZN"]
    ticker = tickers[-1:]

    cp.candlestick_plot(ticker)
    mtp.multi_ticker_plot(tickers)
