########################################################################
##
## CS 101 Lab
## Program #6
## Name Jack Turner
## Email jnt4vp@umsystem.edu
##
## PROBLEM : Create a Caesar Cipher
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
## Makes sure the user inputs 1,2 or Q on the Main Menu
##  
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

def encode():
    text = input("\nEnter (brief) text to encrypt: ")
    shift = int(input("Enter the number to shift letters by: "))
    ord_list = []
    ord_list_change = []
    encoded_string = ""
    for letter in text:
        ord_list.append(ord(letter))
    for number in ord_list:
        if number != 32:
            ord_list_change.append(number+shift)
        elif number == 32:
            ord_list_change.append(number)
    for number in ord_list_change:
        encoded_string += chr(number).upper()
    print("Encrypted:",encoded_string,"\n")
    
def decode():
    text = input("\nEnter (brief) text to decrypt: ")
    shift = int(input("Enter the number to shift letters by: "))
    ord_list = []
    ord_list_change = []
    decoded_string = ""
    for letter in text:
        ord_list.append(ord(letter))
    for number in ord_list:
        if number != 32:
            ord_list_change.append(number-shift)
        elif number == 32:
            ord_list_change.append(number)
    for number in ord_list_change:
        decoded_string += chr(number).upper()
    print("Decrypted:",decoded_string,"\n")
    
if __name__ == "__main__":    
    def cipher():
        play = True
        while play == True:
            mainmenu = input("MAIN MENU:\n1) Encode a string\n2) Decode a string\nQ) Quit\nEnter your selection ==> ")
            if mainmenu == "1":
                encode()
            elif mainmenu == "2":
                decode()
            elif mainmenu.lower() == "q":
                play = False
            else:
                print("Please enter 1 2 or Q")
                cipher()
    cipher()