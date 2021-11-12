########################################################################
##
## CS 101 Lab
## Program #10
## Name Jack Turner
## Email jnt4vp@umsystem.edu
##
## PROBLEM : Create a program to find the most commonly used words in a text file
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

import re

def reader(input1):
    words = []
    file = open(input1, "r")
    f = file.read()
    splitter = re.split(" |\n",f)
    for word in splitter:
        word = word.replace(".", "")
        word = word.replace(",", "")
        word = word.replace("!", "")
        words.append(word) 
    for word in words:
        if "-" in word:
            words.remove(word)
    for word in words:
        words[words.index(word)] = word.lower()
    return words

def numberofwords():
    try:
        input1 = input("\nEnter the name of the file to open ")
        words = reader(input1)
        print("\nMost frequently used words")
        print("#           Word               Freq.")
        print("=====================================")
        wordlist = []
        occurences = []
        dictionary1 = {}
        dictionary = []
        ordered = {}
        for word in words:
            if len(word) > 3:
                if word not in wordlist:
                    wordlist.append(word)
                    occurences.append(1)
                elif word in wordlist:
                    occurences[wordlist.index(word)] += 1
        for word in wordlist:
            dictionary.append({word:occurences[wordlist.index(word)]})
        count = 1
        once = []
        for value in dictionary:
            for val in value:
                if value.get(val) == 1:
                    once.append(value)     
        lister = []    
        for value in dictionary:
            for val in value:
                dictionary1[val] = value.get(val)
        sortedlist = sorted(dictionary1, key=dictionary1.get)
        sortedlist.reverse()
        if len(sortedlist) < 10:
            for word in sortedlist:
                lister.append(word)
        else:
            for word in sortedlist[0:10]:
                lister.append(word)
        for word in lister:
            print(count, "         ",word, "            ", dictionary1.get(word))
            count += 1
        print("\nThere are {} words that occur only once".format(len(once)))
        print("There are {} unique words in the document".format(len(wordlist)))
    except FileNotFoundError:
        print("Could not find {}".format(input1))
        print("Please Try Again")
        numberofwords()

numberofwords()