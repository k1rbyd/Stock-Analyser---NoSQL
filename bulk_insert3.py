from cassandra.cluster import Cluster
from datetime import datetime, timedelta
import random

# Connect to Cassandra
cluster = Cluster(['127.0.0.1'], port=9042)
session = cluster.connect()
session.execute("USE StockTracker")

stocks = ['AAPL', 'GOOG', 'TSLA', 'GME']
days = 365  # one full year

print("⏳ Inserting 1-year stock data for multiple companies...")

for stock_symbol in stocks:
    base_date = datetime.now() - timedelta(days=days)
    for i in range(days):
        date = base_date + timedelta(days=i)
        
        # Set realistic base prices
        base_price = {
            'AAPL': 170,
            'GOOG': 2800,
            'TSLA': 250,
            'GME': 40
        }[stock_symbol]

        # Add volatility logic
        if stock_symbol == 'GME':
            # wild random spikes and drops
            change_factor = random.uniform(-0.4, 0.4)
            open_price = round(base_price * (1 + change_factor), 2)
            close_price = round(open_price * (1 + random.uniform(-0.5, 0.5)), 2)
            high_price = max(open_price, close_price) * (1 + random.uniform(0, 0.3))
            low_price = min(open_price, close_price) * (1 - random.uniform(0, 0.3))
            volume = random.randint(500000, 50000000)
        else:
            open_price = round(base_price + random.uniform(-15, 15), 2)
            close_price = round(open_price + random.uniform(-8, 8), 2)
            high_price = max(open_price, close_price) + round(random.uniform(0, 8), 2)
            low_price = min(open_price, close_price) - round(random.uniform(0, 8), 2)
            volume = random.randint(3000000, 15000000)

        # Insert record
        session.execute("""
            INSERT INTO stock_prices (stock_symbol, timestamp, open, close, high, low, volume)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (stock_symbol, date, open_price, close_price, high_price, low_price, volume))

print("✅ Bulk insert for 1 year of data (4 stocks) completed successfully!")
