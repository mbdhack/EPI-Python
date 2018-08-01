from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    min_price_so_far,max_profit = float('inf'),0
    for price in prices:
        max_profit_for_now = price-min_price_so_far
        min_price_so_far = min(price,min_price_so_far)
        max_profit = max(max_profit_for_now,max_profit)
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
