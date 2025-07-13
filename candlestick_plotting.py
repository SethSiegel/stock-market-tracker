#! python3
# candlestick plotter with yfinance and plotly
import yfinance as yf
import plotly.graph_objects as go


def candlestick_plot(ticker):
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
        name=f'{ticker} Live Market Data')])

    fig.update_layout(
        xaxis_rangeslider_visible=False,
        title=f'{ticker} Live Market Data',
        xaxis_title='Time (minutes)',
        yaxis_title='Price (USD)',
        template='plotly_dark')

    fig.show()


if __name__ == "__main__":
    current_script_path = __file__
    print(f'wrong file: {current_script_path}')
    print("This file is not meant to be run directly.")
    print("Please run the main script instead.")
