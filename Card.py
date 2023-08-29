#this class represents the cards in a deck of 52 cards
#list methods used: non
#tuples used: 2 (one for the value list from printing the name, the other for the image file name)
class Card:
    value_list = (0, 0, "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace")
    value_list_file = (0, 0, "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace")

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

    def image_file_name(self):
        return f'{Card.value_list_file[self.value]}_of_{self.suit}.png'

    def get_name(self):
        return f'{Card.value_list[self.value]} of \n{self.suit}'
