# coinToss.py

# You're going to create a program that simulates tossing a coin 
# 5,000 times. Your program should display how many times the 
# head/tail appears.

# Sample output should be like the following:

# Starting the program...

# Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far 
# Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far 
# Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far 
# Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
# ........
# Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far 

# Ending the program, thank you!

import random

def coinToss():
	print "Starting the program..."
	flips = 0
	heads = 0
	tails = 0
	for i in range(5000):
		coin = round(random.random())
		flips += 1
		if coin == 0:
			heads += 1
			print "Attempt #{}: Coin flips and it's a head! ... Got {} head(s) and {} tail(s)".format(flips,heads,tails)
		if coin == 1:
			tails += 1
			print "Attempt #{}: Coin flips and it's a tail! ... Got {} head(s) and {} tail(s)".format(flips,heads,tails)

	print "Ending the program, thank you!"


coinToss()