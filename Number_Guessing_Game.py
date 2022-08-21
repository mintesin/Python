import random

print("Please welcome to the number guessing Game")
print("I am thinking of a number between 1 and 100")
levels={'easy':5,'hard':10}
for level in levels:
  print(level)
level=input("Please choose the level: ")
number_ranges=list(range(1,100))
chosen_number=random.choice(number_ranges)

# print(chosen_number)
# print(number_ranges)

def play_the_game(levels):
  num_trails=0
  while num_trails<levels[level]:
    guess_number=int(input("Guess the number I am thinking: "))
    if guess_number>chosen_number:
      print("Too high")
      print("Guess again")
    elif guess_number<chosen_number:
      print("Too low")
      print("Guess again")
    else:
      print("you guessed it right")
      exit()

    num_trails +=1
play_the_game(levels)












