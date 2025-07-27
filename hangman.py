#Hangman Game
import random
randomWords = [
  "apple", "velocity", "quantum", "umbrella", "zebra",
  "lantern", "whistle", "echo", "marble", "galaxy",
  "crimson", "ripple", "tornado", "frost", "plasma"
]
word = random.choice(randomWords)
# print(word)
blank = ""

for i in word:
    blank += "_"

print(blank)
tries = 1
correctLetters = []
while tries <= 10:
    display = ""
    guess = input("Guess one letter: ")
    for letter in word:
        if letter == guess.lower():
            display += guess
            correctLetters.append(guess)
        elif letter in correctLetters:
            display += letter
        else:
            display += "_"
    print(display)
    if "_" not in display:
        break
    tries += 1
finalWord = input("Guess the final word: ")
if finalWord.lower() == word:
    print("You won, the word is indeed", word)
else:
    print("You lost the actual word is: ", word)

    


    
