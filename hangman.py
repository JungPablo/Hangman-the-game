import random
import re
import os
import winsound

# function for check the local os and then clear the screen


def clear_screen():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


file_opnd = open('dbase.txt', 'r', encoding='utf-8')  # open dbase.txt
words = file_opnd.read()  # read dbase.txt into words

words1 = re.sub("[ :.]", " ", words)  # replace symbols by space
low_words1 = words1.lower()  # modify to lowercase
words2 = low_words1.split()  # modify words1 string to words2 list

# modify words2 list to dic_words dictionary
dic_words = {}
counter = 0
for i in words2:
    if counter == 0:
        dic_words[i] = ""
        ant_word = i
    elif counter % 2 != 0:
        dic_words[ant_word] = i
    else:
        ant_word = i
    counter += 1

s_time = 200
s_frec = 300
game_name = (' ---------------------\n'
            '|    H A N G M A N    |\n'
            ' ---------------------\n')

# start and continue the Hangman game while contn is 'y'
contn = 'y'
while contn == 'y' or contn == 'Y':
    pair_word = key, val = random.choice(
        list(dic_words.items()))  # get random key-value pair

    # ======================================================
    eng_word = pair_word[0]  # random english word (key)
    sp_word = pair_word[1]  # random spanish word (value)
    # ======================================================

    clear_screen()  # calling clear_screen() function
    tries = 0  # number of tries of a player
    letters = ''  # all entry chars of the player
    letter = ''  # letter of the player
    print(game_name)
    print('Guess the english word of next spanish word: '+sp_word)
    while True:  # infinit loop
        if tries == 0:
            print('Good Luck!')
        print('Tries: ', tries)
        guess = True
        for w in eng_word:  # print the letter/s and/or '_' from letters
            if w in letters:
                print(w, end=' ')
            else:
                print('_', end=' ')
                guess = False  # if no '_' means the player won
        if guess:  # player won
            print()
            clear_screen()
            print(game_name)
            print('Correct!: ', eng_word)
            print('You won! Congratulations!!')
            contn = input('One more time? (Y or N) ')  # play one more time?
            while contn != 'y' and contn != 'Y' and contn != 'n' and contn != 'N':  # wrong option
                winsound.Beep(s_frec, s_time)
                clear_screen()
                print('Wrong option. Please write a valid option...')
                contn = input('One more time? (Y or N) ')
            break  
        print()
        letter = input("Enter a letter :")  # input a letter
        # while letter is more than 1 or (letter in letters or letters ='')==> input error
        while len(letter) != 1 or letter in letters:
            winsound.Beep(s_frec, s_time)
            clear_screen()
            print(game_name)
            print('Guess the english word of next spanish word: '+sp_word)
            print('Please, input only one new letter ')
            print('Tries: ', tries)
            for w in eng_word:  # print the letter/s and/or '_' from letters
                if w in letters:
                    print(w, end=' ')
                else:
                    print('_', end=' ')
                    guess = False  # if no '_' means the player won
            print()
            letter = input("Enter a letter :")
        clear_screen()
        # show the random spanish word to the player
        print(game_name)
        print('Guess the english word of next spanish word: '+sp_word)
        if letter in eng_word:  # is the entry correct?
            print("Correct!")
            letters += letter # updating letters with new letter
        else:  # is the entry wrong?
            winsound.Beep(s_frec, s_time)
            print('Wrong')
        tries += 1  # increase nbr of tries
file_opnd.close()
clear_screen()
print(game_name)
print('Thanks for play Hangman')
