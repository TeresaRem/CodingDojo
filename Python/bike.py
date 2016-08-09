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
	def reverse(self):
		print "Reversing"
		if self.miles < 5:
			print "you are at start"
			return
		self.miles -= 5

bike1 = Bike(200,200)
bike2 = Bike(150,150)
bike3 = Bike(100,100)

bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()