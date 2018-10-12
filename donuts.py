# Create a function to help Mr. James plan for a donut celebration
## Input: Exam Scores for all students
## Output: How many donuts

# Conditions
## If the class average is an A, every student gets a donut
## If the class average is a B, every student gets a half donut. Make sure not to round half donuts up. Return the float.
## If the class average is a C, every student gets 1/3 of a donut. Make sure not to round up, but to return the float
## If the class average is a D, every student will give Mr. James a half donut.


# Step One
## Create a flow chart for your algorithm



# Step Two
## Create your function. Fully comment out you code.
#
def grade2Donuts():
    allGrades = []      # array to add inputted grades later
    classSize = 13      # size of class for amount of donuts, known in our case

    for question in range(13):      # asks for grade 13 times, based on known number of students
        grade = int(input("Enter student's exam grade:\n"))
        allGrades.append(grade)     # adds inputted grade to array
    averageGrade = (sum(allGrades) // len(allGrades))       # calculates grade average for class

    if averageGrade <= 70:      # series of conditions for average class grade, returns required amount of donuts
        print ((classSize/2),"donuts will be needed, but all given to Mr. James.")
    elif 80 >= averageGrade > 70:
        print ((classSize/3),"donuts will be needed.")
    elif 90 >= averageGrade > 80:
        print ((classSize/2),"donuts will be needed.")
    else:
        print (classSize,"donuts will be needed.")


grade2Donuts()

# Step Three
## Beta test your function with another group. How can you make you function better?

def grade2Donuts():
    allGrades = []
    classSize = int(input("How many students are in the class?\n"))     # asks for number of students, as is a function for a nother group
    teacherName = input("What is the teacher's name?\n")        # teacher's name is for only if score is below 70, in the specific return

    for question in range(classSize):       # new variable class size takes places of where 13 was.
        grade = int(input("Enter student's exam grade:\n"))
        allGrades.append(grade)
    averageGrade = (sum(allGrades) // len(allGrades))

    if averageGrade <= 70:
        print ((classSize/2),"donuts will be needed, as the average exam score was",(averageGrade))
        print ("...but all given to",(teacherName))     # application of teacher's name
    elif 80 >= averageGrade > 70:
        print ((classSize/3),"donuts will be needed, as the average exam score was",(averageGrade))
    elif 90 >= averageGrade > 80:
        print ((classSize/2),"donuts will be needed, as the average exam score was",(averageGrade))
    else:
        print (classSize,"donuts will be needed, as the average exam score was",(averageGrade))

grade2Donuts()
