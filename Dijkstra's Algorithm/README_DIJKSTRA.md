# 🚀 Dijkstra’s Algorithm (Uniform Cost Search) for Indian Cities

## 📌 Overview

This project implements **Dijkstra’s Algorithm**, also known as **Uniform Cost Search (UCS)** in Artificial Intelligence, to find the shortest path between cities in India based on road distances.

The algorithm computes the minimum distance from a given source city to all other cities in the graph.

---

## 🧠 Concept

* Each **city** is represented as a **node**
* Each **road** is represented as an **edge with cost (distance in km)**
* The algorithm always expands the **lowest-cost path first**
* It guarantees the **shortest path** in a weighted graph with non-negative edges

---

## 🗂️ Project Structure

```
dijkstra_india.py   # Main Python implementation
README.md           # Project documentation
```

---

## ⚙️ Requirements

* Python 3.x
* No external libraries required (uses built-in `heapq`)

---

## ▶️ How to Run (Ubuntu)

1. Open Terminal

   ```
   Ctrl + Alt + T
   ```

2. Navigate to the file location

   ```
   cd <your-folder-path>
   ```

3. Run the program

   ```
   python3 dijkstra_india.py
   ```

---

## 📥 Sample Input

The graph is predefined in the code using a dictionary:

```
"Delhi": [("Agra", 233), ("Jaipur", 280)]
```

You can modify or extend this dataset by adding more cities and distances.

---

## 📤 Sample Output

```
Shortest distances from Delhi:

Agra: 233 km
Jaipur: 280 km
...

Shortest path from Delhi to Chennai:
Delhi -> Jaipur -> Mumbai -> Pune -> Bangalore -> Chennai
Total distance: XXXX km
```

---

## 🔍 Algorithm Steps

1. Initialize all distances as infinity
2. Set source city distance to 0
3. Use a **priority queue (min-heap)**
4. Pick the city with the smallest distance
5. Update distances of neighboring cities
6. Repeat until all nodes are visited

---

## 💡 Features

* Finds shortest distance to all cities
* Displays shortest path between two cities
* Efficient implementation using priority queue
* Easy to extend with more data

---

## 🚧 Future Improvements

* Load real-world data from CSV or API
* Add user input for source and destination
* Visualize graph using libraries like NetworkX
* GUI-based implementation

---

## 📚 Applications

* GPS Navigation systems
* Network routing
* Transportation planning
* AI pathfinding problems

---