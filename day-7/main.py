import random

from hangman_art import stages, logo
from hangman_words import word_list

print(logo)

chosen_word = random.choice(word_list)

lives = 6

display = []
for _ in range(len(chosen_word)):
    display += '_'
print(display)

end_of_game = False
while not end_of_game:
    guess = input('Guess a letter: ').lower()

    if guess in display:
        print(f'You have already guessed {guess}')

    if guess not in chosen_word:
        print(f"Your guessed {guess} is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print('You lose!')
            end_of_game = True

    for index in range(len(chosen_word)):
        letter = chosen_word[index]
        if letter == guess:
            display[index] = letter

    print(f"{' '.join(display)}")

    if '_' not in display:
        print('You win!')
        end_of_game = True

    print(stages[lives])
