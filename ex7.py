import matplotlib.pyplot as plt
import json
import time

def binary_search_with_configurable_midpoint(arr, target, initial_midpoint):
    start = 0
    end = len(arr) - 1
    mid = initial_midpoint
    
    while (start <= end):
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
        
        mid = (start + end) // 2
    
    return -1

def measure_performance(arr, tasks):
    performance_data = []
    
    for target in tasks:
        midpoints = [target]  # Each task value itself serves as a midpoint
        best_time = float('inf')
        best_midpoint = None
        
        for midpoint in midpoints:
            start_time = time.time()
            result = binary_search_with_configurable_midpoint(arr, target, midpoint)
            end_time = time.time()
            elapsed_time = end_time - start_time
            
            if elapsed_time < best_time:
                best_time = elapsed_time
                best_midpoint = midpoint
        
        performance_data.append({'task_value': target, 'best_midpoint': best_midpoint})
        print(f"Task: {target}, Best Midpoint: {best_midpoint}, Time: {best_time} seconds")
    
    return performance_data

def plot_scatter(tasks):
    task_values = [task['task_value'] for task in tasks]
    chosen_midpoints = [task['best_midpoint'] for task in tasks]
    plt.scatter(task_values, chosen_midpoints)
    plt.xlabel('Task Values')
    plt.ylabel('Chosen Midpoints')
    plt.title('Chosen Midpoints for Each Task')
    plt.show()

if __name__ == "__main__":
    with open('ex7data.json', 'r') as file:
        data = json.load(file)
        arr = data  # where arr is an integer array

    with open('ex7tasks.json', 'r') as file:
        tasks = json.loads(file.read())

    performance_data = measure_performance(arr, tasks)
    plot_scatter(performance_data)

    
# there is a linear relationship between the task values 
# and the chosen midpoints, it suggests that the choice of midpoint has a consistent 
# and predictable impact on performance across different tasks, this is because as the task values increase
# the midpoints will also increase indicating  that the performance of the binary search algorithm 
# is directly influenced by the task values and the choice of initial midpoint