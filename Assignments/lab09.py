########################################################################
##
## CS 101 Lab
## Program #8
## Name Jack Turner
## Email jnt4vp@umsystem.edu
##
## PROBLEM : Create a program to output weighted grades
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
## Makes sure the user inputs one of the main menu options and doesn't allow values lower than 0
##  
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

import math

testscores = []

def tests(a):
    global testscores
    if a == "a":
        testscore = int(input("\nEnter the new Test score 0-100 ==> "))
        while testscore < 0:
            print("Must be greater than 0")
            testscore = int(input("\nEnter the new Test score 0-100 ==> "))
        testscores.append(testscore)
        return testscores
    elif a == "r":
        removetest = int(input("\nEnter the Assignment to remove 0-100 ==> "))
        while removetest not in testscores:
            print("Could not find that score to remove")
        testscores.pop(testscores.index(removetest))
        return testscores
    elif a == "c":
        print("Tests cleared")
        testscores = []
        return testscores
    
assignmentscores = []

def assignments(a):
    if a == "a":
        global assignmentscores
        assignmentscore = int(input("\nEnter the new Assignment score 0-100 ==> "))
        while assignmentscore < 0:
            print("Must be greater than 0")
            assignmentscore = int(input("\nEnter the new Assignment score 0-100 ==> "))
        assignmentscores.append(assignmentscore)
        return assignmentscores
    elif a == "r":
        removeassignment = int(input("\nEnter the Assignment to remove 0-100 ==> "))
        while removeassignment not in assignmentscores:
            print("Could not find that score to remove")
        assignmentscores.pop(removeassignment)
        return assignmentscores
    elif a == "c":
        print("Assignments cleared")
        assignmentscores = []
        return assignmentscores       

def grades():
    playing = True
    while playing == True:
        input1 = input("\tGrade Menu\n1 - Add Test\n2 - Remove Test\n3 - Clear Tests\n4 - Add Assignment\n5 - Remove Assignment\n6 - Clear Assignments\nD - Display Scores\nQ - Quit\n\n==> ")
        if input1 == "1":
            test1 = tests("a")
        elif input1 == "2":
            test2 = tests("r")
        elif input1 == "3":
            test3 = tests("c")
        elif input1 == "4":
            assignment1 = assignments("a")
        elif input1 == "5":
            assignment2 = assignments("r")
        elif input1 == "6":
            assignment3 = assignments("c")
        elif input1 == "D": 
            testavg = sum(test1) / len(test1)
            teststd = sum([((x - testavg) ** 2) for x in test1]) / len(test1)
            assignavg = sum(assignment1) / len(assignment1)
            assignstd = sum([((x - assignavg) ** 2) for x in assignment1]) / len(assignment1)
            weighted = (testavg * 0.6) + (assignavg * 0.4)
            print("Type               #       min       max       avg       std")
            print("============================================================")
            print("Tests              {}      {:.1f}      {:.1f}      {:.2f}     {:.2f}".format(len(test1),min(test1),max(test1),testavg,teststd))
            print("Programs           {}      {:.1f}      {:.1f}      {:.2f}     {:.2f}".format(len(assignment1),min(assignment1),max(assignment1),assignavg,assignstd))
            print("\n\nThe weighted score is {:.2f}".format(weighted))
        elif input1 == "Q":
            playing = False
        else:
            grades()
grades()