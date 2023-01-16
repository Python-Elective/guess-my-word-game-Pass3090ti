
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "word_list.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Reading word_list file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # word_list: list of strings
    word_list = line.split()
    print(len(word_list), "words found")
    return word_list

def choose_word(word_list):
    """
    word_list (list): list of words (strings)

    Returns a word from word_list at random
    """
    return random.choice(word_list)

# end of helper code
# -----------------------------------

# Load the list of words into the variable word_list
# so that it can be accessed from anywhere in the program
word_list = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for letter in secret_word:
      if letter not in letters_guessed:
        return False
    return True


### Testcases
#print(is_word_guessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']))
# print(is_word_guessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))
# print(is_word_guessed('pineapple', []))



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    full_word = ''
    for letter in secret_word:
      if letter in letters_guessed:
        full_word += letter
        
      else: 
        full_word += " _ "
    return full_word
    
    
    
      
#Testcases
#print(get_guessed_word('apple', ['e', 'i', 'k', 'p', 'r', 's']))
# print(get_guessed_word('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u']))

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...   
    
    import string
    alphabet = string.ascii_lowercase

    """ Pseudocode
    for every letter in letters_guessed
      .replace the letter in the alphabet with empty string


    
    convert alphabet to list
    for every letter in letters_guessed
    .remove that letter from the alpha_list
    return string of joined characters in alpha_list

    alpha_list = list(alphabet)
    alpha_list.remove(,,,,,,,,,,,)
    return ''*join(,,,,,)

    for every letter in the alphabet
      if the letter is not guessed yet i.e. it is available 
      keep adding the water
    """
    for letter in letters_guessed:

        if letter in alphabet:

          alphabet = alphabet.replace(letter,'')

    return alphabet    



#Testcases 
#print( get_available_letters(['e', 'i', 'k', 'p', 'r', 's']) )
  
def game_loop(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game.

    * At the start of the game, let the user know how many 
      letters the secret_word contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''


    # While True: # game loop

    # True: # game loop

    #   if lives < 1:
    #     Game over you're dead'
    #     break

    #   if number_of_enemies == 0:
    #     Game over You Win 
    #     break 
    
    guess_remaining = 8
    letter_guessed = []

    print('Let the game begin!')
    print('I am thinking of a word with' ,len(secret_word), 'letter')

    while is_word_guessed(secret_word, letter_guessed) == False:
      print ('You have ', guess_remaining, ' guesses remaining.')
      print ('Letters available to you: ', get_available_letters(letter_guessed))
      inputLetters = input('Guess a letter: ')
      if inputLetters in get_available_letters(letter_guessed):
        letter_guessed.append(inputLetters)
        if (inputLetters in secret_word):
          print('Correct: ', get_guessed_word(secret_word, letter_guessed))
          print('')
        else:
          print('Incorrect, this letter is not in my word: ', get_guessed_word(secret_word, letter_guessed))
          print('')
          guess_remaining -= 1
      else:
        print('You fool! You tried this letter already: ', get_guessed_word(secret_word, letter_guessed))
        print('')
      if guess_remaining == 0:
        break
        
    if is_word_guessed(secret_word, letter_guessed) == True:
      print('YOU WIN! XD')
    else: 
      print('GAME OVER! THE WORD IS', secret_word)

def main():
    secret_word = choose_word(word_list)
    game_loop(secret_word)

# Testcases
# you might want to pick your own
# secret_word while you're testing


if __name__ == "__main__":
    main()