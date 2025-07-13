#!python3
# multi-ticker plotting with yfinance and plotly
# also adds in the daily difference between open and close prices

import yfinance as yf
import plotly.graph_objects as go


def calc_daily_diff(ticker, data):
    open = data[ticker]['Open']
    close = data[ticker]['Close']
    diff = close - open
    return diff


def multi_ticker_plot(tickers):
    tickers_for_yfinance = [item.replace(",", "") for item in tickers]
    data = yf.download(tickers_for_yfinance, period='2y',
                       ignore_tz=True, group_by='ticker',
                       auto_adjust=False)
    data = data.reset_index()

    fig = go.Figure()
    for ticker in tickers:
        plot_ticker(ticker, data, fig)
        data_diff = calc_daily_diff(ticker, data)
        fig.add_trace(go.Scatter(
            x=data['Date'], y=data_diff, mode='lines',
            name=f'{ticker} Daily Diff'))
    fig.show()


def plot_ticker(ticker, data, fig):
    fig.add_trace(go.Scatter(x=data['Date'], y=data[ticker]['Open'],
                  mode='lines', name=f'{ticker} Open'))


if __name__ == "__main__":
    current_script_path = __file__
    print(f'wrong file: {current_script_path}')
    print("This file is not meant to be run directly.")
    print("Please run the main script instead.")


'''
df = yf.download(tickers="VOO", period='1d', interval='1m',
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
'''
