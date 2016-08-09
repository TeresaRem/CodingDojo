# car.py

class Car(object):
	def __init__(self,price,speed,fuel="Full",mileage=20,tax=0.12):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.tax = tax
		if self.price > 10000:
			self.tax = 0.15
		self.display_all()
	def display_all(self):
		print "Price: ${}".format(self.price)
		print "Speed: {}mph".format(self.speed)
		print "Fuel: {}".format(self.fuel)
		print "Milage: {}mpg".format(self.mileage)
		print "Tax: {}".format(self.tax)
		print ""

car1 = Car(100,100,"Kind of Full",20)
car2 = Car(100000,100)
car3 = Car(10000,50)
car4 = Car(2000,5,"Not Full",30)
car5 = Car(20000,10,"Empty")
car6 = Car(30000,100)