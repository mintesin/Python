from art import logo,vs
from game_data import data
import os
import random

# picking the celebrities from the given data
def pick_celebrity(data):
  celebrity=[]
  for i in range(2):
    chosen_celebrity=random.choice(data)
    celebrity.append(chosen_celebrity)
  return celebrity #returns list of two dictionaries of the selected celebrity

def play(data):
  game_over=False
  score=0
  while not game_over:
    print(logo)
    chosen_celebrity=pick_celebrity(data)
    # picking celebrities
    A=chosen_celebrity[0]
    B=chosen_celebrity[1]
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
    # comparing the chosen celebrity and the unchosen one
    choice=input("Who has more followers: ")
    if choice=='A' and A['follower_count']<=B['follower_count']:
      game_over=True
      print(f"Your score is {score} ")
    elif choice=='B' and B['follower_count']<=A['follower_count']:
      game_over=True
      print("Your score is zero")

    elif choice=='A' and A['follower_count']>B['follower_count']:
      score +=1
      print(f"Your score is {score}")
    elif choice=='B' and B['follower_count']>A['follower_count']:
      score+=1
      print(f"Your score is {score}")
    else: game_over=True
    os.system('clear')









play(data)
