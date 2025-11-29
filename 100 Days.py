#Day 9 - Secret Auction

print("Welcome to the secret auction.")
#Dictionary to store bidders and bids

#Creating a fuction to determine the highest bidder
def highest_bidder(bidding_dict):
    #Set initial highest amount to 0
    highest_amount = 0
    #For loop to go through each bidder in the bidding dictionary
    for bidder in bidding_dict:
        #Bid amount is retrieved from dictionary's key
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_amount:
            #If current bid amount is higher than highest amount, update highest amount and winner
            highest_amount = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_amount}")

    for i in bidding_dict:
        print(f"{name} bid ${bidding_dict[name]}")

bids = {}
#more_bidders act a flag to continue or stop the bidding process
more_bidders = True
highest_bid = 0
while more_bidders:
    name = input("What is your name?: ")
    amount = int(input("What is your bid?: $"))

    #bids dictionary updated with name and amount
    bids[name] = amount
    continue_bidding = input("Are there any other bidders? Type 'Yes' or 'No'.\n").lower()
    if continue_bidding == "yes":
        more_bidders = True
    else:
        more_bidders = False
        highest_bidder(bids)



