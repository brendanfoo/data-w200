from numpy import random
class Bidder:
    from numpy import random
    """
    A Bidder class that includes:
    an initializer with the definition def __init__(self, num_users, num_rounds) , in which
    num_users contains the number of User objects in the game, and num_rounds contains the
    total number of rounds to be played. The Bidder might want to use this info to help plan its
    strategy.
    a bid method with the definition def bid(self, user_id) , which returns a non-negative
    amount of money, in dollars round to three (3) decimal places.
    a notify method with the definition def notify(self, auction_winner, price,
    clicked) , which is used to send information about what happened in a round back to the
    Bidder . Here, auction_winner is a boolean to represent whether the given Bidder won
    the auction ( True ) or not ( False ). price is the amount of the second bid, which the winner
    pays. If the given Bidder won the auction, clicked will contain a boolean value to
    represent whether the user clicked on the ad. If the given Bidder did not win the auction,
    clicked will always contain None .
    """
    def __init__(self, num_users, num_rounds):
        self.num_users = num_users
        self.num_rounds = num_rounds
        self.bidding_round = 0
        
    def bid(self, user_id):
        self.bidding_round += 1
        
        return random.randint(10, 100)
    
    def notify(self, auction_winner, price, clicked):
        print("Winning Price was", price)
        if auction_winner:
            if clicked:
                print("You won! The user clicked!")
            else:
                print("You won! The user did not click!")
        else:
            print("You did not win!")