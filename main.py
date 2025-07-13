import yfinance as yf
import plotly.graph_objects as go
# import pandas as pd
# from datetime import datetime

ticker = "VOO"

df = yf.download(tickers=ticker, period='1d', interval='1m',
                 ignore_tz=True)
df.columns = ['Close', 'High', 'Low', 'Open', 'Volume']
df = df.reset_index()

dfTime = df['Datetime'].dt.strftime('%H:%M')

fig = go.Figure(data=[go.Candlestick(
    x=dfTime,
    open=df['Open'],
    high=df['High'],
    low=df['Low'],
    close=df['Close'],
    name='APPLE Live Market Data')])

fig.update_layout(
    xaxis_rangeslider_visible=False,
    title='AAPL Live Market Data',
    xaxis_title='Time (minutes)',
    yaxis_title='Price (USD)',
    template='plotly_dark')

fig.show()


# print(dfTime)
