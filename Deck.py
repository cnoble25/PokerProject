import Card
import random


# this class represents the deck which cards are pulled from in poker
# list methods used: pop, shuffle, len
# list comprehension used in __init__ method to create the 52 cards
# for i in range used in __init__ method inside the list comprehension
# for i in list used in print deck method to individually print each object in the deck
# tuples used: suits (the suits that exist in poker)
class Deck:
    suits = ("spades", "clubs", "hearts", "diamonds")

    def __init__(self):
        self.all_cards = [Card.Card(i, x) for x in self.suits for i in range(2, 15)]

    def get_deck(self):
        return self.all_cards

    def print_deck(self):
        for x in self.all_cards:
            print(x.get_name())

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_card(self):
        Top_Card = self.all_cards[0]
        self.all_cards.pop(0)
        if len(self.all_cards) == 0:
            print("all cards have been pulled")
            return
        else:
            return Top_Card
