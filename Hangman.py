import random
import hangmanWords
import hangmanArt
k=0
while True:
    print(hangmanArt.logo)
    wordList = hangmanWords.word_list
    randomWord = random.choice(wordList)
    print("_"*len(randomWord))
    print(randomWord)
    outputWord = []
    for letter in range(len(randomWord)):
        outputWord.append("_")


    for j in range(7):
        guessLetter = input("Guess a letter: ").lower()
        wrongNumber = 0
        for i in range(len(randomWord)):
            print(j)
            if randomWord[i]==guessLetter:
                if j==0:
                    pass
                else:
                    j=j=j-1
                print(j,"loop")
                #print(outputWord)
                if guessLetter in outputWord:
                    print(f"You have entered the letter '{guessLetter}' already")
                outputWord[i]=guessLetter
                wrongNumber = 0

            else:
                wrongNumber +=1
                j=k


        if wrongNumber==len(randomWord):
            print(f"'{guessLetter}' is not a letter in the word" )
            print(k, "K")
            print(j,"j")
            print(hangmanArt.hangman[k]+"\n\n")
            k=k+1


        display =''.join(outputWord)
        print(display)
        if display == randomWord:
            print("You guessed it correct.")
            break
    print(f"The correct word is **{randomWord}**")
    repeatGame = input("Do you want to continue the game?\nPress 'y' for yes and 'n' for no").lower()
    if repeatGame == 'n':
        break
