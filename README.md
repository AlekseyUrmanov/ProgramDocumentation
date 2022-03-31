# ProgramDocumentation

## Bot9 functions and variables

### auth()
Generates a public and privte endpoint connection with coinbase servers. Stores these references as variables to be used throughout the program.

## global variables

### order_status_dict = {}
Dictioniary off all open orders, with relative data

### order_book = {}
Unsorted dictionary of prices that exist in the order book, corresponding to liquid quantity at said price level

### orders_at_price = {}
Dictionary of prices that exist in order book, corresponding to sets of order ids that are open at those price levels

### bid_ask_order_book = {}
Dictioniary of prices in order book, corresponding to a 'buy' or 'sell' value: used to identify best bid and ask, without rest API polling

### void_orders_at_price = {}
Dictioniary of prices, of orders, of arrays. Hold the order id of every single order that comes through after an open order has been placed, per individual order, at a variable price level

### order_id_fill_prices = {}
Dictioniary of sell side order ids, with their buy side filled pric, used to determine profitability intervals 

### inventory = []
Stack of all buy side filled orders: LIFO used to determine profitability at time or order match. 

### profit = 0, profit_points = None, accumulated_fees = 0
Basic holding points for fee data and profit

### Order Flow Variables
order_sizes = []
median_order_size = 0
mean_order_size = 0
total_orders = 0
orders_per_min = 0




