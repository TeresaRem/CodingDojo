## insertionSort.py

## fix this, it is backwards

def insertionSort(arr):
	start=1
	for i in range(0,len(arr)):
		for j in range(start,0,-1):
			if arr[j] > arr[j-1]:
				temp = arr[j]
				arr[j] = arr[j-1]
				arr[j-1] = temp
				print "swapped {} and {}".format(arr[j],arr[j-1])
		start+=1
		print arr
		if start+1 > len(arr):
			break
	return arr



insertionSort([6,5,3,1,8,7,2,4]);
