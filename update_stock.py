from cassandra.cluster import Cluster
from datetime import datetime

# Connect to Cassandra
cluster = Cluster(['127.0.0.1'], port=9042)
session = cluster.connect()
session.execute("USE StockTracker")

# Update a stock price (using same timestamp as before)
stock_symbol = 'AAPL'

# For simplicity, fetch the latest timestamp for this stock
latest_row = session.execute("""
    SELECT timestamp FROM stock_prices
    WHERE stock_symbol=%s
    LIMIT 1
""", (stock_symbol,)).one()

if latest_row:
    session.execute("""
        UPDATE stock_prices
        SET close=%s
        WHERE stock_symbol=%s AND timestamp=%s
    """, (177.5, stock_symbol, latest_row.timestamp))
    print("✅ Stock price updated successfully!")
else:
    print("No stock data found to update.")
