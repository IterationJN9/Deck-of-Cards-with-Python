# Deck of Cards Program
# This program creates a Card class and a Deck class representing the standard 52-card playing deck.

# Card class requirements
# Each instance of Card should have a suit.
# Each instance of Card should have a value.
# Card's __repr__ method should display the card's value and suit.

class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def __repr__(self):
		return "{} of {}".format(self.value, self.suit)
		# Can use f string instead
		# return f"{self.value} of {self.suit}"

# Deck class requirements
# Each instance of Deck should have all 52 possible instances of Card.
# The count instance method should return a count of how many cards remain in the deck.
# The __repr__ method should return how many cards are in the deck.
# The _deal instance method should accept a number and remove that many cards from the end of the deck.
    # It might need to remove fewer if there are not enough cards in the deck.
    # If the deck is depleted then it should raise a ValueError message.
# The shuffle instance method should shuffle a value deck of cards and return a ValueError message if not full.
# The deal_card instance method should use the _deal method to deal a single card from the deck and return it.
# The deal_hand instance method should accept a number and use the _deal method to deal a list of cards from the deck and return that list.

from random import shuffle

class Deck:
	def __init__(self):
		suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
		values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        # List comprehension method to create all cards
		self.cards = [Card(value, suit) for suit in suits for value in values]

		# Nested loop method to create all cards
		# self.cards = []
		# for suit in suits:
		#	for value in values:
		#		self.cards.append(Card(value, suit))
		#		print self.cards

		

	#print(self.cards)

	# Define functions for the deck of cards

	def __repr__(self):
		return "Deck of {} cards".format(self.count())

	def count(self):
        return len(self.cards)
        
    def _deal(self, num):
        count = self.count()
        actual = min([count,num])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards
            
    def deal_card(self):
        return self._deal(1)[0]
            
    def deal_hand(self, hand_size):
        return self._deal(hand_size)
            
    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
                
        shuffle(self.cards)
        return self