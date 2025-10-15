# Real-Time Traffic Monitoring and Congestion Analysis using MongoDB

## Objective
To demonstrate the key NoSQL features of MongoDB — flexibility, scalability, and document-based storage — through a real-time traffic monitoring and congestion analysis system.

---

## NoSQL Feature Demonstrated

- **Document-Based Data Model:** Stores traffic data (vehicle counts, speed, and timestamps) in flexible JSON-like documents.  
- **Real-Time Updates:** Supports continuous insertion and updates of live traffic feed data.  
- **Horizontal Scalability:** Easily scales across multiple nodes for large-scale city-wide traffic networks.  
- **Aggregation Framework:** Enables efficient querying and analysis of traffic congestion patterns over time.  

---

## Tools and Technologies Used

- **Database:** MongoDB 7.0  
- **Language:** Python  
- **Libraries:** `pymongo`, `matplotlib`, `pandas`, `datetime`  
- **Environment:** macOS (Kaushik’s MacBook Air, M3)  

---

## Setup Instructions

### 1. Install MongoDB
```
brew tap mongodb/brew  
brew install mongodb-community@7.0  
brew services start mongodb-community@7.0
```
sad
```
sad
```

### 2. Set Up Python Virtual Environment
```
python3 -m venv venv  
source venv/bin/activate
```

### 3. Install Dependencies
```
pip install pymongo matplotlib pandas
```

### 4. Run the Database Setup Script
```
python setup_db.py
```

### 5. Insert Live Traffic Data
```
python insert___.py <proper file name>
```

### 6. Visualize Congestion Trends
```
python plot___.py <proper file name>
```

## Result

The project demonstrates MongoDB’s capability to:
  Handle real-time, unstructured traffic data streams
  Perform efficient queries for route- or time-based congestion analysis
  Visualize and analyze congestion trends dynamically

## Conclusion

This project showcases how MongoDB effectively manages dynamic, high-velocity IoT and traffic sensor data while maintaining flexibility and horizontal scalability.
It highlights the advantages of NoSQL databases in real-time analytics and smart city infrastructure management.
