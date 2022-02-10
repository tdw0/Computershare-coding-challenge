# read file
txt = open("test.txt", "r")
prices = txt.read().split(',')
prices = list(map(float, prices)) # string to float
txt.close()

# init variables
buy_price = prices[0]
sell_price = prices[1]
profit = sell_price - buy_price
index_buy = 0
index_sell = 0

for i in range(0, len(prices)):
    for j in range(i+1, len(prices)):
        if prices[j] - prices[i] > profit:
            profit      = prices[j] - prices[i]
            buy_price   = prices[i]
            sell_price  = prices[j]
            index_buy   = i + 1
            index_sell  = j + 1
    

print ("{}({}),{}({})".format(index_buy, buy_price, index_sell, sell_price))
