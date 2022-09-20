import random
import sys
lives = 6
#Starting with a list of secret words
words = ['monkey','camel','mouse','baboon','tiger','lion','crocodile']
#pick up a random word from the list of secret words
secret_word = random.choice(words)
#display the number of letters in the secret word as underscores
guessed_word = ['_' for x in range(len(secret_word))]
print(' '.join(guessed_word))

while(lives>0):
    guessed_letter = input("Enter a letter: ").lower()
    if guessed_letter and guessed_letter in secret_word and guessed_letter not in guessed_word:
        for index in range(len(secret_word)):
            if secret_word[index] == guessed_letter:
                guessed_word[index] = guessed_letter
        print(' '.join(guessed_word))
    elif guessed_letter=='': #Checking if enter was pressed
        print('You need to enter a letter before pressing enter.')
    elif guessed_letter in guessed_word: # checking if the letter was choesn before
        print(' '.join(guessed_word))
        print('You chose that letter before.')
    else:
        lives -= 1
        print(' '.join(guessed_word))
        print(f'Wrong letter. You have {lives} lives left.')
        if lives == 5:
            print("""
                -----------
                |         |
                |         O
                |
                |
                |
                |
            """)
        elif lives == 4:
             print("""
                -----------
                |         |
                |         O
                |         | 
                |         |
                |
                |
            """)
        elif lives == 3:
            print("""
                -----------
                |         |
                |         O
                |        /| 
                |         |
                |
                |
            """)
        elif lives == 2:
            print("""
                -----------
                |         |
                |         O
                |        /|\ 
                |         |
                |
                |
            """)
        elif lives == 1:
            print("""
                -----------
                |         |
                |         O
                |        /|\ 
                |         |
                |        /
                |
            """)
        
          
    if '_' not in guessed_word:
        print(' '.join(guessed_word))
        print('You guessed it right. Well done.')
        sys.exit() #quit() # exit() #This will terminate the program
print("""
                -----------
                |         |
                |         O
                |        /|\ 
                |         |
                |        / \\
                |
            """)           
print('You ran out of lives. Game Over') 
 