from numpy import random
class User:
    from numpy import random
    """
    A User class that includes:
    an initializer method with the definition def __init__(self) .
    a private __probability attribute to represent the probability of clicking on an ad. When a
    user is created, the secret probability is drawn from a uniform distribution from 0 to 1.
    (Please use the random or numpy.random modules)
    a show_ad method with the definition def show_ad(self) that represents showing an ad
    to this User . This method should return True to represent the user clicking on and ad and
    False otherwise.
    """
    def __init__(self):
        """
        constructor method that initializes a User instance
        """
        from numpy import random
        self.__probability = random.uniform(0, 1)
        
    def show_ad(self):
        """
        simulates a user clicking on the ad on the user's own probability of clicking the ad
        """
        click = random.uniform(0, 1)
        if click <= self.__probability:
            return True
        return False
    
class Auction:
    from numpy import random
    """
    An Auction class that includes:
    an initializer with the definition def __init__(self, users, bidders) . Here, users is
    expected to contain a list of all User objects. bidders is expected to contain a list of all
    Bidder objects.
    an execute_round method with the header def execute_round(self) . This method
    should execute all steps within a single round of the game.
    a balances attribute, which contains a dictionary of the current balance of every Bidder
    """
    def __init__(self, users, bidders):
        """
        constructor method that initializes an Auction instance
        """
        self.users = users
        self.bidders = bidders
        self.balances = {bidder: 0 for bidder in bidders}
        
    def execute_round(self):
        """
        plays each step in the auction and bidding cycle
        """
        chosen_user = random.randint(0, len(self.users))
        
        all_bids = {}
        for bidder in self.bidders:
            all_bids[bidder] = bidder.bid(chosen_user)
        
        #looks through all the bids and finds the winning bid and highest bid
        highest_bid = 0   
        winning_price = 0
        for bidder, bid in all_bids.items():
            if bid > highest_bid:
                winning_price = highest_bid
                highest_bid = bid
            elif bid > winning_price:
                winning_price = bid
        
        #randomly selects a winner in the event of a tiebreaker
        winners = [bidder for bidder, bid in all_bids.items() if bid == max(all_bids.values())]
        winner = winners[random.randint(0, len(winners))]
        
        clicked = self.users[chosen_user].show_ad()
        
        #notifies the winner and losers
        for bidder in self.bidders:
            if bidder == winner:
                bidder.notify(True, winning_price, clicked)
                self.balances[bidder] -= winning_price
                if clicked:
                    self.balances[bidder] += 1
            else:
                bidder.notify(False, winning_price, clicked)
        
                                 