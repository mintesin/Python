
import random
import os
user_cards = []
computer_cards = []
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score>21 and computer_score>21:
        return "You went over and you Loose"
    if computer_score==user_score:
        return "Draw"
    elif computer_score==0:
        return "Lose The opponent has black jack"
    elif user_score==0:
        return "Win with Blackjack"
    elif user_score>21:
        return "You went over You loose"
    elif computer_score>21:
        return "Opponent went over You win"
    elif user_score>computer_score:
        return "You win"
    else:
        return "You loose"


def play_game():
    user_cards=[]
    computer_cards=[]
    is_game_over=False
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
# If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"your cards are{user_cards} and your score is {user_score}")
        print(f'computer cards are {computer_cards} and computer score is {computer_score}')
        print(f"Compiter first card:{computer_cards[0]}")
        print(compare(user_score,computer_score))
 # If the game has not ended, ask the user if they want to draw another card.
        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal=input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal=='y':
                user_cards.append(deal_card())
            else:
                is_game_over=True
# Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score !=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)
        print(f"   Your final hand: {user_cards}, final score: {user_score}")
        print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(compare(user_score, computer_score))




# Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  # os.system('clear')
  play_game()














