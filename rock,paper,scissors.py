import random

while True:
  plays = ["rock", "paper", "scissors"]
  computer_action = random.choice(plays)
  player_action = input("Choose a play(rock, papper, scissors):")
  print(f"\nPlayer 1 choose {player_action} and computer you pick a {computer_action}.")
  
  if player_action == computer_action:
    print("its a tie.")
  elif player_action == "rock":
    if computer_action == "scissors":
      print(f"You win player 1, rock beats scissors!")
    else:
      print("You lose player 1, rock beats scissors.")
  elif player_action == "paper":
    if computer_action == "scissors":
      print("Player 1 you lose, scissors beats paper.")
    else:
      print("Computer you lose, scissors beats paper.")
  elif player_action == "paper":
    if computer_action =="rock":
      print("Player 1, you win paper beats rock.")
  else:
      print("Computer you lose, paper beats rock")

  play_again =input("play again? (y/n)")
  if play_again.lower != "y":
    break
  
    