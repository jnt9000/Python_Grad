########################################################################
##
## CS 101 Lab
## Program #9
## Name Jack Turner
## Email jnt4vp@umsystem.edu
##
## PROBLEM : Create a program to find police crimes in a file
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
## Makes sure the user inputs a valid file
##  
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

import csv

def month_from_number(integer):
    integer = int(integer)
    if integer == 1:
        return "January"
    elif integer == 2:
        return "February"
    elif integer == 3:
        return "March"
    elif integer == 4:
        return "April"
    elif integer == 5:
        return "May"
    elif integer == 6:
        return "June"
    elif integer == 7:
        return "July"
    elif integer == 8:
        return "August"
    elif integer == 9:
        return "September"
    elif integer == 10:
        return "October" 
    elif integer == 11:
        return "November"
    elif integer == 12:
        return "December"
    else:
        return False

def read_in_file(filename):
    file = open(filename, encoding="utf-8")
    file_csv = csv.reader(file)
    list1 = []
    for line in file_csv:
        list1.append(line)
    file.close()
    return list1

def create_reported_date(listname):
    keylist = []
    key_count = {}
    for lists in listname[1:]:
        keylist.append(lists[1])
    for key in keylist:
        try:
            key_count[key] += 1
        except KeyError:
            key_count[key] = 1
    return key_count

def create_reported_month(listname):
    keylist = []
    key_count = {}
    for lists in listname[1:]:
        keylist.append(lists[1][1])
    for key in keylist:
        try:
            key_count[key] += 1
        except KeyError:
            key_count[key] = 1
    return key_count    

def create_offense_dict(listname):
    keylist = []
    key_count = {}
    for lists in listname[1:]:
        keylist.append(lists[7])
    for key in keylist:
        try:
            key_count[key] += 1
        except KeyError:
            key_count[key] = 1
    return key_count
        
def create_offense_by_zip(listname):
    keylist = []
    key_count = {}
    key_count2 = {}
    for lists in listname[1:]:
        if lists[7] not in key_count:
            key_count.update({lists[7]:[lists[13]]})
        else:
            key_count[lists[7]].append(lists[13])
    for key in key_count:
        key_count2.update({key:[]})
        for key1 in key_count.get(key):
            try:
                key_count2[key][int(key_count.get(key).index(key1))][key1] += 1
            except:
                key_count2[key].append({key1:1})
    return key_count2
    
    
        
                
def crimedata():
    input1 = input("Enter the name of crime data file ==> ")
    try:
        read_in_file(input1)
    except FileNotFoundError:
        print("Could not find the file specified. {} not found".format(input1))
        crimedata()
    maxcrime = 0
    pos = 0
    for key in create_reported_month(read_in_file(input1)):
        if create_reported_month(read_in_file(input1)).get(key) > maxcrime:
            maxcrime = create_reported_month(read_in_file(input1)).get(key)
    for key in create_reported_month(read_in_file(input1)):
        if create_reported_month(read_in_file(input1)).get(key) == maxcrime:
            pos = key
    print("The month with the highest # of crimes is {} with {} offenses".format(month_from_number(pos),maxcrime))
    maxoffense = 0
    pos2 = 0
    for key in create_offense_dict(read_in_file(input1)):
        if create_offense_dict(read_in_file(input1)).get(key) > maxoffense:
            maxoffense = create_offense_dict(read_in_file(input1)).get(key)
    for key in create_offense_dict(read_in_file(input1)):
        if create_offense_dict(read_in_file(input1)).get(key) == maxoffense:
            pos2 = key    
    print("The offense with the highest # of crimes is {} with {} offenses\n".format(pos2,maxoffense))
    input2 = input("Enter an offense ")
    print("\n",input2,"offenses by Zip Code")
    print("Zip Code # Offenses")
    print("===================")
    for crime in create_offense_by_zip(read_in_file(input1)):
        if crime == input2:
            for thing in create_offense_by_zip(read_in_file(input1)).get(crime):
                for zipcode in create_offense_by_zip(read_in_file(input1)).get(crime)[create_offense_by_zip(read_in_file(input1)).get(crime).index(thing)]:
                    print(zipcode,"           ", create_offense_by_zip(read_in_file(input1)).get(crime)[create_offense_by_zip(read_in_file(input1)).get(crime).index(thing)].get(zipcode))

crimedata()