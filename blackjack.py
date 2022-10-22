############### Blackjack Project #####################

# Imported files/modules
import random
import blackjack_art

logo = blackjack_art.logo

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

######################################################################


# list of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Function
def deal_cards():
    deal_cards = random.choice(cards)
    return deal_cards


def calculate_score(input_cards):
   if sum(input_cards) == 21 and len(input_cards) == 2:
       return 0

   if 11 in input_cards and sum(input_cards) < 21:
       cards.remove(11)
       cards.append(1)

   return sum(input_cards)


def compare(user_total, computer_total):
    if user_total == computer_total:
        return "Draw"
    elif computer_total == 0:
        return "You lose, opponent has Blackjack"
    elif user_total == 0:
        return "You Win, with BlackJack"
    elif user_total > 21:
        return "You went over 21, you lose"
    elif computer_total > 21:
        return "Opponent went over, You win"
    elif user_total > computer_total:
        return 'You Win'
    else:
        return "You Lose"

def blackJack() :
    print(logo)

    user_cards = []
    computer_cards = []

    continuePlay = True

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())


    while continuePlay is True:
        user_total = calculate_score(user_cards)
        computer_total = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_total}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_total == 0 or computer_total == 0 or user_total > 21:
          continuePlay = False
        else:
          user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
          if user_should_deal == "y":
              user_cards.append(deal_cards())
          else:
              is_game_over = True

    while computer_total != 0 and computer_total < 17:
        computer_cards.append(deal_cards())
        computer_total = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_total}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_total}")
    print(compare(user_total, computer_total))

while input("Do you want to play a game of BlackJack: Type 'y' or 'n'").lower() == "y":
    blackJack()


