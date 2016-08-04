## selectionSort.py

def selectionSort(arr):
	min = arr[0]
	start = 0
	for i in range(0,len(arr)-1):
		for j in range(start,len(arr)):
			if arr[j] < min:
				min = arr[j]
				index = j
		print "current minimum is {} at index {}".format(min,index)
		if arr[start] > min:
			temp = arr[start]
			arr[start] = arr[index]
			arr[index] = temp
			print "swap {} and {}".format(arr[index],arr[start])
		print "array is:"
		print arr
		start+=1
		min = arr[start]
	return arr

selectionSort([6,5,3,1,8,7,2,4])