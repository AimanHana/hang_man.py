import random
import sys
import os
import nltk
#Starting with a list of secret words from the dictionary
nltk.downlaod('words') to download the words from the dictionary
from nltk.corpus import words
word_list = words.words()
tried = []
lives = 6
#pick up a random word from the list of secret words
secret_word = random.choice(word_list)
#display the number of letters in the secret word as underscores
guessed_word = ['_' for x in range(len(secret_word))]
print("""
 _                                              
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|  
                    __/ |                      
                   |___/ 
""")
print(' '.join(guessed_word))

while(lives>=0):
    guessed_letter = input("Enter a letter: ").lower()
    if guessed_letter and guessed_letter in secret_word and guessed_letter not in guessed_word:
        print('Correct Guess, well done.')
        for index in range(len(secret_word)):
            if secret_word[index] == guessed_letter:
                guessed_word[index] = guessed_letter
        print(' '.join(guessed_word))
    elif guessed_letter=='': #Checking if enter was pressed
        print('You need to enter a letter before pressing enter.')
    elif guessed_letter in guessed_word: # checking if the letter was choesn before
        print(' '.join(guessed_word))
        print('You chose that letter before.')
    elif guessed_letter in tried:
        print('You made that mistake before.')
    else:
        tried.append(guessed_letter)
        lives -= 1
        if lives == 5:
            cls = lambda: os.system('clear')
            cls()
            print("""
 _                                              
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|  
                    __/ |                      
                   |___/ 
""",end='')
            print("""
                -----------
                |         |
                |         O
                |
                |
                |
                |
            """)
            print(' '.join(guessed_word))
            print(f'Wrong letter. You have {lives} lives left.')
            print(f'You wrongly tried {tried} so far.')
           
        elif lives == 4:
            cls()
            print("""
 _                                              
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|  
                    __/ |                      
                   |___/ 
""")
            print("""
                -----------
                |         |
                |         O
                |         | 
                |         |
                |
                |
            """)
            print(' '.join(guessed_word))
            print(f'Wrong letter. You have {lives} lives left.')
            print(f'You wrongly tried {tried} so far.')
            
        elif lives == 3:
            cls()
            print("""
 _                                              
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|  
                    __/ |                      
                   |___/ 
""")
            print("""
                -----------
                |         |
                |         O
                |        /| 
                |         |
                |
                |
            """)
            print(' '.join(guessed_word))
            print(f'Wrong letter. You have {lives} lives left.')
            print(f'You wrongly tried {tried} so far.')
            
        elif lives == 2:
            cls()
            print("""
 _                                              
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|  
                    __/ |                      
                   |___/ 
""")
            print("""
                -----------
                |         |
                |         O
                |        /|\ 
                |         |
                |
                |
            """)
            print(' '.join(guessed_word))
            print(f'Wrong letter. You have {lives} lives left.')
            print(f'You wrongly tried {tried} so far.')
           
        elif lives == 1:
            cls()
            print("""
 _                                              
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|  
                    __/ |                      
                   |___/ 
""")
            print("""
                -----------
                |         |
                |         O
                |        /|\ 
                |         |
                |        /
                |
            """)
            print(' '.join(guessed_word))
            print(f'Wrong letter. You have {lives} lives left.')
            print(f'You wrongly tried {tried} so far.')
          
        elif lives == 0:
            cls()
            print("""
 _                                              
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|  
                    __/ |                      
                   |___/ 
""")
            print("""
                -----------
                |         |
                |         O
                |        /|\ 
                |         |
                |        / \\
                |
            """)
            print(' '.join(guessed_word))
            print(f'Wrong letter. You have {lives} lives left.')
            print(f'You wrongly tried {tried} so far.')
         
            print("""
                ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
                ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
                ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
                ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
                ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
                ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
                ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
                ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
                ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
                ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
                ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼            
            """)
            sys.exit()
          
    if '_' not in guessed_word:
        # print(' '.join(guessed_word))
        print('You guessed it right. Well done.')
        sys.exit() #quit() # exit() #This will terminate the program