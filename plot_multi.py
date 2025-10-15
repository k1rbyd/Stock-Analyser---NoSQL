from cassandra.cluster import Cluster
import pandas as pd
import matplotlib.pyplot as plt

# Connect to Cassandra
cluster = Cluster(['127.0.0.1'], port=9042)
session = cluster.connect()
session.execute("USE StockTracker")

stocks = ['AAPL', 'GOOG', 'TSLA']
plt.figure(figsize=(14,7))

for stock in stocks:
    rows = session.execute("SELECT timestamp, close FROM stock_prices WHERE stock_symbol=%s", (stock,))
    data = pd.DataFrame([(row.timestamp, row.close) for row in rows], columns=['Date', 'Close'])
    data = data.sort_values('Date')
    plt.plot(data['Date'], data['Close'], label=stock)

plt.title("📈 1-Year Stock Price Trend (AAPL, GOOG, TSLA)")
plt.xlabel("Date")
plt.ylabel("Closing Price (USD)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
