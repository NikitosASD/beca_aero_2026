import random

# A class is like a template:
    # I can use that class to create an instance of the class called object, then I can use the instance
    # Each instance keeps track of its own state,
        # so I can update an instance created from a class and it won't impact other object created from the same class

class Card:
    """ Specifiy the suit and rank when a card object is constructed """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    


    def __str__(self):
            # It's called when print is invoked on an object from the class
                # When I print an object from the card class, it will print something
        return f"{self.rank["rank"]} of {self.suit}"
            # I use an "f string"






class Deck:
    def __init__(self):
        # The contents of this "__init__" method should be code that is run once to initialize the instance
        # All the methods or functions of this class should have a "self" argument (anything inside a () )
        # "self" represents the instance of the class
        # By using the "self" keyword, the function can access the attributes and methods of the class

        """ List of cards """
        self.cards = []
            # The "self" makes it so I can access it in other places
        suits = ["spades", "clubs", "hearts", "diamonds"]
        ranks = [
            {"rank": "A", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10}
        ]

        """ Makes a list of every card as "suit", {"rank": "x", "value": "y"} """
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
                    # I'm passing "Card" instances



    """ Function that shuffles the cards randomly """
    def shuffle(self):
        # With "self", it's going to get a reference to the instance
        if len(self.cards) > 1:
            # The "if" makes it so if there're more than 1 cards on the deck, it shuffles them
            random.shuffle(self.cards)



    """ Funtion that deals (gives) the last card of the deck """
    def deal(self, number):
        # I can still call this function with a single number but, with "self", it's also going to get a reference to the instance
        cards_dealt = []
        for x in range(number):
            if len(self.cards) > 0:
                # The "if" makes it so if there're cards on the deck, it gives one
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt
            # I have to use a "return" to use the "cards_dealt" variable outside the function






class Hand:
    def __init__(self, dealer = False):
        # The dealer's default value is set to False
        self.cards = []
        self.value = 0
            # Makes the hand keep track of the value of the hands
        self.dealer = dealer
    


    def add_card(self, card_list):
        self.cards.extend(card_list)
    


    """ Function that calculates the value of the hand """
    def calculate_value(self):
        self.value = 0
        has_ace = False
            # Starts the value at 0 and it hasn't an Ace

        """ Loop that sums the card values and checks if there is an Ace """
        for card in self.cards:
            card_value = int(card.rank["value"])
            self.value += card_value

            if card.rank["rank"] == "A":
                has_ace = True
        
        """ Condition that if theres an Ace and the hand value is over 21, it automaticaly counts the Ace as 1 """
        if has_ace and self.value > 21:
            self.value -= 10



    """ Method to get the hand value """
    def get_value(self):
        self.calculate_value()
            # The value I get may be incorrect, so first I calculate it before I return it
            # To call the "Hand" instance "calculate_value", I have to put a "self." before
        return self.value
        # It's a better practise to have a function to return the value because I may want some extra code to run in there
            # Depending on some conditions, I may want to modify the value before I return it
    


    """ Method to check if there's a blackjack """
    def is_blackjack(self):
        return self.get_value() == 21
            # Returns True or False depending the value is equal to 21 (blackjack)
    


    """ Displays the message depending of whether "self.dealer" is True or not """
    def display(self, show_all_dealer_cards = False):
        print(f"{"Dealer's" if self.dealer else "Your"} hand:")

        """ Loop to show all the cards unless:
                - It's the first dealer's card *and*
                - The argument show_all_dealer_cards isn't set to True (False) *and*
                - My hand is a blackjack (21) """
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer and not show_all_dealer_cards and not self.is_blackjack():
                print("hidden")
            else:
                print(card)
        
        """ Shows only the value of my hand """
        if not self.dealer:
            print("Value:", self.get_value())
        
        print()






class Game:
    def play(self):
        game_number = 0
        games_to_play = 0

        """ Loop that keeps asking how many games (it only accepts numbers) """
        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many games do you want to play? "))
            except:
                print("You must enter a number.")
        
        """ Loop that continues until it matches the number of games I wanted to play """
        while game_number < games_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer = True)

            """ Deals 2 cards to each player in turns """
            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))
            
            """ Leaves a space and adds a separator of *, then prints the game number and another separator """
            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)

            player_hand.display()
            dealer_hand.display()

            """ Condition that continues to the next game of the loop """
            if self.check_winner(player_hand, dealer_hand):
                continue
            
            """ The player has to decide whether to hit or stand *only* while he doesn't go over 21 or choose stand """
            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Please choose 'Hit' or 'Stand': ").lower()
                    # "lower()" converts the player's input to lower case no matter what
                print()
                
                """ Loops the question until the player decides something valid """
                while choice not in ["h", "s", "hit", "stand"]:
                    choice = input("Please enter 'Hit' or 'Stand' (or H/S): ").lower()
                    print()
                
                """ Adds a card when the player's choice is "hit" """
                if choice in ["hit", "h"]:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()
            
            if self.check_winner(player_hand, dealer_hand):
                continue
            
            """ Save the player's and dealer's hand value """
            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            """ While the dealer's hand is less than 17, it keeps adding cards to his hand """
            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal(1))
                dealer_hand_value = dealer_hand.get_value()
            
            """ After the dealer's stops adding his cards, it shows them (end of the game) """
            dealer_hand.display(show_all_dealer_cards = True)

            if self.check_winner(player_hand, dealer_hand):
                continue

            print("Final Results")
            print("Your hand:", player_hand_value)
            print("Dealer's hand:", dealer_hand_value)

            self.check_winner(player_hand, dealer_hand, True)

        print("\nThanks for playing")



    def check_winner(self, player_hand, dealer_hand, game_over = False):
        if not game_over:
            if player_hand.get_value() > 21:
                print("You busted. Dealer wins!")
                return True
            
            elif dealer_hand.get_value() > 21:
                print("Dealer busted. You win!")
                return True
            
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print("Both players have blackjack! Tie!")
                return True
            
            elif player_hand.is_blackjack():
                print("You have blackjack. You win!")
                return True
            
            elif dealer_hand.is_blackjack():
                print("Dealer has blackjack. Dealer wins!")
                return True
        
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("You win!")

            elif player_hand.get_value() == dealer_hand.get_value():
                print("Tie!")

            else:
                print("Dealer wins!")
            return True
        return False
                

g = Game()
g.play()