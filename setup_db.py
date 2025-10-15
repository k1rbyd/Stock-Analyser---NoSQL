from cassandra.cluster import Cluster
import time

# Connect to Cassandra (no keyspace yet)
cluster = Cluster(['127.0.0.1'], port=9042)
session = cluster.connect()

# Create keyspace
session.execute("""
    CREATE KEYSPACE IF NOT EXISTS StockTracker
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}
""")

# Wait a tiny bit for Cassandra to register keyspace
time.sleep(1)

# Use the keyspace via query (safer than set_keyspace)
session.execute("USE StockTracker")

# Create table
session.execute("""
    CREATE TABLE IF NOT EXISTS stock_prices (
        stock_symbol text,
        timestamp timestamp,
        open float,
        close float,
        high float,
        low float,
        volume bigint,
        PRIMARY KEY (stock_symbol, timestamp)
    ) WITH CLUSTERING ORDER BY (timestamp DESC)
""")

print("✅ Keyspace and table created successfully!")
