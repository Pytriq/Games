# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings
    of lowercase letters.
    
    Depending on the size of the word list, this function
    may take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed
    so far
    returns: boolean, True if all the letters of secretWord
    are in lettersGuessed; False otherwise
    '''
    done = False
    guess = ''
    for l in lettersGuessed:
        if l in secretWord:
            guess += l
    if len(guess) == len(secretWord):
        done = True
    return done
    #one liners
    #return set(list(secretWord)).issubset(set(lettersGuessed))
    #return all(c in lettersGuessed for c in secretWord)
    #return set(secretWord).issubset(lettersGuessed)
    #return not(set(secretWord) - set(lettersGuessed))



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed 
    so far
    returns: string, comprised of letters and underscores
    that represents what letters in secretWord
    have been guessed so far.
    '''
    word = ''
    i = 0
    for c in secretWord:
        if i >= len(secretWord):
            break
        if secretWord[i] in lettersGuessed:
            word = word + secretWord[i]
        else:
            word += ' _ '
        i += 1
    
    return word
    
    ''' One liner'''
    #return "".join(c if c in lettersGuessed else "_ " for c in secretWord)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been 
    guessed so far
    returns: string, comprised of letters 
    that represents what letters have not
      yet been guessed.
    '''
    letters = string.ascii_lowercase #alphabet letters, az
    available_letters = ''
    for i in letters:
        if i not in lettersGuessed:
            available_letters = available_letters + i
    return available_letters
    #one Liner
    return ''.join(c for c in 'abcdefghijklmnopqrstuvwxyz' if c not in lettersGuessed)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter)
    per round.

    * The user should receive feedback immediately
    after each guess about whether their guess appears 
    in the computers word.

    * After each round, you should also display
    to the user the partially guessed word so far, 
    as well as letters that the 
    user has not yet guessed.

    Follows the other limitations detailed 
    in the problem write-up.
    '''
    turns, lettersGuessed, won = 8, [], False

    
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(len(secretWord)))
    
    while not won:
        print("------------")
        if secretWord == getGuessedWord(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            won = True
        else:
            print("You have {} guesses left".format(turns))
            print("Available letters:", getAvailableLetters(lettersGuessed))
            guess = input("Please guess a letter: ")
            if guess in lettersGuessed:
                print("Oops! You've already guessed that letter:",
                      getGuessedWord(secretWord, lettersGuessed))
            else:
                lettersGuessed.append(guess.lower())
                if guess in secretWord:
                    print("Good guess:", 
                          getGuessedWord(secretWord,lettersGuessed))
                else:
                    print("Oops! That letter is not in my word:",
                        getGuessedWord(secretWord, lettersGuessed))
                    turns -= 1
                    if turns <= 0:
                        print("-----------")
                        print("Sorry! You ran out of moves. The word was:",
                              secretWord + ".")
                        break
                           


secretWord = chooseWord(wordlist).lower()
#secretWord = 'apple'
hangman(secretWord)
