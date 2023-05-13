# learned dictionary , nesting lists and dictionaries
from art import logo
print(logo)
print("Welcome to the Silent bidding, place every bid.")
bids = {}
def add_bid(name, bid):
  bids[name] = bid

all_bids_placed = False
while not all_bids_placed:
  entry = input("What is your name? ")
  price = int(input("Place your bid. "))
  add_bid(entry, price)
  want_to_continue = input("Is there more bids? Type 'yes' or 'no'. ").lower()
  if want_to_continue == 'no':
    all_bids_placed = True

highest_bid = 0
winner = ""
for x in bids:
    if bids[x] > highest_bid:
        highest_bid = bids[x]
        winner = x
print(f"The winner is {winner} with a bid of {highest_bid}$.")