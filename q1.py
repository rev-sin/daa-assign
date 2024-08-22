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
			arr[i], arr[j] = arr[j], arr[i]

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

# Function to print an array
def print_array(arr):
	for i in arr:
		print(i, end=" ")
	print()

# Driver code
if __name__ == "__main__":
	arr = [10, 7, 8, 9, 1, 5]
	print("Given array is")
	print_array(arr)

	quick_sort(arr, 0, len(arr) - 1)

	print("\nSorted array is")
	print_array(arr)
	print("\ndone\n")

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
given array of values in the rangeof indices 
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


data = [45, -2, -45, 78, 30, -42, 10, 19, 73, 93]
data = mergeSort3Way(data, 10)
print("After 3 way merge sort: ", end="")
for i in range(10):
	print(f"{data[i]} ", end="")

# This code is contributed by Susobhan Akhuli

print("\ndone\n")

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


# Driver's code
if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7]

	# Function call
	heapSort(arr)
	N = len(arr)

	print("Sorted array is")
	for i in range(N):
		print("%d" % arr[i], end=" ")
# This code is contributed by Mohit Kumra

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

arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
bucket_sort(arr)
print("Sorted array is:")
print(" ".join(map(str, arr)))

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

	# Function to create a linked list from a list
	@classmethod
	def from_list(cls, arr):
		linked_list = cls()
		for item in arr:
			linked_list.append(item)
		return linked_list

# A function to do counting sort of arr[] according to
# the digit represented by exp.
def countingSort(arr, exp1):

	n = len(arr)

	# The output array elements that will have sorted arr
	output = [0] * (n)

	# initialize count array as 0
	count = [0] * (10)

	# Store count of occurrences in count[]
	for i in range(0, n):
		index = arr[i] // exp1
		count[index % 10] += 1

	# Change count[i] so that count[i] now contains actual
	# position of this digit in output array
	for i in range(1, 10):
		count[i] += count[i - 1]

	# Build the output array
	i = n - 1
	while i >= 0:
		index = arr[i] // exp1
		output[count[index % 10] - 1] = arr[i]
		count[index % 10] -= 1
		i -= 1

	# Copying the output array to arr[],
	# so that arr now contains sorted numbers
	for i in range(0, len(arr)):
		arr[i] = output[i]

# Method to do Radix Sort
def radixSort(arr):

	# Find the maximum number to know number of digits
	max1 = max(arr)

	# Do counting sort for every digit. Note that instead
	# of passing digit number, exp is passed. exp is 10^i
	# where i is current digit number
	exp = 1
	while max1 / exp >= 1:
		countingSort(arr, exp)
		exp *= 10

# Driver code
arr = [170, 45, 75, 90, 802, 24, 2, 66]

# Create a linked list from the array
linked_list = LinkedList.from_list(arr)

# Function Call on the linked list
radixSort(linked_list.to_list())

# Print sorted linked list
sorted_arr = linked_list.to_list()
for i in sorted_arr:
	print(i, end=" ")

# This code is contributed by Mohit Kumra
# Edited by Patrick Gallagher
