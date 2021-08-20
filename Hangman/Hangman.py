import random
import hangmanWords
import hangmanArt


while True:
    random_word = random.choice(hangmanWords.word_list)
    list_random_word = list(random_word)
    position = -1
    display_list = list("_" * (len(random_word)))

    display_string = ''
    lives = 7
    count = 0
    while lives > 0:
        guess_letter = input("Guess the letter: ")
        for position, letter in enumerate(list_random_word):
            if letter == guess_letter:
                display_list[position] = guess_letter
        display_string = ''.join(display_list)
        if random_word.find(guess_letter) == -1:
            print(f"You gussed it wrong. No '{guess_letter}' in this word")
            print(hangmanArt.hangman[count])
            count += 1
            if count == 7:
                print("Sorry, you loose")
            lives -= 1
        else:
            print(f"You guessed it right. You have uncovered letter'{guess_letter}'")
        if random_word == display_string:
            print("You got it correctly")
        print(display_string)
    print(f"The correct word is: '{random_word}' ")
    play = input("Press any key to continue. Press 'n' to exit").lower()
    if play == 'n':
        break

# k=0
# while True:
#     print(hangmanArt.logo)
#     wordList = hangmanWords.word_list
#     randomWord = random.choice(wordList)
#     print("_"*len(randomWord))
#     print(randomWord)
#     outputWord = []
#     for letter in range(len(randomWord)):
#         outputWord.append("_")
#
#
#     for j in range(7):
#         guessLetter = input("Guess a letter: ").lower()
#         wrongNumber = 0
#         for i in range(len(randomWord)):
#             print(j)
#             if randomWord[i]==guessLetter:
#                 if j==0:
#                     pass
#                 else:
#                     j=j=j-1
#                 print(j,"loop")
#                 #print(outputWord)
#                 if guessLetter in outputWord:
#                     print(f"You have entered the letter '{guessLetter}' already")
#                 outputWord[i]=guessLetter
#                 wrongNumber = 0
#
#             else:
#                 wrongNumber +=1
#                 j=k
#
#
#         if wrongNumber==len(randomWord):
#             print(f"'{guessLetter}' is not a letter in the word" )
#             print(k, "K")
#             print(j,"j")
#             print(hangmanArt.hangman[k]+"\n\n")
#             k=k+1
#
#
#         display =''.join(outputWord)
#         print(display)
#         if display == randomWord:
#             print("You guessed it correct.")
#             break
#     print(f"The correct word is **{randomWord}**")
#     repeatGame = input("Do you want to continue the game?\nPress 'y' for yes and 'n' for no").lower()
#     if repeatGame == 'n':
#         break
