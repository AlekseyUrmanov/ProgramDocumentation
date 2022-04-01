# Trading Tests and Results 
## SUPER-USD 
  - Total Time
    - 46000 sec
    - ~ 12 hours
    - 4 hours active trading
  - Order Profile
    - 6 orders
    - Quantity of 5 SUPER
    - The program lost 1 order
  - Transaction Summary
    - 105 Transactions / 5 open sells at close
    - 470$ traded in volume
    - ~ 525 SUPER traded
  - Profit Summary
    - 0.02 $ fee per transaction (5 SUPER)
    - ~ assume avg price of 0.89
    - 0.05 profit per round trip (size 5, buy/sell)
    - 0.01 gross profit per full trade : 0.05 - 0.04
    - 55 full trades : 110/2 
    - Profit = 55 * 0.01  = 0.55$
    - Fee less profit = 55 * 0.05 = 2.75$
  - Results
    - .89$ * 30 SUPER = 26.7$ trading value
    - 0.55 / 26.7 = 2.06% return
    - 2.06% return in 12 Hours
    - 2.06% return in 4 Hours of active trading
  - Notes
    - Im not sure why or how the program lost an order. This only happned in the last hour of trading
    - The program has a tendancy to just group all the orders together into one price level. With no time between execution, between each other. I hope to develop some system that will keep orders seperate from each other and reduce the 'clumping' tendancy. 
    - While the total run time of the program was 12 Hours, only 4 of those hours saw trading action. The remaining 8 hours were time intervaal were I was a holding a position 5-10% away from best ask. 
### Proof
[SUPER_USD_TRADES.mov.zip](https://github.com/AlekseyUrmanov/ProgramDocumentation/files/8398129/SUPER_USD_TRADES.mov.zip)
