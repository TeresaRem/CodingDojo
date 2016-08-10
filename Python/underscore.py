# underscore.py

class Underscore(object):
  def map(self):
    # your code here
    print 'map'
  def reduce(self):
    # your code here
    print 'reduce'
  def find(self):
    # your code here
    print 'find'
  def filter(self,array,what):
  	arr = []
  	for x in array:
  		if what:
  			arr.append(x)
  		print array[x]
  	print arr
  	return arr
  	# your code 
  def reject(self):
    # your code
    print 'reject'
# you just created a library with 5 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above
