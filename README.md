# ProgramDocumentation

### About
As implied by the name *Bot9* is the nineth edition of my trading bot. It has major efficiency improvements over previous versions and many new functions. 

**fundamentals**
  - The program is *not* object orientated. Though some components are classes. This program is procedure based. It needs to be simple and quick. Thats why all important data types are stored in dictionaries and all processess are simple functions. Dictionary data types serve for direct access to variables, and function 6 times faster than lists. 
  - Depending on conditions and parameters. Dictionaries will hold 15,000 - 20,000 entries, with embeded dictionaries. In certain conditions, the data stream may overflow processing capabilities of the program. The program can only trade one crypto pair. Furture versions of the program will convert the program into a class so multiple instances can be run. 
  - Depending on the instance, the program may or may not be profitable. On high frequency pairs, which is the running design of the program. It is extremely unprofitable due to transaction fees. Disregarding fees, and assuming a fluctuating market, data has shown that it makes 0.3% returns every 10-20minutes. Howevere, fees will be 10x larger than profit. *preliminary estimates*

**strategy**
  - The main logic of the program is to determine a safe and target price, based on order flow and avaliable liquidity. Then, our goal is to sell our inventory as fast as possible at the best ask price. We only post orders to the LOB and we cycle replace them to the target prices we calculate. 

  We track the mean, median and standard deviation of order sizes. We also track the quantity of orders that come through for some time interval. To understand why we don't want to be placing orders at the best bid price. We have to understand the nature of order flow. Order flow comes in chunks, of 4-5 orders, sometimes its cyclical, sometimes there is a linear sell off, or buy in. When this chunk of orders comes in, it will usually wipe out an X amount of liquidity from the LOB. Which will correlate to some amount Y, of price tiers transferring from buy side to sell side. Imagine this quantity of orders as square that moves up and down a number line. Let our open position represent a horizontal line in that square. If our open position is at the best bid, a line at the top of the square, a large order comes through (X) and pushes the entire square into the sell side, by quantity (Y). The best ask is now a point at the bottom of the square, and our order, which needs to be placed at some price point that would set us to be profitable, is at the top of the square. Instead, to ensure that our sell order is around the best ask, we want to hold our buy order a few price tiers bellow the best bid so it executes and flips into a favorable position
  
