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

def time_search_task(arr, task):
    best_time = float('inf')
    best_midpoint = None
    
    midpoints = range(0, len(arr), len(arr) // 1000)
    
    for midpoint in midpoints:
        start_time = time.time()
        binary_search_with_configurable_midpoint(arr, task, midpoint)
        end_time = time.time()
        search_time = end_time - start_time
        
        if search_time < best_time:
            best_time = search_time
            best_midpoint = midpoint
    
    return best_midpoint, best_time

def plot_scatter(tasks):
    task_values = [task['task_value'] for task in tasks]
    chosen_midpoints = [task['best_midpoint'] for task in tasks]
    plt.scatter(task_values, chosen_midpoints)
    plt.xlabel('Task Values')
    plt.ylabel('Bestn Midpoints')
    plt.title('Best Midpoints Vs Task')
    plt.show()

if __name__ == "__main__":
    with open('ex7data.json', 'r') as file:
        arr = json.load(file)


    print("1")
    with open('ex7tasks.json', 'r') as file:
        tasks = json.loads(file.read())

    print("2")
    best_midpoints = []
    for task in tasks:
        best_midpoint, _ = time_search_task(arr, task)
        best_midpoints.append(best_midpoint)
    print("3")
    plt.scatter(tasks, best_midpoints)
    plt.xlabel('Search Tasks')
    plt.ylabel('Best Midpoints')
    plt.title('Best Midpoints vs Search Tasks')
    plt.show()

#4.) Comment on the graph. Does the choice of initial midpoint appear
#    to affect performance? Why do you think is that?

'''The graph shows linear correlation between the tasks and midpoints. The choice of
initial midpoint affects the performance as the algorithm will find the target
(complete the search task) faster if the midpoint is closer to the tartget. The choice of
midpoints increase if the task vals increase.'''
    