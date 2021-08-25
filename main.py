#importing function and modules
import random
from hangman import stages, logo
from words import word_list
# printing the logo from hangman module
print(logo)
game_is_finished = False
# seting the lives left for the user to finish the game
lives = len(stages) - 1
# randomly selecting the words from words module
chosen_word = random.choice(word_list)
# geting the length of the chosen_word
word_length = len(chosen_word)
# declaring empty list
display = []
# looping through the word_lenght to display "_" in the console
for _ in range(word_length):
    display += "_"
# main loop for the game
while not game_is_finished:
    # user guessing the words and geting them in lower case
    guess = input("Guess a letter: ").lower()
    # if the user already guessed the word means print the message
    if guess in display:
        print(f"You've already guessed {guess}")
    # if the user guessed right letter then displaying them
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")
    # if the user guessed wrong letter printing the message and reduceing the lives left
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        # if the user loose all lives GAME OVER
        if lives == 0:
            game_is_finished = True
            print("You lose.")
    # if user guessed the word correctly then finishing the game WIN
    if not "_" in display:
        game_is_finished = True
        print("You win.")
    # printing the hangman ASCII art
    print(stages[lives])



