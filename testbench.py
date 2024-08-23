import time
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import sorting algorithms
from q1 import quick_sort, mergeSort3Way, heapSort, bucket_sort, radix_sort_linked_list, LinkedList


# Helper functions for measuring performance
def measure_performance(sort_function, arr):
    """Measures execution time of the sorting function."""
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    return execution_time


def generate_array(size):
    """Generates a random array of the given size."""
    return np.random.randint(0, 10000, size).tolist()


def test_sorting_algorithm(sort_function, sizes):
    """Tests the sorting algorithm and measures performance."""
    times = []
    for size in sizes:
        arr = generate_array(size)

        # Measure performance
        try:
            exec_time = measure_performance(sort_function, arr.copy())
            times.append(exec_time)
            print(f"Size: {size}, Time: {exec_time:.4f} ms")
        except Exception as e:
            print(f"Error sorting array of size {size}: {e}")
            times.append(None)  # Append None to indicate error

    return times


def plot_performance(sizes, times_dict):
    """Plots performance results using Seaborn."""
    plt.figure(figsize=(12, 8))
    sns.set_theme(style="whitegrid")  # Use set_theme instead of set
    for label, times in times_dict.items():
        plt.plot(sizes, times, marker='o', label=label)

    plt.xlabel('Array Size')
    plt.ylabel('Execution Time (ms)')
    plt.title('Sorting Algorithms Performance')
    plt.legend()
    plt.grid(True)
    plt.show()


# Sizes to test
sizes = [100, 500, 1000]

# Test Quick Sort
print("Testing Quick Sort")
quick_sort_times = test_sorting_algorithm(lambda arr: quick_sort(arr, 0, len(arr) - 1), sizes)

# Test 3-Way Merge Sort
print("Testing 3-Way Merge Sort")
merge_sort_times = test_sorting_algorithm(lambda arr: mergeSort3Way(arr, len(arr)), sizes)

# Test Heap Sort
print("Testing Heap Sort")
heap_sort_times = test_sorting_algorithm(heapSort, sizes)

# Test Bucket Sort
print("Testing Bucket Sort")
bucket_sort_times = test_sorting_algorithm(bucket_sort, sizes)

# Test Radix Sort
print("Testing Radix Sort")


def radix_sort_test(arr):
    """Wraps radix_sort_linked_list for testing."""
    linked_list = LinkedList()
    for num in arr:
        linked_list.append(num)
    sorted_linked_list = radix_sort_linked_list(linked_list)
    return sorted_linked_list.to_list()


radix_sort_times = test_sorting_algorithm(lambda arr: radix_sort_test(arr), sizes)

# Plot the performance results
times_dict = {
    'Quick Sort': quick_sort_times,
    '3-Way Merge Sort': merge_sort_times,
    'Heap Sort': heap_sort_times,
    'Bucket Sort': bucket_sort_times,
    'Radix Sort': radix_sort_times
}

plot_performance(sizes, times_dict)
