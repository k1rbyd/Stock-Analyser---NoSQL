from cassandra.cluster import Cluster
import pandas as pd
import matplotlib.pyplot as plt

# Connect to Cassandra
cluster = Cluster(['127.0.0.1'], port=9042)
session = cluster.connect()
session.execute("USE StockTracker")

# Fetch all rows for AAPL
rows = session.execute("SELECT timestamp, close FROM stock_prices WHERE stock_symbol=%s", ('AAPL',))

# Convert to pandas DataFrame
data = pd.DataFrame([(row.timestamp, row.close) for row in rows], columns=['Date', 'Close'])
data = data.sort_values('Date')

# Plot
plt.figure(figsize=(10,5))
plt.plot(data['Date'], data['Close'], marker='o', linestyle='-', color='blue')
plt.title('AAPL Closing Price Trend')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.grid(True)
plt.tight_layout()
plt.show()
