Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... 
... print("Welcome to the rock paper and scissors!")
... print("--------------------------------------")
... 
... options = ["Rock", "Paper", "Scissors"]
... 
... for attempt in range(3):
...   input(f"Choose from {options} ")
...   player = input("My choice is ")
...   computer = random.choice(options)
...   computer_choice = random.choice(options)
...   print(computer_choice)
... 
... if player == computer:
...   print("It's a draw!")
... if player == "Rock" and computer == "Scissors":
...   print("You win!")
... elif player == "Paper" and computer == "Rock":
...   print("You win!")
... elif player == "Scissors" and computer == "Paper":
...   print("You win!")
... else:
...   print("Computer wins!")
...   
... play_again_input = input("Do you want to play again? (yes/no) ")
... play_again = play_again_input == "yes"
... 
... if play_again_input.lower() != "yes":
...   print("Game over!")
... else:
