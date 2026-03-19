# 🚗 Unmanned Ground Vehicle (UGV) Path Planning using A* Algorithm

## 📌 Overview

This project simulates an **Unmanned Ground Vehicle (UGV)** navigating a battlefield represented as a **70×70 grid**.
The UGV finds the **shortest path** from a start node to a goal node while avoiding obstacles using the **A* (A-Star) search algorithm**.

---

## 🎯 Objectives

* Implement pathfinding in a grid-based environment
* Avoid known obstacles
* Compute the **optimal (shortest) path**
* Evaluate performance using different obstacle densities

---

## 🧠 Algorithm Used

### A* Search Algorithm

A* is an informed search algorithm that finds the shortest path using:

* **g(n)** → cost from start node
* **h(n)** → heuristic (estimated cost to goal)

### Heuristic Used:

* **Manhattan Distance**

```
h(n) = |x1 - x2| + |y1 - y2|
```

---

## 🗺️ Grid Representation

* `0` → Free space
* `1` → Obstacle
* `2` → Path taken by UGV

---

## ⚙️ Features

* Configurable obstacle density:

  * Low (0.1)
  * Medium (0.3)
  * High (0.5)
* Automatically generates random obstacles
* Computes shortest path
* Displays execution time and path length

---

## 📊 Measures of Effectiveness

The performance of the algorithm is evaluated using:

1. **Path Length**

   * Number of steps from start to goal

2. **Execution Time**

   * Time taken to compute the path

3. **Success Rate**

   * Whether a valid path is found

4. **Nodes Explored (implicit)**

   * Indicates algorithm efficiency

---

## ▶️ How to Run

### Step 1: Install Python

Make sure Python 3 is installed:

```
python3 --version
```

### Step 2: Install NumPy (if required)

```
pip3 install numpy --break-system-packages
```

### Step 3: Run the Program

```
python3 UGV.py
```

### Step 4: Input

Enter obstacle density when prompted:

```
0.1  OR  0.3  OR  0.5
```

---

## 🧾 Sample Output

```
Enter obstacle density: 0.3

Path found!
Path length: 138
Time taken: 0.02 seconds
```

Grid output:

```
0 = free space
1 = obstacle
2 = path
```

---

## ❌ Possible Case

If no valid path exists:

```
No path found!
```

---

## 🚀 Observations

* Low obstacle density → faster execution and shorter path
* High obstacle density → increased complexity and possible failure
* A* performs efficiently due to heuristic guidance

---

## 🛠️ Technologies Used

* Python 3
* NumPy (optional)
* Heap Queue (priority queue)

---

## 📌 Conclusion

The A* algorithm effectively enables the UGV to navigate through a grid with obstacles while ensuring the shortest path. It is suitable for real-time path planning applications in robotics and AI.

---
