from cassandra.cluster import Cluster
from datetime import datetime, timedelta
import random

# Connect to Cassandra
cluster = Cluster(['127.0.0.1'], port=9042)
session = cluster.connect()
session.execute("USE StockTracker")

stocks = ['AAPL', 'GOOG', 'TSLA']
days = 365  # one full year

print("⏳ Inserting 1-year stock data for multiple companies...")

for stock_symbol in stocks:
    base_date = datetime.now() - timedelta(days=days)
    for i in range(days):
        date = base_date + timedelta(days=i)
        
        # realistic base prices
        base_price = {
            'AAPL': 170,
            'GOOG': 2800,
            'TSLA': 250
        }[stock_symbol]

        # simulate daily variations
        open_price = round(base_price + random.uniform(-15, 15), 2)
        close_price = round(open_price + random.uniform(-8, 8), 2)
        high_price = max(open_price, close_price) + round(random.uniform(0, 8), 2)
        low_price = min(open_price, close_price) - round(random.uniform(0, 8), 2)
        volume = random.randint(3000000, 15000000)

        session.execute("""
            INSERT INTO stock_prices (stock_symbol, timestamp, open, close, high, low, volume)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (stock_symbol, date, open_price, close_price, high_price, low_price, volume))

print("✅ Bulk insert for 1 year of data (3 stocks) completed successfully!")
