# stars.py

# Create a function called  draw_stars() that takes a list of numbers 
# and prints out  *.

def draw_stars_simple(x):
	for i in range(len(x)):
		print "*"*x[i]

# Allow a list containing integers and strings to be passed to the  
# draw_stars() function. When a string is passed, instead of  
# displaying *, display the first letter of the string according 
# to the example below. You may use the .lower() string method for this part.

# For example:
#  x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

# draw_stars(x):

# **** 
# ttt 
# * 
# mmmmmmm 
# ***** 
# ******* 
# jjjjjjjjjjj

def draw_stars(x):
	for i in range(len(x)):
		if isinstance(x[i],(int,long)):
			print "*"*x[i]
		else:
			print x[i][0].lower()*len(x[i])


draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])

# how to do draw_stars without isinstance?