"""冒泡排序 """


def bubble_sort(arr):
	length = len(arr)
	for item in range(0, length):
		for index in range(1, length - item):
			if arr[index -1] > arr[index]:
				arr[index - 1], arr[index] = arr[index], arr[index-1]

	return arr

print bubble_sort([5,4,3,2,1])


def bubble_sort_1(arr):
	length = len(arr)
	flag = length
	for item in range(0, length):
		for index in range(1, flag):
			if arr[index-1] > arr[index]:
				flag = index
				arr[index - 1], arr[index] = arr[index], arr[index-1]

	return arr

print bubble_sort_1([5,4,3,2,1])



def bubble_sort_2(arr):
	isSorted = False
	length = len(arr)
	i = 0
	while i < len(arr) and not isSorted:
		isSorted = True
		for index in range(1, length - i):
			if arr[index-1] > arr[index]:
				isSorted = False
				arr[index - 1], arr[index] = arr[index], arr[index-1]

	return arr

print bubble_sort_2([5,4,3,2,1])
