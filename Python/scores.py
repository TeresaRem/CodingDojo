# Create a program that prompts the user ten times for a 
# test score between 60 and 100. Each time a score is generated, 
# your program should display what is the grade of that score. 
# Here is the grade table:

# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A

# Result is 
# Score: 87; Your grade is B

def scoresAndGrades():
	scores = []
	grades = []
	for i in range(10):
		score = input('Enter your score between 60 and 100: ')
		if score > 100 or score < 60:
			grades.append("N/A")
			print "invalid score entered"
		if score > 89 and score < 101:
			grades.append("A")
		if score > 79 and score < 90:
			grades.append("B")
		if score > 69 and score < 80:
			grades.append("C")
		if score > 59 and score < 70:
			grades.append("D")
		scores.append(score)

	print "Scores and Grades"

	for j in range(len(scores)-1):
		print "Score: {};Your grade is {}".format(scores[j],grades[j])

	print "End of the program. Bye!"

scoresAndGrades()