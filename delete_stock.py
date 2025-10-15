from cassandra.cluster import Cluster

# Connect to Cassandra
cluster = Cluster(['127.0.0.1'], port=9042)
session = cluster.connect()
session.execute("USE StockTracker")

# Delete a stock price (latest row for AAPL)
stock_symbol = 'AAPL'

# Fetch latest timestamp
latest_row = session.execute("""
    SELECT timestamp FROM stock_prices
    WHERE stock_symbol=%s
    LIMIT 1
""", (stock_symbol,)).one()

if latest_row:
    session.execute("""
        DELETE FROM stock_prices
        WHERE stock_symbol=%s AND timestamp=%s
    """, (stock_symbol, latest_row.timestamp))
    print("✅ Latest stock price deleted successfully!")
else:
    print("No stock data found to delete.")
