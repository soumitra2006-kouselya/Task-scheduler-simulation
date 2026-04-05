# Task-scheduler-simulation
Task Scheduler Simulation using Priority Queue (SJF) with optimized execution and time complexity analysis
# Task Scheduler Simulation System

##  Overview
This project simulates CPU scheduling using optimization techniques.

##  Features
- Shortest Job First (SJF) algorithm
- Priority Queue implementation
- Waiting time and turnaround time calculation

##  Concepts Used
- Data Structures (Heap / Priority Queue)
- Time Complexity Optimization
- Algorithm Design

##  How to Run
```bash
python scheduler.py

## Sample Output

Task 1 -> Start: 0, End: 5, Waiting: 0, Turnaround: 5  
Task 2 -> Start: 5, End: 8, Waiting: 4, Turnaround: 7  
Task 4 -> Start: 8, End: 14, Waiting: 5, Turnaround: 11  
Task 3 -> Start: 14, End: 22, Waiting: 12, Turnaround: 20  

Average Waiting Time: 5.25  
Average Turnaround Time: 10.75  
