from cassandra.cluster import Cluster
from datetime import datetime
import time

# Connect to Cassandra (no keyspace)
cluster = Cluster(['127.0.0.1'], port=9042)
session = cluster.connect()

# Wait a moment to ensure keyspace is ready
time.sleep(1)

# Select the keyspace explicitly
session.execute("USE StockTracker")

# Insert one stock price
session.execute("""
    INSERT INTO stock_prices (stock_symbol, timestamp, open, close, high, low, volume)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
""", ('AAPL', datetime.now(), 175.0, 176.4, 177.0, 174.5, 52340000))

print("✅ Inserted one stock price successfully!")
