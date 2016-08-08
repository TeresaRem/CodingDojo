# Create a function called 'multiply' that reads each value in the list 
# (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been 
# multiplied by 5.

# The function should multiply each value in the list by the second argument. 
# b = multiply(a, 5) 
# print b

def multiply(arr,num):
	for i in range(len(arr)):
		arr[i] = arr[i]*num
	print arr
	return arr

multiply([2,4,10,16],5) 