# MathDojo.py

# Create a Python class called MathDojo that has the methods 
# add and subtract. Have these 2 functions take at least 1 parameter. 

# Then create a new instance called md. It should be able to do the following task:
# MathDojo().add(2).add(2, 5).subtract(3, 2).result
# which should perform 0+2+(2+5)-(3+2) and return 4.


class MathDojo(object):
	def add(x,*y):
		sum = 0
		for i in y:
			sum += i
		return sum
	def subtract(x,*y):
		return x
	def result(self):
		print self;
		return self;

md = MathDojo()

md.add(2).add(2, 5).subtract(3, 2).result