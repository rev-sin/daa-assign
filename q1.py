"""
References from:
Quick Sort - https://www.geeksforgeeks.org/quick-sort-algorithm/
3-Way Merge Sort - https://www.geeksforgeeks.org/3-way-merge-sort/
Heap Sort - https://www.geeksforgeeks.org/heap-sort/
Bucket Sort - https://www.geeksforgeeks.org/bucket-sort-in-python/
Radix Sort - https://www.geeksforgeeks.org/radix-sort/
"""

"""
QUICK SORT - https://www.geeksforgeeks.org/quick-sort-algorithm/
"""

def partition(arr, low, high):
  
	# Choose the pivot
	pivot = arr[high]
	
	i = low - 1
	
	# Traverse arr[low..high] and move all smaller
	# elements on the left side. Elements from low to 
	# i are smaller after every iteration
	for j in range(low, high):
		if arr[j] < pivot:
			i += 1
			arr[i], arr[j] = arr[i], arr[j]
	
	# Move pivot after smaller elements and
	# return its position
	arr[i + 1], arr[high] = arr[high], arr[i + 1]
	return i + 1

# The QuickSort function implementation
def quick_sort(arr, low, high):
	if low < high:
		# pi is the partition return index of pivot
		pi = partition(arr, low, high)

		# Recursion calls for smaller elements
		# and greater or equals elements
		quick_sort(arr, low, pi - 1)
		quick_sort(arr, pi + 1, high)

"""
3-WAY MERGE SORT - https://www.geeksforgeeks.org/3-way-merge-sort/
"""

""" Merge the sorted ranges [low, mid1), [mid1,mid2) 
and [mid2, high) mid1 is first midpoint 
index in overall range to merge mid2 is second 
midpoint index in overall range to merge"""

def merge(gArray, low, mid1, mid2, high, destArray):
	i = low
	j = mid1
	k = mid2
	l = low

	# Choose smaller of the smallest in the three ranges
	while ((i < mid1) and (j < mid2) and (k < high)):
		if(gArray[i] < gArray[j]):
			if(gArray[i] < gArray[k]):
				destArray[l] = gArray[i]
				l += 1
				i += 1
			else:
				destArray[l] = gArray[k]
				l += 1
				k += 1
		else:
			if(gArray[j] < gArray[k]):
				destArray[l] = gArray[j]
				l += 1
				j += 1
			else:
				destArray[l] = gArray[k]
				l += 1
				k += 1

	# Case where first and second ranges
	# have remaining values
	while ((i < mid1) and (j < mid2)):
		if(gArray[i] < gArray[j]):
			destArray[l] = gArray[i]
			l += 1
			i += 1
		else:
			destArray[l] = gArray[j]
			l += 1
			j += 1

	# case where second and third ranges
	# have remaining values
	while ((j < mid2) and (k < high)):
		if(gArray[j] < gArray[k]):
			destArray[l] = gArray[j]
			l += 1
			j += 1
		else:
			destArray[l] = gArray[k]
			l += 1
			k += 1

	# Case where first and third ranges have
	# remaining values
	while ((i < mid1) and (k < high)):
		if(gArray[i] < gArray[k]):
			destArray[l] = gArray[i]
			l += 1
			i += 1
		else:
			destArray[l] = gArray[k]
			l += 1
			k += 1

	# Copy remaining values from the first range
	while (i < mid1):
		destArray[l] = gArray[i]
		l += 1
		i += 1

	# Copy remaining values from the second range
	while (j < mid2):
		destArray[l] = gArray[j]
		l += 1
		j += 1

	# Copy remaining values from the third range
	while (k < high):
		destArray[l] = gArray[k]
		l += 1
		k += 1

""" Performing the merge sort algorithm on the 
given array of values in the range of indices 
[low, high). low is minimum index, high is 
maximum index (exclusive) """

def mergeSort3WayRec(gArray, low, high, destArray):
	# If array size is 1 then do nothing
	if (high - low < 2):
		return

	# Splitting array into 3 parts
	mid1 = low + ((high - low) // 3)
	mid2 = low + 2 * ((high - low) // 3) + 1

	# Sorting 3 arrays recursively
	mergeSort3WayRec(destArray, low, mid1, gArray)
	mergeSort3WayRec(destArray, mid1, mid2, gArray)
	mergeSort3WayRec(destArray, mid2, high, gArray)

	# Merging the sorted arrays
	merge(destArray, low, mid1, mid2, high, gArray)

def mergeSort3Way(gArray, n):
	# if array size is zero return null
	if (n == 0):
		return

	# creating duplicate of given array
	fArray = []

	# copying elements of given array into
	# duplicate array
	fArray = gArray.copy()

	# sort function
	mergeSort3WayRec(fArray, 0, n, gArray)

	# copy back elements of duplicate array
	# to given array
	gArray = fArray.copy()

	# return the sorted array
	return gArray

"""
HEAP SORT - https://www.geeksforgeeks.org/heap-sort/
"""

# To heapify subtree rooted at index i.
# n is size of heap

def heapify(arr, N, i):
	largest = i  # Initialize largest as root
	l = 2 * i + 1     # left = 2*i + 1
	r = 2 * i + 2     # right = 2*i + 2

	# See if left child of root exists and is
	# greater than root
	if l < N and arr[largest] < arr[l]:
		largest = l

	# See if right child of root exists and is
	# greater than root
	if r < N and arr[largest] < arr[r]:
		largest = r

	# Change root, if needed
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]  # swap

		# Heapify the root.
		heapify(arr, N, largest)

# The main function to sort an array of given size

def heapSort(arr):
	N = len(arr)

	# Build a maxheap.
	for i in range(N//2 - 1, -1, -1):
		heapify(arr, N, i)

	# One by one extract elements
	for i in range(N-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]  # swap
		heapify(arr, i, 0)

"""
BUCKET SORT - https://www.geeksforgeeks.org/bucket-sort-2/
"""

def insertion_sort(bucket):
	for i in range(1, len(bucket)):
		key = bucket[i]
		j = i - 1
		while j >= 0 and bucket[j] > key:
			bucket[j + 1] = bucket[j]
			j -= 1
		bucket[j + 1] = key

def bucket_sort(arr):
	n = len(arr)
	buckets = [[] for _ in range(n)]

	# Put array elements in different buckets
	for num in arr:
		bi = int(n * num)
		buckets[bi].append(num)

	# Sort individual buckets using insertion sort
	for bucket in buckets:
		insertion_sort(bucket)

	# Concatenate all buckets into arr[]
	index = 0
	for bucket in buckets:
		for num in bucket:
			arr[index] = num
			index += 1

"""
RADIX SORT - https://www.geeksforgeeks.org/radix-sort/
"""

# Node class to represent each element in the linked list
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

# Linked list class
class LinkedList:
	def __init__(self):
		self.head = None

	# Function to insert a new node at the end
	def append(self, data):
		if self.head is None:
			self.head = Node(data)
		else:
			current = self.head
			while current.next:
				current = current.next
			current.next = Node(data)

	# Function to convert linked list to list
	def to_list(self):
		arr = []
		current = self.head
		while current:
			arr.append(current.data)
			current = current.next
		return arr

	# Function to convert list to linked list
	def from_list(self, arr):
		self.head = None
		for data in arr:
			self.append(data)

	# Function to get the maximum value in the linked list
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

# Function to perform counting sort on the linked list based on digit represented by exp
def counting_sort_linked_list(linked_list, exp):
	output = LinkedList()
	count = [0] * 10

	# Calculate count of occurrences
	current = linked_list.head
	while current:
		index = (current.data // exp) % 10
		count[index] += 1
		current = current.next

	# Update count to get positions
	for i in range(1, 10):
		count[i] += count[i - 1]

	# Build output linked list
	current = linked_list.head
	output_list = [None] * len(linked_list.to_list())
	while current:
		index = (current.data // exp) % 10
		output_list[count[index] - 1] = current.data
		count[index] -= 1
		current = current.next

	output.from_list(output_list)
	return output

# Radix sort function for linked list
def radix_sort_linked_list(linked_list):
	max_val = linked_list.get_max()
	exp = 1
	while max_val // exp > 0:
		linked_list = counting_sort_linked_list(linked_list, exp)
		exp *= 10
	return linked_list
