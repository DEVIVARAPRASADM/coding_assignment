def minimize_loss(prices):
    indexed_prices = [(price, idx) for idx, price in enumerate(prices)]
    sorted_prices = sorted(indexed_prices)

    min_loss = float('inf')
    buy_year = sell_year = -1

    for i in range(len(sorted_prices) - 1, 0, -1):
        high_price, high_idx = sorted_prices[i]
        low_price, low_idx = sorted_prices[i - 1]

        if high_idx < low_idx:
            loss = high_price - low_price
            if 0 < loss < min_loss:
                min_loss = loss
                buy_year = high_idx + 1
                sell_year = low_idx + 1

    return (buy_year, sell_year, min_loss if min_loss != float('inf') else -1)

prices = [20, 15, 7, 2, 13]
buy_year, sell_year, loss = minimize_loss(prices)
print(f"Buy in Year {buy_year}, Sell in Year {sell_year}, Loss: {loss}")
