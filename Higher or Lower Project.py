import random
from art import logo,vs
from game_data import data

def format_account(account):
    account_name = account["name"]
    account_description = account ["description"]
    account_country = account["country"]
    return f"{account_name} a {account_description} from {account_country}"

def check_difference(user_guess,follower_a,follower_b):
    if follower_a > follower_b:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
account_a = random.choice(data)
account_b = random.choice(data)
game_is_on = True
score = 0
while game_is_on:
    if account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A: {format_account(account_a)}")
    print(vs)
    print(f"Against B: {format_account(account_b)}")
    ask_question = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n" * 20)
    print(logo)
    follower_a_count = account_a["follower_count"]
    follower_b_count = account_b["follower_count"]
    is_correct = check_difference(ask_question,follower_a_count,follower_b_count)
    if is_correct:
        score+=1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_is_on = False
