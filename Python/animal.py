# animal.py

class Animal(object):
	def __init__(self,name):
		self.name = name
		self.health = 100
	def walk(self):
		self.health -= 1
		return self
	def run(self):
		self.health -= 5
		return self
	def displayHealth(self):
		print "name is {}".format(self.name)
		print "health is {}".format(self.health)
		return self

animal = Animal('animal').walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
	def __init__(self,name):
		super(Dog,self).__init__(self)
		self.health = 150
		self.name = name
	def pet(self):
		self.health += 5
		return self

dog = Dog('dog').walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
	def __init__(self,name):
		super(Dragon,self).__init__(self)
		self.health = 170
		self.name = name
	def fly(self):
		self.health -= 10
		return self
	def displayHealth(self):
		print "this is a dragon!"
		super(Dragon,self).displayHealth()
		return self

dragon = Dragon('dragon').walk().walk().walk().run().run().fly().fly().displayHealth()


