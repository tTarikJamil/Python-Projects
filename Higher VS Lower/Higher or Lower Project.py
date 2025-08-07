import random
from art import logo, vs
from game_deta import data
# Higher or Lower Game
def from_account(account):
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return f"{account_name} a {account_desc} from {account_country}"

# Function to check if the guess is correct
# It compares the follower counts of two accounts and checks if the guess matches the account with more followers.
def check_answer(User_guess, a_follower, b_follower):
    if a_follower > b_follower:
        return User_guess == 'a'
    else:
        return User_guess == 'b'
print(logo)
game_is_on = True
account_a = random.choice(data)
account_b = random.choice(data)
score = 0
# The game continues until the player makes an incorrect guess.
while game_is_on:
    if account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A: {from_account(account_a)}")
    print(vs)
    print(f"Against B: {from_account(account_b)}")
    ask_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen for a better user experience
    print("\n" * 20)
    print(logo)
    
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(ask_guess, a_follower_count, b_follower_count)
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_is_on = False
        


