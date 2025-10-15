from cassandra.cluster import Cluster
from datetime import datetime, timedelta
import random

# Connect to Cassandra
cluster = Cluster(['127.0.0.1'], port=9042)
session = cluster.connect()
session.execute("USE StockTracker")

# Simulate 7 days of stock prices
stock_symbol = 'AAPL'
base_date = datetime.now() - timedelta(days=7)

for i in range(7):
    date = base_date + timedelta(days=i)
    open_price = round(170 + random.uniform(-5, 5), 2)
    close_price = round(open_price + random.uniform(-2, 2), 2)
    high_price = max(open_price, close_price) + round(random.uniform(0, 2), 2)
    low_price = min(open_price, close_price) - round(random.uniform(0, 2), 2)
    volume = random.randint(5000000, 10000000)

    session.execute("""
        INSERT INTO stock_prices (stock_symbol, timestamp, open, close, high, low, volume)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (stock_symbol, date, open_price, close_price, high_price, low_price, volume))

print("✅ Bulk insert completed!")
