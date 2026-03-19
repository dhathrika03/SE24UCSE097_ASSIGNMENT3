# 🚗 Dynamic UGV Pathfinding using A* (Replanning)

## 📌 Overview

This project implements a **dynamic pathfinding algorithm** for an Unmanned Ground Vehicle (UGV) navigating a grid-based environment with **dynamic obstacles**.

Unlike traditional pathfinding where obstacles are static and known beforehand, this system simulates a **real-world environment** where obstacles can **appear randomly during movement**. The UGV continuously replans its path using the **A* algorithm**.

---

## 🧠 Key Concepts

* **A* Search Algorithm**
* **Dynamic Environment Handling**
* **Replanning Strategy (Online Planning)**
* **Grid-based Navigation**

---

## ⚙️ How It Works

1. The environment is represented as a **2D grid**.
2. The UGV starts at a given **start position** and aims to reach the **goal position**.
3. Initially, the grid has no obstacles.
4. At each step:

   * A path is computed using **A***.
   * The UGV moves **one step forward**.
   * New obstacles are randomly introduced into the grid.
   * The path is recalculated if needed.
5. This process continues until:

   * The goal is reached ✅
   * OR no valid path exists ❌

---

## 🗂️ File Structure

```
dynamic_ugv_pathfinding.py   # Main Python script
README.md                    # Project documentation
```

---

## ▶️ How to Run

### 1. Save the file

Save the Python code as:

```
dynamic_ugv_pathfinding.py
```

### 2. Open terminal / command prompt

Navigate to the file location:

```
cd path_to_your_file
```

### 3. Run the program

```
python dynamic_ugv_pathfinding.py
```

---

## 🖥️ Output Explanation

The program prints the grid after each step.

### Symbols Used:

| Symbol | Meaning           |
| ------ | ----------------- |
| `.`    | Free space        |
| `#`    | Obstacle          |
| `P`    | Path taken by UGV |

---

### Example Output:

```
Replanning from: (0, 0)

. . . . . . . . . .
. # . . . . . # . .
. . . . # . . . . .
. . . . . . . . . .
...
```

---

## ⚡ Features

* Handles **dynamic obstacles**
* Uses **heuristic-based optimal search (A*)**
* Demonstrates **real-time replanning**
* Simple and easy-to-understand implementation

---

## ⚠️ Limitations

* Obstacles are added **randomly**, not based on real sensor data
* May sometimes result in **no available path**
* Not optimized for large-scale maps

---

## 🚀 Future Improvements

* Implement **D* Lite algorithm** for faster replanning
* Add **visual animation using matplotlib**
* Integrate **sensor simulation (LIDAR, camera)**
* Expand to larger and more complex environments

---

## 🧾 Conclusion

This project demonstrates how a UGV can navigate in a **dynamic and uncertain environment** by continuously updating its path using the **A* algorithm with replanning**.

It highlights the importance of **adaptive decision-making** in real-world robotics applications.

---