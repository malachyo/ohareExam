
def procrastinateCalc():

    deadline = float(input("How many hours until the assignment is due?\n"))
    calcResult = deadline - deadline / 8
    resultDeadline = round((calcResult), 1)

    print("You should do the assignment %f hours from now" %resultDeadline)

procrastinateCalc()


def procrastinateCalcRevised():

    deadline = float(input("How many hours until the assignment is due?\n"))
    importance = input("\nHow important is the assignment?\n""a) utmost important vital determining future important\n""b) ok yea pretty important like big project time\n""c) eh whatever not too bad like isall good\n""d) nah who even bout to do this\n")

    if importance == "a":
        calcResult = deadline - deadline / 8
    elif importance == "b":
        calcResult = deadline - deadline / 6
    elif importance == "c":
        calcResult = deadline - deadline / 4
    else:
        calcResult = deadline - deadline / 2

    resultDeadline = round((calcResult), 1)

    print("You should do the assignment %f hours from now" %resultDeadline)

procrastinateCalcRevised()
