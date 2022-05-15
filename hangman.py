maxWongAnswers = 10

def drawHangman(wrongAnswerCount):
    if (wrongAnswerCount == 0):
        print("   _______  ")
        print("   |     |  ")
        print("         |  ")
        print("         |  ")
        print("         |  ")
        print("         |  ")
        print("        / \ ")
    elif (wrongAnswerCount == 1):
        print("   _______  ")
        print("   |     |  ")
        print("   O     |  ")
        print("         |  ")
        print("         |  ")
        print("         |  ")
        print("        / \ ")    
    elif (wrongAnswerCount == 2):
        print("   _______  ")
        print("   |     |  ")
        print("   O     |  ")
        print("   |     |  ")
        print("   |     |  ")
        print("         |  ")
        print("        / \ ")
    elif (wrongAnswerCount == 3):
        print("   _______  ")
        print("   |     |  ")
        print("   O     |  ")
        print("  \|     |  ")
        print("   |     |  ")
        print("         |  ")
        print("        / \ ")
    elif (wrongAnswerCount == 4):
        print("   _______  ")
        print("   |     |  ")
        print("   O     |  ")
        print("  \|/    |  ")
        print("   |     |  ")
        print("         |  ")
        print("        / \ ")
    elif (wrongAnswerCount == 5):
        print("   _______  ")
        print("   |     |  ")
        print("   O     |  ")
        print(" ‾\|/    |  ")
        print("   |     |  ")
        print("         |  ")
        print("        / \ ")
    elif (wrongAnswerCount == 6):
        print("   _______  ")
        print("   |     |  ")
        print("   O     |  ")
        print(" ‾\|/‾   |  ")
        print("   |     |  ")
        print("         |  ")
        print("        / \ ")
    elif (wrongAnswerCount == 7):
        print("   _______  ")
        print("   |     |  ")
        print("   O     |  ")
        print(" ‾\|/‾   |  ")
        print("   |     |  ")
        print("  /      |  ")
        print("        / \ ")
    elif (wrongAnswerCount == 8):
        print("   _______  ")
        print("   |     |  ")
        print("   O     |  ")
        print(" ‾\|/‾   |  ")
        print("   |     |  ")
        print("  / \    |  ")
        print("        / \ ")
    elif (wrongAnswerCount == 9):
        print("   _______  ")
        print("   |     |  ")
        print("   O     |  ")
        print(" ‾\|/‾   |  ")
        print("   |     |  ")
        print(" _/ \    |  ")
        print("        / \ ")
    else:
        print("   _______  ")
        print("   |     |  ")
        print("   O     |  ")
        print(" ‾\|/‾   |  ")
        print("   |     |  ")
        print(" _/ \_   |  ")
        print("        / \ ")

def getSecretWord():
    secretWord = input("What is the secret word? ").lower()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    return secretWord

def getInitialFilledInWord(secretWord):
    return "_" * len(secretWord)

def getSortedList(items):
    sortedList = list(items)
    sortedList.sort()
    return sortedList

def getLetterGuess():
    letterGuess = input("What is your letter guess? ").lower()
    return letterGuess

def isLetterInWord(letterGuess, secretWord):
    return secretWord.find(letterGuess) >= 0

def getUpdatedFilledInWord(guessedLetters, secretWord):
    filledInWord = ""
    for letter in secretWord:
        if (letter in guessedLetters):
            filledInWord += letter
        else:
            filledInWord += "_"
    return filledInWord

def main():
    print("Hangman")
    #get secret word
    secretWord = getSecretWord()
    filledInAnswer = getInitialFilledInWord(secretWord)
    wrongAnswerCount = 0
    guessedLetters = set()
    while ((filledInAnswer != secretWord) and (wrongAnswerCount < maxWongAnswers)):
        #draw everything
        print("")
        drawHangman(wrongAnswerCount)
        print(f"guessed letters: {getSortedList(guessedLetters)}")
        print(f"current answer: {filledInAnswer}")
        #get letter guess
        letterGuess = getLetterGuess()
        if (letterGuess in guessedLetters):
            print(f"'{letterGuess}' was already guessed!")
            continue
        guessedLetters.add(letterGuess)
        letterInWord = isLetterInWord(letterGuess, secretWord)
        if (letterInWord):
            #if the letter is in the word, fill in the matching spaces
            filledInAnswer = getUpdatedFilledInWord(guessedLetters, secretWord)
        else:
            #if the letter is not in the word, add to the hangman body
            wrongAnswerCount += 1

    print("")
    drawHangman(wrongAnswerCount)
    if (filledInAnswer == secretWord):
        print(f"YOU WIN! You guessed '{secretWord}'")
    else:
        print(f"YOU LOSE! The word was '{secretWord}'")

if __name__ == '__main__':
    main()