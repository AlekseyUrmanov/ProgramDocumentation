import statistics
import time
import cbpro
import datetime
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from multiprocessing import Process

auth_client = None
pub_client = None


def auth():
    global auth_client, pub_client
    key = ''
    secret = ''
    passphrase = ''

    auth_client = cbpro.AuthenticatedClient(key=key, b64secret=secret, passphrase=passphrase)
    pub_client = cbpro.PublicClient()


auth()

# My algorithm is very simple:
# if current minute trading volume is 1.5 time previous minute trading volume and current minute return is positive,
# you will buy at beginning of next minute and sell after one minute, this is to capture short momentum by volatile trading volume.
# I am restricted to open Crypto account in any exchange due to the citizenship. You can go to Voyager to open account which is zero trade fee.


plotting_data = {'BuyVolumes': [], 'SellVolumes': [], 'TotalVolume': [], 'Prices': []}

min_total_trading_volume = []
min_buy_volume = []
min_sell_volume = []

total_orders = 0

buy_volume = 0
sell_volume = 0
total_volume = 0

crypto_price = 0

var_time = datetime.datetime.now()

min_open_price = 0


def sort_msg(msg):
    global total_orders, buy_volume, sell_volume, var_time, min_buy_volume, min_sell_volume, total_volume, crypto_price, min_open_price

    #print('SORTING DATA')
    msg_type = msg['type']
    if msg_type == 'subscriptions' or msg_type == 'last_match':
        pass
    elif msg_type == 'match':
        side = msg['side']
        size = msg['size']
        price = msg['price']

        total_orders += 1

        if side == 'sell':
            buy_volume += (float(price) * float(size))
            total_volume += (float(price) * float(size))

        else:
            sell_volume += (float(price) * float(size))
            total_volume += (float(price) * float(size))

    elif msg_type == 'ticker':
        crypto_price = float(msg['price'])
    else:
        pass

    if (datetime.datetime.now() - var_time).seconds >= 60:
        min_open_price = crypto_price

        '''print('\nNew minute')
        print(f'Total traded volume = {total_volume}')
        print(f'Min open price : {min_open_price}')'''

        var_time = datetime.datetime.now()
        min_sell_volume.append(sell_volume)
        min_buy_volume.append(buy_volume)
        min_total_trading_volume.append(total_volume)

        plotting_data['BuyVolumes'].append(buy_volume)
        plotting_data['SellVolumes'].append(sell_volume)
        plotting_data['TotalVolume'].append(total_volume)
        plotting_data['Prices'].append(min_open_price)

        buy_volume = 0
        sell_volume = 0
        total_volume = 0

        trade(action=1)
    else:
        pass


to_open = False
open_position = False

profit = 0


def trade(action=0):

    global auth_client, open_position, to_open, crypto_price, profit

    if action == 1:

        if open_position is False and to_open is True:
            print(f'bought market')
            x = auth_client.place_order('ADA-USD', 'buy', order_type='market', size=1)
            print(x)
            open_position = True
            to_open = False

        elif open_position is True and to_open is True:
            print('continued open position')

            to_open = False
            pass

        elif open_position is True and to_open is False:
            print(f'sold market')

            x = auth_client.place_order('ADA-USD', 'sell', order_type='market', size=1)
            print(x)
            open_position = False

            pass

        else:

            pass

    elif action == 0:
        to_open = True
    else:
        pass


def check_conditions():

    global total_volume, buy_volume, sell_volume, min_total_trading_volume, min_open_price, crypto_price

    while True:

        current_volume = total_volume
        if len(min_total_trading_volume) == 0:

            pass
        else:
            '''
            print(f'\nPrevious Minute Trading Volume {min_total_trading_volume[-1]}')
            print(f'Current Trading Volume {total_volume}')
            print(f'Min Open Price : {min_open_price}\nCurrent Price : {crypto_price}')'''

            if current_volume > (1.5 * min_total_trading_volume[-1]) and crypto_price > min_open_price:
                #print('CONDITION MET')
                trade(action=0)

            else:
                pass
        time.sleep(1)


class MyWebsocketClient(cbpro.WebsocketClient):
    def on_open(self):
        self.url = "wss://ws-feed.pro.coinbase.com/"
        self.products = ['ADA-USD']
        self.channels = ['matches',
                         'ticker_1000']  # matches 'user','ticker_1000','full','level2_50','level2_batch' is same as 50
        self.auth = True
        self.api_key = ''
        self.api_passphrase = ''
        self.api_secret = ''
        self.should_print = False
        self.stime = datetime.datetime.now()
        self.is_on = True

        print("--op--")

    def on_message(self, msg):
        # print(msg)
        sort_msg(msg)
        pass

    def on_close(self):
        print((datetime.datetime.now() - self.stime).seconds)
        self.is_on = False
        print("--cd--")


try:
    x = MyWebsocketClient()
    x.start()

    check_conditions()

finally:
    x.close()


