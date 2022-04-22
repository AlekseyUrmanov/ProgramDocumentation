import statistics
import time
import cbpro
import datetime
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from multiprocessing import Process

auth_client = None
pub_client = None

'''
# My algorithm is very simple:
# if current minute trading volume is 1.5 time previous minute trading volume and current minute return is positive,
# you will buy at beginning of next minute and sell after one minute, this is to capture short momentum by volatile trading volume.
# I am restricted to open Crypto account in any exchange due to the citizenship. You can go to Voyager to open account which is zero trade fee.


Can you change to another one that , if previous 5 minute return is negative and current 5 minute return is 
positive. And current 5 minute trading volume is 1.5 time greater than previous 5 minute trading volume or 0.5
time less than previous 5 minute trading volume, you will buy and sell in next 5 minute. Current algorithm profit
will be eaten all by fees

Can you set a time interval? If the trade occurs after 8 pm and next day 4 am for weekday, and also for weekend,
 the time interval bar for BTC or ETH will be 15 minutes rules, for ADA, the rule will be 30 minutes. Other time,
  the rule for BTC and ETH is 5 minutes, for other like ADA will be 15 minutes.
'''


def auth():
    global auth_client, pub_client
    key = '8811ae1f541f911b68394649c73d17e8'
    secret = 's1L46eZRpoHdWYu6DcYROQugtgY7rrfGu7S/jUGEWMTIDUC2bgiV3c8FB1lxjVF3NHm9UnTL6U7p6A+Mptgjew=='
    passphrase = 'omgvd80zrdr'

    auth_client = cbpro.AuthenticatedClient(key=key, b64secret=secret, passphrase=passphrase)
    pub_client = cbpro.PublicClient()


auth()


volume = 0
volumes = []

total_orders = 0

prices = []

start_time = datetime.datetime.now()
trading_time = start_time

trading_interval = 5

return_condition = False
volume_condition = False

minute = 0

tick_price = 0

# variables should be organized into object trader class


def sort_msg(msg):
    global total_orders, start_time, volume, volumes, tick_price, prices

    # bugs out sometimes due to connectivity, mostly fixed

    msg_type = msg['type']

    if msg_type == 'subscriptions' or msg_type == 'last_match' or msg_type is None:
        pass
    elif msg_type == 'match':
        # side = msg['side']
        size = msg['size']
        price = msg['price']

        total_orders += 1
        volume += float(price) * float(size)

    elif msg_type == 'ticker':
        tick_price = float(msg['price'])
        #print(tick_price)

    else:
        pass

    # criterion for trading 5minute intervals,
    # no interchangeable specification has been added.
    # time interval 8pm/4am has not been added due to mac timing issues

    if (datetime.datetime.now()-start_time).seconds >= (5*60):
        start_time = datetime.datetime.now()

        if len(volumes) > 1:
            volumes.pop(0)
            prices.pop(0)
            volumes.append(volume)
            prices.append(tick_price)
        else:
            volumes.append(volume)
            prices.append(tick_price)

        print(volumes)
        print(volume)
        print(prices)
        print(tick_price)

        volume = 0
        trade(action=1)

    else:
        pass


to_open = False
open_position = False

profit = 0

# entire trader functionality should be re worked


def trade(action=0):

    global auth_client, open_position, to_open, profit

    if action == 1:

        if open_position is False and to_open is True:
            print(f'bought market')
            #x = auth_client.place_order('ADA-USD', 'buy', order_type='market', size=1)
            #print(x)
            open_position = True
            to_open = False

        elif open_position is True and to_open is True:
            print('continued open position')

            to_open = False
            pass

        elif open_position is True and to_open is False:
            print(f'sold market')

            #x = auth_client.place_order('ADA-USD', 'sell', order_type='market', size=1)
            #print(x)
            open_position = False

            pass

        else:

            pass

    elif action == 0:
        to_open = True
    else:
        pass


def check_conditions():

    global volumes, tick_price, volume, prices

    while True:

        if x.is_on is False:
            x.start()
        else:
            pass

        if len(volumes) <= 1:
            pass
        else:
            if (prices[1] - prices[0] < 0) and (tick_price > prices[1]):
                # within a 5 minute interval the current return can switch from positive to negative so the trader
                # will place a trade if the return goes positive and ends the 5 min period negative which is
                # counterintuitive

                # conditions need some work
                if (volume > 1.5 * volumes[1]) or (volume < 0.5 * volumes[1]):
                    trade()
                else:
                    pass
            else:
                pass
        time.sleep(1)


class MyWebsocketClient(cbpro.WebsocketClient):
    def on_open(self):
        self.url = "wss://ws-feed.pro.coinbase.com/"
        self.products = ['ADA-USD']
        self.channels = ['matches',
                         'ticker_1000']
        self.auth = True
        self.api_key = '8811ae1f541f911b68394649c73d17e8'
        self.api_passphrase = 'omgvd80zrdr'
        self.api_secret = 's1L46eZRpoHdWYu6DcYROQugtgY7rrfGu7S/jUGEWMTIDUC2bgiV3c8FB1lxjVF3NHm9UnTL6U7p6A+Mptgjew=='
        self.should_print = False
        self.stime = datetime.datetime.now()
        self.is_on = True

        print("--op--")

    def on_message(self, msg):
        # print(msg)
        sort_msg(msg) # routes message from websocket into processing function
        pass

    def on_close(self):
        print((datetime.datetime.now() - self.stime).seconds)
        self.is_on = False
        print("--cd--")


try:
    x = MyWebsocketClient()  # establish websocket object
    x.start() # start connection

    check_conditions() # check if conditions have been met

finally:
    x.close()  # when you kill the program the web socket will take a few seconds to close.


