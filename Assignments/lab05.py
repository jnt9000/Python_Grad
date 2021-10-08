########################################################################
##
## CS 101 Lab
## Program #4
## Name Jack Turner
## Email jnt4vp@umsystem.edu
##
## PROBLEM : Create a program that acts as a slot machine using functions
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Will continue to ask player to input until it is correct in play_again function,
##      Wager must be between 0-100 and cannot exceed the bank value, 
##      get_bank value must be between 0-100
##  
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

import random

def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    ask = input("Do you want to play again? ==> ")
    if ask == 'YES' or ask == 'Y':
        return True
    elif ask == 'NO' or ask == 'N':
        return False
    else:
        print("You must enter Y/YES/N/NO to continue.  Please try again")
        play_again()

def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    wager_amount = int(input("How many chips do you want to wager? ==> "))
    if wager_amount <= 0:
        print("The wager amount must be greater than 0. Please enter again. ")
        get_wager()
    elif wager_amount > bank:
        print("The wager amount cannot be greater than how much you have. ")
        get_wager()
    else:    
        return wager_amount            

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    pos1 = random.randint(1,10)
    pos2 = random.randint(1,10)
    pos3 = random.randint(1,10)

    return pos1, pos2, pos3

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if reela == reelb and reela == reelc:
        return 3
    elif reela == reelb or reela == reelc or reelb == reelc:
        return 2
    else:
        return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    chips = int(input("How many chips do you want to start with? ==> "))
    if chips < 0:
        print("Too low a value, you can only choose 1 -100 chips")
        chips()
    elif chips > 101:
        print("Too high a value, you can only choose 1 -100 chips")
        chips()
    else:
        return chips

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3:
        return wager * 10
    elif matches == 2:
        return wager * 3
    else:
        return wager * -1     


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        while bank > 0:
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print("You lost all", 0, "in", 0, "spins")
        print("The most chips you had was", 0)
        playing = play_again()