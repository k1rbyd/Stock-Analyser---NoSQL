from cassandra.cluster import Cluster

# Connect to Cassandra
cluster = Cluster(['127.0.0.1'], port=9042)
session = cluster.connect()
session.execute("USE StockTracker")

# Fetch all prices for a stock
stock_symbol = 'AAPL'
rows = session.execute("""
    SELECT * FROM stock_prices
    WHERE stock_symbol=%s
""", (stock_symbol,))

# Print results
for row in rows:
    print(f"Time: {row.timestamp}, Open: {row.open}, Close: {row.close}, High: {row.high}, Low: {row.low}, Volume: {row.volume}")
