########################################################################
##
## CS 101 Lab
## Program #7
## Name Jack Turner
## Email jnt4vp@umsystem.edu
##
## PROBLEM : Create a program to identify vehicles within a certain mpg threshold set by the user
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
## Makes sure the user inputs a mpg value between 0 and 100 and tells the user if their file exists
##  
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

def output(input1,input2,input3):
    file = open(input2)
    file1 = file.read()
    file2 = file1.split("\n")
    file4 = open(input3,"w")
    for line in file2[1:]:
        file3 = line.split("\t")
        try:
            if int(file3[7]) > input1:
                file4.write("{} {}              {}                            {:.3f}\n".format(file3[0],file3[1],file3[2],int(file3[7])))
        except ValueError:
            print("Could not convert value {} for vehicle {} {} {}".format(file3[7],file3[0],file3[1],file3[2]))
            continue
        except IndexError:
            continue
    file.close()
    file4.close()

def output_check(outputfile):
    try:
        file = open(outputfile) 
        file.close()
        return True
    except IOError:
        return False
        
def input_check(inputfile):
    try:
        file = open(inputfile)
        file.close()
        return True
    except FileNotFoundError:
        return False
        
def mpg():
    try:
        input1 = float(input("Enter the minimum mpg ==> "))
        while input1 not in range(0,100):
            if input1 < 0:
                print("Fuel economy must be greater than 0")
                input1 = float(input("Enter the minimum mpg ==> "))
            elif input1 > 100:
                print("Fuel economy must be less than 100")
                input1 = float(input("Enter the minimum mpg ==> "))
        input2 = input("Enter the name of the input vehicle file ==> ")
        while input_check(input2) == False:
            print("Could not open file {}".format(input2))
            input2 = input("Enter the name of the input vehicle file ==> ")
        input3 = input("Enter the name of the file to output to ==> ")
        while output_check(input3) == False:
            print("There is an IO Error {}".format(input3))
            input3 = input("Enter the name of the file to output to ==> ")
        output(input1,input2,input3)
    except ValueError:
        print("You must enter a number for the fuel economy")
        mpg()
    
mpg()