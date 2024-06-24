import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock, paper, scissors]

your_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game[your_choice])

random_choice = random.randint(0, 2)
print("Computer chose:")
print(game[random_choice])

if (your_choice == 0 and random_choice == 2) or (your_choice == 1 and random_choice == 0) or (your_choice == 2 and random_choice == 1):
    print("You win!")
elif your_choice == random_choice:
    print("It's a draw!")
else:
    print("You lose!")
