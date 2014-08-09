#Run on python 3.4.1

# This program simulates the hangman game. A word
# is chosen from a predefined list of five words.
# The player is given a max of 10 lives to
# guess the word correctly. Python controls the game.

import random

def pick_word():
    word_list = ['jurong','marina','lakeside','changi','clementi']
    list_length = len(word_list)
    #Choose a random word
    random_word = word_list[random.randint(0,list_length-1)]
    return random_word
    
def main():
    num_of_lives = 10
    word = pick_word()
    #print(word)
    word_length = len(word)
    #Initialize the output list to zeroes
    output_list = ['0']*word_length
    #Convert string to list for easier access
    word_in_list = list(word)
    #print(word_in_list)
    print("Word length = ",word_length)
    while(True):
        
        #Break if there are no more lives
        if num_of_lives==0:
            print("Sorry, Game over.")
            print("The word is",word)
            break

        #Break if the player has won
        print(output_list)
        if '0' not in output_list:
            print("You win!")
            break
        
        input_letter = input("Guess the letter")
        if input_letter not in word_in_list:
            print("Letter not in the word.")
            num_of_lives -= 1
        else:
            #Use enumerate to iterate over the list and find matches
            for i, item in enumerate(word_in_list):
                if item == input_letter:
                    output_list[i] = word_in_list[i]
        print(output_list)
        print("Number of lives remaining = ",num_of_lives)
            
main()
