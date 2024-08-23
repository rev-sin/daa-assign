"""
References from:
Quick Sort - https://www.geeksforgeeks.org/quick-sort-algorithm/
3-Way Merge Sort - https://www.geeksforgeeks.org/3-way-merge-sort/
Heap Sort - https://www.geeksforgeeks.org/heap-sort/
Bucket Sort - https://www.geeksforgeeks.org/bucket-sort-in-python/
Radix Sort - https://www.geeksforgeeks.org/radix-sort/
"""

class QuickSort:
    def __init__(self):
        self.swaps = 0
        self.comparisons = 0

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            self.comparisons += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                self.swaps += 1

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        self.swaps += 1
        return i + 1

    def quick_sort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)

    def sort(self, arr):
        self.quick_sort(arr, 0, len(arr) - 1)
        return arr, self.swaps, self.comparisons

class ThreeWayMergeSort:
    def __init__(self):
        self.swaps = 0
        self.comparisons = 0

    def merge(self, gArray, low, mid1, mid2, high, destArray):
        i, j, k, l = low, mid1, mid2, low

        while i < mid1 and j < mid2 and k < high:
            self.comparisons += 2
            if gArray[i] < gArray[j]:
                if gArray[i] < gArray[k]:
                    destArray[l] = gArray[i]
                    i += 1
                else:
                    destArray[l] = gArray[k]
                    k += 1
            else:
                if gArray[j] < gArray[k]:
                    destArray[l] = gArray[j]
                    j += 1
                else:
                    destArray[l] = gArray[k]
                    k += 1
            l += 1

        while i < mid1 and j < mid2:
            self.comparisons += 1
            if gArray[i] < gArray[j]:
                destArray[l] = gArray[i]
                i += 1
            else:
                destArray[l] = gArray[j]
                j += 1
            l += 1

        while j < mid2 and k < high:
            self.comparisons += 1
            if gArray[j] < gArray[k]:
                destArray[l] = gArray[j]
                j += 1
            else:
                destArray[l] = gArray[k]
                k += 1
            l += 1

        while i < mid1 and k < high:
            self.comparisons += 1
            if gArray[i] < gArray[k]:
                destArray[l] = gArray[i]
                i += 1
            else:
                destArray[l] = gArray[k]
                k += 1
            l += 1

        while i < mid1:
            destArray[l] = gArray[i]
            i += 1
            l += 1

        while j < mid2:
            destArray[l] = gArray[j]
            j += 1
            l += 1

        while k < high:
            destArray[l] = gArray[k]
            k += 1
            l += 1

    def mergeSort3WayRec(self, gArray, low, high, destArray):
        if high - low < 2:
            return

        mid1 = low + ((high - low) // 3)
        mid2 = low + 2 * ((high - low) // 3) + 1

        self.mergeSort3WayRec(destArray, low, mid1, gArray)
        self.mergeSort3WayRec(destArray, mid1, mid2, gArray)
        self.mergeSort3WayRec(destArray, mid2, high, gArray)

        self.merge(destArray, low, mid1, mid2, high, gArray)

    def sort(self, gArray):
        n = len(gArray)
        if n == 0:
            return gArray, self.swaps, self.comparisons

        fArray = gArray.copy()
        self.mergeSort3WayRec(fArray, 0, n, gArray)
        gArray = fArray.copy()
        return gArray, self.swaps, self.comparisons

class HeapSort:
    def __init__(self):
        self.swaps = 0
        self.comparisons = 0

    def heapify(self, arr, N, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        self.comparisons += 1
        if l < N and arr[largest] < arr[l]:
            largest = l

        self.comparisons += 1
        if r < N and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.swaps += 1
            self.heapify(arr, N, largest)

    def sort(self, arr):
        N = len(arr)
        for i in range(N//2 - 1, -1, -1):
            self.heapify(arr, N, i)

        for i in range(N-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.swaps += 1
            self.heapify(arr, i, 0)

        return arr, self.swaps, self.comparisons

class BucketSort:
    def __init__(self):
        self.swaps = 0
        self.comparisons = 0

    def insertion_sort(self, bucket):
        for i in range(1, len(bucket)):
            key = bucket[i]
            j = i - 1
            while j >= 0 and bucket[j] > key:
                self.comparisons += 1
                bucket[j + 1] = bucket[j]
                j -= 1
                self.swaps += 1
            bucket[j + 1] = key

    def sort(self, arr):
        n = len(arr)
        if n <= 1:
            return arr, self.swaps, self.comparisons

        max_val = max(arr)
        buckets = [[] for _ in range(n)]

        for num in arr:
            bi = min(int(n * num / (max_val + 1)), n - 1)
            buckets[bi].append(num)

        for bucket in buckets:
            self.insertion_sort(bucket)

        index = 0
        for bucket in buckets:
            for num in bucket:
                arr[index] = num
                index += 1

        return arr, self.swaps, self.comparisons

class RadixSortLinkedList:
    def __init__(self):
        self.swaps = 0
        self.comparisons = 0

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class LinkedList:
        def __init__(self):
            self.head = None

        def append(self, data):
            if self.head is None:
                self.head = RadixSortLinkedList.Node(data)
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = RadixSortLinkedList.Node(data)

        def to_list(self):
            arr = []
            current = self.head
            while current:
                arr.append(current.data)
                current = current.next
            return arr

        def from_list(self, arr):
            self.head = None
            for data in arr:
                self.append(data)

        def get_max(self):
            if not self.head:
                return None
            max_val = self.head.data
            current = self.head.next
            while current:
                if current.data > max_val:
                    max_val = current.data
                current = current.next
            return max_val

    def counting_sort_linked_list(self, linked_list, exp):
        output = self.LinkedList()
        count = [0] * 10

        current = linked_list.head
        while current:
            index = (current.data // exp) % 10
            count[index] += 1
            current = current.next

        for i in range(1, 10):
            count[i] += count[i - 1]

        current = linked_list.head
        output_list = [None] * len(linked_list.to_list())
        while current:
            index = (current.data // exp) % 10
            output_list[count[index] - 1] = current.data
            count[index] -= 1
            current = current.next

        output.from_list(output_list)
        return output

    def radix_sort_linked_list(self, linked_list):
        max_val = linked_list.get_max()
        exp = 1
        while max_val // exp > 0:
            linked_list = self.counting_sort_linked_list(linked_list, exp)
            exp *= 10
        return linked_list

    def sort(self, arr):
        linked_list = self.LinkedList()
        linked_list.from_list(arr)
        sorted_linked_list = self.radix_sort_linked_list(linked_list)
        return sorted_linked_list.to_list(), self.swaps, self.comparisons
