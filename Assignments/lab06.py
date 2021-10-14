########################################################################
##
## CS 101 Lab
## Program #5
## Name Jack Turner
## Email jnt4vp@umsystem.edu
##
## PROBLEM : Create a program to decode library numbers
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
## Makes sure the user enters the right number of characters and at the right places
##  
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
import string

def get_school(index5):
    school1 = "School of Computing and Engineering SCE" 
    school2 = "School of Law"
    school3 = "College of Arts and Sciences"
    school4 = "Invalid School"
    if index5 == 1:
        return school1
    elif index5 == 2:
        return school2
    elif index5 == 3:
        return school3
    else:
        return school4
    
def get_grade(index6):
    grade1 = "Freshman"
    grade2 = "Sophomore"
    grade3 = "Junior"
    grade4 = "Senior"
    grade5 = "Invalid Grade"
    if index6 == 1:
        return grade1
    elif index6 == 2:
        return grade2
    elif index6 == 3:
        return grade3
    elif index6 == 4:
        return grade4
    else:
        return grade5

def character_value(character):
    return string.ascii_uppercase.index(character)

def get_check_digit(card):
    converted_card = []
    converted_card2 = []
    check_digit = 0
    for value in card:
        if value.isdigit() == False:
            converted_card.append(str(string.ascii_uppercase.index(value)))
        else:
            converted_card.append(value)
    for value in card:
        converted_card2.append((int(card.index(value))+1)*int((converted_card[card.index(value)])))
    for num in converted_card2:
        if converted_card2.index(num) < 9:  
            check_digit += num
    if (check_digit % 10) != converted_card2[9]:
        return False, (check_digit % 10)
    else:
        return True

def verify_check_digit(card):
    Error1 = "The length of the number given must be 10"
    Error2 = "The first 5 characters must be A-Z, the invalid character is at 3 is %"
    Error3 = "The last 3 characters must be 0-9, the invalid character is at 7 is X"
    Error4 = "The sixth character must be 1 2 or 3"
    Error5 = "The seventh character must be 1 2 3 or 4"
    Error6 = "Check Digit 8 does not match calculated value 2."
    Valid = ""
    i = ""
    for char in card[0:5]:
        if char.isdigit() == True:
            i += char
    if len(str(card)) != 10:
        return False, "The length of the number given must be 10"
    elif card[0:5].isdigit() == True:
        return False, "The first 5 characters must be A-Z, the invalid character at {} is {}".format(card.index(i[0]),i[0])        
    elif int(card[-1]) not in range(0,10) and int(card[-2]) not in range (0,10) and int(card[-3]) not in range(0,10):
        return False, "The last 3 characters must be 0-9, the invalid character is at 7 is X"
    elif int(card[5]) not in range(1,4):
        return False, "The sixth character must be 1 2 or 3"
    elif int(card[6]) not in range(1,5):
        return False, "The seventh character must be 1 2 3 or 4"
    else:
        return True, ""
        
if __name__ == "__main__":
    playing = True
    while playing:
        card = input("Enter Library Card. Hit Enter To Exit ==> ")
        if verify_check_digit(card)[0] == False:
            print("Library card is invalid.")
            print(verify_check_digit(card)[1])
        else:
            print("Library card is valid.")
            print("The card belongs to a student in",get_school(int(card[5])))
            print("The card belongs to a",get_grade(int(card[6])))