import time
from binance.client import Client 
import requests
from urllib.parse import quote
import json

telegram_bot_token = "5676807313:AAFtFvGEc0XmXoZknX73tTb3FxcXF1yEwvg"
telegram_chat_id = "-1001506693326"

binance_api_key = 'AGl5cAzJos1uDBx1dwT8epbp35JfpYg6eHKvVp9cWtlfjEj5CWcGsSwVrIx1LszI'
binance_api_secret = 'CjQXwc7wkw0WJElxCeLWb6kEYla9Hoim0wYVc3wzgo1tK7Ca4ccWUHuJsrjFgGDd'
client = Client(binance_api_key, binance_api_secret)

THRESHOLD = 500

def send_message(report):
    try:
        escaped_message = quote(report)
        url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={telegram_chat_id}&text={escaped_message}"
        res = requests.get(url)
        time.sleep(2)
        return res.json()
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

def handle_big_trades(big_trades):
    if big_trades:
        # sorts by ticker and then by value
        sorted_big_trades = sorted(big_trades, reverse=True, key=lambda x: (x[0], x[4], x[1]))
        chunks = []
        report = ''
        for ticker, value, quantity, price, trade_type in sorted_big_trades:

            new_line = f'[{ticker}.{trade_type:<{6}}] {quantity:.4f}*${price:.2f} = ${value:,.2f}\n'
            if len(report) + len(new_line) >= 4096:
                chunks.append(report)
                report = ''
            report += new_line
        
        for report in chunks:
            print('Sending report')
            print(report)
            # send_message(report)
    else:
        print('No big trades')


def main():
    while True:
        big_trades = []
        print('Start BTC.trades')
        bitcoin_trades = client.get_recent_trades(symbol='BTCUSDT')
        for trade in bitcoin_trades:
            quantity = float(trade['qty'])
            price = float(trade['price'])
            value = quantity * price
            if value > THRESHOLD and (trade['isBuyerMaker'] or not trade['isBuyerMaker']):
                if trade['isBuyerMaker']:
                    trade_type = "venda"
                else:
                    trade_type = "compra"
                big_trades.append(('BTC', value, quantity, price, trade_type))

        print('Start BTC.orders')
        bitcoin_orders = client.get_all_orders(symbol='BTCUSDT', limit=10)
        for order in bitcoin_orders:
            quantity = float(order['origQty'])
            price = float(order['price'])
            value = quantity * price
            if value > THRESHOLD and order['status'] == "FILLED":
                if order['side'] == "SELL":
                    trade_type = "venda"
                if order['side'] == "BUY":      
                    trade_type = "compra"
                print(('BTC', value, quantity, price, trade_type))
                big_trades.append(('BTC', value, quantity, price, trade_type))

        print('Start ETH.trades')
        ethereum_trades = client.get_recent_trades(symbol='ETHUSDT')
        for trade in ethereum_trades:
            if float(trade['qty']) > THRESHOLD and (trade['isBuyerMaker'] or not trade['isBuyerMaker']):
                print('ETH condition!')
                quantity = float(trade['qty'])
                price = float(trade['price'])
                value = quantity * price
                if trade['isBuyerMaker']:
                    trade_type = "venda"
                else:
                    trade_type = "compra"                

                big_trades.append(('ETH', value, quantity, price, trade_type))

        print('Start ETH.orders')
        ethereum_orders = client.get_all_orders(symbol='ETHUSDT', limit=10)
        for order in ethereum_orders:
            if float(order['origQty']) > THRESHOLD and order['status'] == "FILLED":
                print('ETH condition2!')
                quantity = float(order['origQty'])
                price = float(order['price'])
                value = quantity * price
                if order['side'] == "SELL":
                    trade_type = "venda"
                elif order['side'] == "BUY":
                    trade_type = "compra"
                
                big_trades.append(('ETH', value, quantity, price, trade_type))

        handle_big_trades(big_trades)
        # Espera 60 segundos para verificar novamente
        time.sleep(10)


if __name__ == '__main__':
    main()