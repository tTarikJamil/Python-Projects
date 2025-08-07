import random
from art import logo
def del_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)
def compare(u_score, c_score):
    if c_score == u_score:
        print("It's Draw")
    elif c_score == 0:
        print("User loses")
    elif u_score == 0:
        print("User win")
    elif u_score > 21:
        print("User loses")
    elif c_score > 21:
        print("Computer loses")
    elif u_score > c_score:
        print("You win")
    else:
        print("You loses")
def play_game():
    print(logo)
    user_cards = []
    user_score = -1
    computer_cards = []
    computer_score = -1
    is_game_over = False
    for _ in range(2):
        user_cards.append(del_card())
        computer_cards.append(del_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your Cards = {user_cards},current Score = {user_score}")
        print(f"Computer first Cards = {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card or type 'n' to pass")
            if user_should_deal == "y":
                user_cards.append(del_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(del_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand:{user_cards},Final score{user_score}")
    print(f"Computer final hand:{computer_cards},Final score{computer_score}")
    compare(user_score, computer_score)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("/n"*20)
    play_game()
