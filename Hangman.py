import random
hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
wordList = ['apple', 'ball', 'cat']
randomWord = wordList[random.randint(0, 2)].lower()
print("_"*len(randomWord))

outputWord = []
for letter in range(len(randomWord)):
    outputWord.append("_")
k=0

for j in range(11):
    guessLetter = input("Guess a letter: ").lower()
    wrongNumber = 0
    for i in range(len(randomWord)):

        if randomWord[i]==guessLetter:

            #print(outputWord)

            outputWord[i]=guessLetter
            wrongNumber = 0
        else:
            wrongNumber +=1
            print(j)
    if wrongNumber==len(randomWord):
        print(hangman[k])
        k+=1

    display =''.join(outputWord)
    print(display)
    if display == randomWord:
        print("You guessed it correct.")
        break
print(f"The correct word is {randomWord}")
