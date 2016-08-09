# bike.py

class Bike(object):
	def __init__(self,price,max_speed,miles=0):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles
	def displayInfo(self):
		print "${}, {}mph, {} miles".format(self.price,self.max_speed,self.miles)
	def ride(self):
		print "Riding"
		self.miles += 10
		return self
	def reverse(self):
		print "Reversing"
		if self.miles < 5:
			print "you are at start"
			return self
		self.miles -= 5
		return self

bike1 = Bike(200,200)
bike2 = Bike(150,150)
bike3 = Bike(100,100)

bike1.ride().ride().ride().reverse().displayInfo()

bike2.ride().ride().reverse().reverse().displayInfo()

bike3.reverse().reverse().reverse().displayInfo()