from cassandra.cluster import Cluster
import pandas as pd
import matplotlib.pyplot as plt

# Connect
cluster = Cluster(['127.0.0.1'], port=9042)
session = cluster.connect()
session.execute("USE StockTracker")

stocks = ['AAPL', 'GOOG', 'TSLA', 'GME']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # blue, orange, green, red

plt.figure(figsize=(14,7))

for stock, color in zip(stocks, colors):
    rows = session.execute(
        "SELECT timestamp, close FROM stock_prices WHERE stock_symbol=%s", (stock,)
    )
    data = pd.DataFrame([(row.timestamp, row.close) for row in rows], columns=['Date', 'Close'])
    data = data.sort_values('Date')
    plt.plot(data['Date'], data['Close'], label=stock, color=color, linewidth=2)

plt.title("1-Year Stock Price Trends", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Closing Price (USD)", fontsize=12)
plt.legend(title="Stock Symbol")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
