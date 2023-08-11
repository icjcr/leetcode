def calculate_max_profit(prices: list[int]) -> int:
    if len(prices) < 2:
        return 0
    max_profit, buy_price = 0, prices[0]
    for price in prices:
        next_profit = price - buy_price
        if max_profit < next_profit:
            max_profit = price - buy_price
        elif price < buy_price:
            buy_price = price
    return max_profit
