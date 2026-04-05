# Task Scheduler Simulation using Shortest Job First (SJF)
# Concepts: Priority Queue, Time Optimization

import heapq

class Task:
    def __init__(self, id, arrival, burst):
        self.id = id
        self.arrival = arrival
        self.burst = burst

# Sample input tasks
tasks = [
    Task(1, 0, 5),
    Task(2, 1, 3),
    Task(3, 2, 8),
    Task(4, 3, 6)
]

# Sort tasks based on arrival time
tasks.sort(key=lambda x: x.arrival)

# Priority Queue (min-heap based on burst time)
pq = []

time = 0
i = 0
n = len(tasks)

waiting_time = 0
turnaround_time = 0

print("\nExecution Order:\n")

while i < n or pq:

    # Add all tasks that have arrived to the queue
    while i < n and tasks[i].arrival <= time:
        heapq.heappush(pq, (tasks[i].burst, tasks[i]))
        i += 1

    if pq:
        burst, task = heapq.heappop(pq)

        start_time = time
        time += burst

        wait = start_time - task.arrival
        tat = time - task.arrival

        waiting_time += wait
        turnaround_time += tat

        print(f"Task {task.id} -> Start: {start_time}, End: {time}, Waiting: {wait}, Turnaround: {tat}")

    else:
        # If no task is available, move time forward
        time += 1

# Averages
print("\nAverage Waiting Time:", waiting_time / n)
print("Average Turnaround Time:", turnaround_time / n)