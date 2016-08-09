## bubbleSort.py

import random, datetime

def bubbleSort(arr):
	# print "starting array is:"
	# print arr
	a = datetime.datetime.now()
	for i in range(len(arr)-1,0,-1):
		for j in range(0,i):
			if arr[j] > arr[j+1]:
				temp = arr[j+1]
				arr[j+1] = arr[j]
				arr[j] = temp
				# print "swapped {} and {}".format(arr[j],arr[j+1])
				# print arr
	b = datetime.datetime.now()
	time = b - a
	print "{} seconds".format(time.total_seconds())
	return arr


# bubbleSort([6,5,3,1,8,7,2,4])

def randomArr(): # create random array
	arr = []
	for i in range(1000):
		arr.append(random.randint(0,10000))
	return arr

hundred = randomArr()

bubbleSort(hundred)


