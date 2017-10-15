# Problem Set 5: Ghost
# Name: Satyendra gupta
# Collaborators: stackoverflow
# Time: 6 hours
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    #print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

# TO DO: your code begins here..
player = "Player 1"
def player_choose():
    global player
    if player == "Player 1" :     ##if current player is Player 1 then after running function the next will be Player 2
        player = "Player 2"
        return player
    
    elif player == "Player 2" :
        player = "Player 1"
        return player
    else :
        player = "Player 1"
        return player

word = ""
print ""
print ""
print "Welcome to Ghost!"
print ""
print player + " goes first. "
print ""

def ghost():
    global word
    if any(word in s for s in wordlist):
        print "current word fragment: " + "'" + word + "'"
        #print player + " says letter :"
        x = ""
        x = raw_input(player + " says letter :")
        if len(x) == 1:
            word = word + string.lower(x)
        if len(x) != 1:
            print "'" + x + "'" " is not a valid input."
            print player + " input only single alphabet."
            return ghost()
        
        if not any(word in s for s in wordlist):
            print player + " loses because no word begins with " + "'" + word + "'" + "."
            player_choose()
            print player + " wins!"
            print ""
            word = ""
            return ghost()
            
        if word in wordlist and len(word) >= 3:
            player_choose()
            print player + " loses because " + "'" + word + "'" + " is a word."
            player_choose()
            print player + " wins!"
            print ""
            word = ""
            player_choose()
            return ghost()
        else :
            player_choose()
            return ghost()


if __name__ == '__main__':
    ghost()

        
            
        

