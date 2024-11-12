import time
import random

# Function for Deterministic QuickSort
def deterministic_quicksort(arr):
    # Base case: if the array has 0 or 1 elements, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose the pivot (the last element in this case)
    pivot = arr[-1]
    
    # Partition the array into two halves: less and greater
    less = [x for x in arr[:-1] if x <= pivot]
    greater = [x for x in arr[:-1] if x > pivot]
    
    # Recursively sort the partitions and concatenate the results
    return deterministic_quicksort(less) + [pivot] + deterministic_quicksort(greater)

# Function for Randomized QuickSort
def randomized_quicksort(arr):
    # Base case: if the array has 0 or 1 elements, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose a random pivot
    pivot = arr[random.randint(0, len(arr) - 1)]
    
    # Partition the array into three parts: less, equal, and greater
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    
    # Recursively sort the less and greater partitions and concatenate the results
    return randomized_quicksort(less) + equal + randomized_quicksort(greater)

# Function to measure the time taken by a sorting function
def measure_time(sort_func, arr):
    start = time.time()  # Record the start time
    sorted_arr = sort_func(arr)  # Sort the array using the specified sorting function
    end = time.time()  # Record the end time
    return end - start  # Calculate the time difference

# Generate a random list of numbers
arr = [random.randint(1, 10000) for _ in range(1000)]

# Measure time taken by deterministic quicksort
time_det = measure_time(deterministic_quicksort, arr.copy())
print(f"Deterministic Quick Sort Time: {time_det:.6f} seconds")

# Measure time taken by randomized quicksort
time_rand = measure_time(randomized_quicksort, arr.copy())
print(f"Randomized Quick Sort Time: {time_rand:.6f} seconds")