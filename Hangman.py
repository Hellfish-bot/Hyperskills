import random

print("H A N G M A N")

def programme():
    option = input('Type "play" to play the game, "exit" to quit: ')
    if option == 'play':
        run_programme()
    elif option == 'exit':
        exit_programme()
    else:
        print('Not an option')

def run_programme(): 
    list_words = ['python', 'java', 'kotlin', 'javascript']
    word_choice = random.choice(list_words)
    hidden_word = list('-' * len(word_choice))
    lives = 8

    ascii_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    previous_choices = []
    
    while lives > 0:
        print('\n' + ''.join(hidden_word))
        if '-' not in hidden_word:
            print('You guessed the word!')
            print('You survived!')
            break
        letter = input('Input a letter: ')
        if len(letter) != 1:
            print('You should input a single letter')
        elif letter not in ascii_list:
            print('It is not an ASCII lowercase letter')
        elif letter in previous_choices and letter in ascii_list and len(letter) == 1:
            print('You already typed this letter')
        else:
            if letter in word_choice and letter not in hidden_word:
                for i in range(len(word_choice)):
                    if word_choice[i] == letter:
                        hidden_word[i] = letter
            elif letter in word_choice and letter in hidden_word:
                print('You already typed this letter')
            else:
                print('No such letter in the word')
                lives -= 1
        previous_choices.append(letter)
    else:
        print('You are hanged!')

def exit_programme():
    while True:
        break
    
programme()
