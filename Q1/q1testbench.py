import time
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import sorting algorithm classes
from q1 import QuickSort, ThreeWayMergeSort, HeapSort, BucketSort, RadixSortLinkedList


# Helper functions for measuring performance
def measure_performance(sort_class, arr):
    """Measures execution time, swaps, and comparisons of the sorting class."""
    sorter = sort_class()  # Instantiate the sorting class
    start_time = time.time()
    sorted_arr, swaps, comparisons = sorter.sort(arr.copy())
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    return execution_time, swaps, comparisons


def generate_array(size):
    """Generates a random array of the given size."""
    return np.random.randint(0, 10000, size).tolist()


def test_sorting_algorithm(sort_class, sizes):
    """Tests the sorting algorithm and measures performance."""
    times = []
    for size in sizes:
        arr = generate_array(size)

        # Measure performance
        try:
            exec_time, swaps, comparisons = measure_performance(sort_class, arr)
            times.append(exec_time)
            print(f"Size: {size}, Time: {exec_time:.4f} ms, Swaps: {swaps}, Comparisons: {comparisons}")
        except Exception as e:
            print(f"Error sorting array of size {size}: {e}")
            times.append(None)  # Append None to indicate error

    return times


def plot_performance(sizes, times_dict, filename="sorting_performance.png"):
    """Plots performance results using Seaborn and saves the plot to a file."""
    plt.figure(figsize=(12, 8))
    sns.set_theme(style="whitegrid")
    for label, times in times_dict.items():
        plt.plot(sizes, times, marker='o', label=label)

    plt.xlabel('Array Size')
    plt.ylabel('Execution Time (ms)')
    plt.title('Sorting Algorithms Performance')
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    print(f"Plot saved as {filename}")


# Sizes to test
sizes = [100, 500, 1000]

# Test Quick Sort
print("Testing Quick Sort")
quick_sort_times = test_sorting_algorithm(QuickSort, sizes)

# Test 3-Way Merge Sort
print("Testing 3-Way Merge Sort")
merge_sort_times = test_sorting_algorithm(ThreeWayMergeSort, sizes)

# Test Heap Sort
print("Testing Heap Sort")
heap_sort_times = test_sorting_algorithm(HeapSort, sizes)

# Test Bucket Sort
print("Testing Bucket Sort")
bucket_sort_times = test_sorting_algorithm(BucketSort, sizes)

# Test Radix Sort
print("Testing Radix Sort")

def radix_sort_test(arr):
    """Wraps RadixSortLinkedList class for testing."""
    if len(arr) > 25:
        return arr  # Avoid testing with large sizes
    linked_list = RadixSortLinkedList.LinkedList()
    for num in arr:
        linked_list.append(num)
    sorted_linked_list = RadixSortLinkedList().sort(linked_list)
    return sorted_linked_list.to_list()

radix_sort_times = test_sorting_algorithm(lambda arr, sizes=sizes: radix_sort_test(arr), sizes=sizes)

# Plot the performance results
times_dict = {
    'Quick Sort': quick_sort_times,
    '3-Way Merge Sort': merge_sort_times,
    'Heap Sort': heap_sort_times,
    'Bucket Sort': bucket_sort_times,
    'Radix Sort': radix_sort_times
}

plot_performance(sizes, times_dict)
