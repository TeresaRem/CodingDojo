# names.py

# Given the following list:
# students = [ 
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
# Create a program that outputs:
# Michael Jordan
# John Rosales
# Mark Guillen
# KB Tonel

def simple_names(x):
	for i in range(len(x)):
		print "{} {}".format(x[i]['first_name'],x[i]['last_name'])

# Given the following dictionary:
users = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

# Create a program that prints the following format 
# (including number of characters in each combined name):
# Students
# 1 - MICHAEL JORDAN - 13
# 2 - JOHN ROSALES - 11
# 3 - MARK GUILLEN - 11
# 4 - KB TONEL - 7
# Instructors
# 1 - MICHAEL CHOI - 11
# 2 - MARTIN PURYEAR - 13

def names(x):
	for key in x: # for students and instructors
		print key
		for index,item in enumerate(x[key],1): # count entries, start at 1
			print "{} - {} {} - {}".format(index,item["first_name"].upper(),item["last_name"].upper(),len(item["first_name"])+len(item["last_name"]))

names(users)






