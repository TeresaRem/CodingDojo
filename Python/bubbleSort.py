## bubbleSort.py

def bubbleSort(arr):
	print "starting array is:"
	print arr
	for i in range(len(arr)-1,0,-1):
		for j in range(0,i):
			if arr[j] > arr[j+1]:
				temp = arr[j+1]
				arr[j+1] = arr[j]
				arr[j] = temp
				print "swapped {} and {}".format(arr[j],arr[j+1])
				print arr
	return arr


bubbleSort([6,5,3,1,8,7,2,4])