Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... 
... print("Welcome to the tic-tac-toe!")
... print("-----------------------------")
... 
... for attempt in range(3):
...   def blank_board():
...     print("0, 1, 2")
...     print("3, 4, 5")
...     print("6, 7, 8")
... 
... blank_board()
... 
... player_counter = 0
... computer_counter = 0
... 
... for attempt in range(3):
...   computer = "X"
...   player = "O"
...   player = input(f"Choose the number 0-8 to inset X or O. ")
...   player_choice = int(player)
...   print("My choice is ", player_choice)
...   computer_choice = random.randint(0, 8)
...   print("Computer choice is ", computer_choice)
... 
... if computer == "X":
...   computer_counter += 1
... else:
...   player_counter += 1
... 
... if player_counter > computer_counter:
...   print("You win!")
... elif player_counter < computer_counter:
...   print("Computer wins!")
... else:
...   print("It's a draw!")
... 
... play_again_input = input("Do you want to play again? (yes/no) ")
... play_again = play_again_input == "yes"
... 
... if play_again_input.lower() != "yes":
...   print("Game over!")
... else:
