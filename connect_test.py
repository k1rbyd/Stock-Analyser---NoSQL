from cassandra.cluster import Cluster

# Connect to local Cassandra
cluster = Cluster(['127.0.0.1'], port=9042)
session = cluster.connect()  # no keyspace yet

# Test connection
row = session.execute("SELECT release_version FROM system.local").one()
if row:
    print(f"Connected! Cassandra version: {row.release_version}")
else:
    print("Connection failed.")
