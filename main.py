# Rock Paper and Scissors Game
import random

# User input
print("It's your turn\nChoose: \nR for Rock\nP for Paper\nS for Scissor")
player = input()

computer = random.randint(1, 3)
# Assigning the Rock,Paper and Scissors to computer
if computer == 1:
    computer = 'R'
elif computer == 2:
    computer = 'P'
elif computer == 3:
    computer = 'S'


def game(player, computer):
    if player == computer:
        return None

    elif computer == 'S':
        if player == 'R':
            return True
        elif player == 'P':
            return False

    elif computer == 'R':
        if player == 'P':
            return True
        elif player == 'S':
            return False

    elif computer == 'P':
        if player == 'S':
            return True
        elif player == 'R':
            return False


print(f"Computer chose: {computer}")
print(f"You chose: {player}")

result = game(player, computer)
if result is None:
    print("The game is a tie!")
elif result:
    print("Hurray! You Won")
else:
    print("You Lose!")
