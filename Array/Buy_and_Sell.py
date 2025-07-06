def max_profit(prices):
    l,r=0,1
    total_profit=0

    while r<len(prices):
        if prices[l]<prices[r]:
            profit=prices[r]-prices[l]
            total_profit=max(profit,total_profit)
        else:
            l=r
        r += 1
    return total_profit


prices=[8,1,4,7]
result=max_profit(prices)
print(result)

     