Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import random

def blank_field():
    print(f"{field[0]}, {field[1]}, {field[2]}")
    print(f"{field[3]}, {field[4]}, {field[5]}")
    print(f"{field[6]}, {field[7]}, {field[8]}")

print("Welcome to the tic-tac-toe!")
print("-----------------------------")

while True:
    field = [" " for _ in range(9)]
    player_counter = 0
    computer_counter = 0

    for attempt in range(3):
        blank_field()

        computer = "X"
        player = "O"

        player_choice = int(input(f"Choose a number 0-8 to insert {player}: "))

        if field[player_choice] == " ":
            field[player_choice] = player
            blank_field()

            computer_choice = random.randint(0, 8)
            while field[computer_choice] != " ":
                computer_choice = random.randint(0, 8)


            field[computer_choice] = computer
            print("Computer choice is ", computer_choice)


    if player_counter > computer_counter:
        print("You win!")
    elif player_counter < computer_counter:
        print("Computer wins!")
    else:
        print("It's a draw!")

    play_again_input = input("Do you want to play again? (yes/no) ")

    if play_again_input.lower() != "yes":
        print("Game over!")
        break
    else:
        print("Let's try again!!")
