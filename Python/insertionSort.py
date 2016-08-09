# insertionSort.py

import random, datetime

def insertionSort(arr):
	a = datetime.datetime.now()
	start=1
	for i in range(0,len(arr)-1):
		for j in range(start,0,-1):
			if arr[j] < arr[j-1]:
				temp = arr[j]
				arr[j] = arr[j-1]
				arr[j-1] = temp
				# print "swapped {} and {}".format(arr[j],arr[j-1])
		start+=1
		# print arr
	b = datetime.datetime.now()
	time = b - a
	print time.total_seconds()
	return arr

# insertionSort([6,5,3,1,8,7,2,4]);

def randomArr(): # create random array
	arr = []
	for i in range(100):
		arr.append(random.randint(0,10000))
	return arr

hundred = randomArr()

insertionSort(hundred)