from build_auction import logo
print(logo)
bids = {}
continue_biding= True
while continue_biding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if should_continue == "no":
        continue_biding = False
        winner = max(bids,key=bids.get)
        print(f"The winner is {winner} with a bid of {bids[winner]}")
    else:
        print("\n" * 20)

