## selectionSort.py

import random, datetime

def selectionSort(arr):
	a = datetime.datetime.now()
	min = arr[0]
	start = 0
	for i in range(0,len(arr)-1):
		for j in range(start,len(arr)):
			if arr[j] < min:
				min = arr[j]
				index = j
		# print "current minimum is {} at index {}".format(min,index)
		if arr[start] > min:
			temp = arr[start]
			arr[start] = arr[index]
			arr[index] = temp
			# print "swap {} and {}".format(arr[index],arr[start])
		# print "array is:"
		# print arr
		start+=1
		min = arr[start]
	b = datetime.datetime.now()
	time = b - a
	print "{} seconds".format(time.total_seconds())
	return arr

# selectionSort([6,5,3,1,8,7,2,4])

def randomArr(): # create random array
	arr = []
	for i in range(1000):
		arr.append(random.randint(0,10000))
	return arr

hundred = randomArr()

selectionSort(hundred)