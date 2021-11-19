########################################################################
##
## CS 101 Lab
## Program #11
## Name Jack Turner
## Email jnt4vp@umsystem.edu
##
## PROBLEM : Create a program with a clock class to print the time
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
## 
##  
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

import time

class Clock:

    def __init__(self, hour, minute, second, typ=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.typ = 0
        if self.typ == 1:
            if hour == 0:
                hour = 12    
    def __str__(self):
        if self.hour < 12:
            self.hour12 = "am"
        else:
            self.hour12 = "pm"          
        return "{:02}:{:02}:{:02} {}".format(self.hour,self.minute,self.second,self.hour12)
    def tick(self):
        if self.second < 59:     
            self.second += 1
        else:
            self.second = 0
            self.minute += 1
        if self.minute > 59:
            self.hour += 1
            self.minute = 0
        if self.hour < 12:
            self.hour12 = "am"
        else:
            self.hour12 = "pm"  
        return "{:02}:{:02}:{:02} {}".format(self.hour,self.minute,self.second,self.hour12)
    
    def ticker(self):
        while True:
            print(self.tick())
            time.sleep(1)

def ClockProgram():
    input1 = int(input("What is the current hour ==> "))
    input2 = int(input("What is the current minute ==> "))
    input3 = int(input("What is the current second ==> "))
    clock = Clock(input1,input2,input3)
    clock.ticker()
    
ClockProgram()