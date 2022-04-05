import cbpro
import datetime

# simple websocket connectivity function for data and trading


class MyWebsocketClient(cbpro.WebsocketClient):
    def on_open(self):
        self.url = "wss://ws-feed.pro.coinbase.com/"
        # connectivity URL

        self.products = ['ADA-USD']
        # trading product, or data collecting product
        # notation XXX-USD or other pair

        self.channels = ['full', 'level2_50']
        # matches 'user','ticker_1000','full','level2_50','level2_batch' is same as 50
        # each channel has specific qualities an results and authentication levels

        self.auth = True
        # authentication choice

        # Authentication parameters
        self.api_key = ''
        self.api_passphrase = ''
        self.api_secret = ''

        # Basic data collection points
        self.should_print = False
        self.stime = datetime.datetime.now()
        self.is_on = True

        print("--op--")

    def on_message(self, msg):
        print(msg)
        # add processing or sorting function
        pass

    def on_close(self):
        print((datetime.datetime.now() - self.stime).seconds)

        self.is_on = False
        print("--cd--")

# data processing function skeleton, includes price updates and order updates and limit order book updates


def process_data(msg):

    if msg['type'] == 'subscriptions':

        pass

    else:

        msg_type = msg['type']

        if msg_type == 'snapshot':

            pass

        elif 'user_id' in msg:

            if msg['user_id'] == '':

                if msg_type == 'received':

                    if msg['order_type'] == 'limit':

                        pass

                    elif msg['order_type'] == 'market':

                        pass

                elif msg_type == 'open':

                    pass

                elif msg_type == 'done':

                    pass

                elif msg_type == 'match':

                    pass

                else:

                    pass

        elif msg_type == 'received':

            pass

        elif msg_type == 'open':

            pass

        elif msg_type == 'done':

            pass

        elif msg_type == 'match':

            pass

        elif msg_type == 'change':

            pass

        elif msg_type == 'activate':

            pass

        elif msg_type == 'l2update':

            pass

        else:

            pass


