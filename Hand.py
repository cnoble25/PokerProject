# import main
import Deck
import Card


# this class represents the hand of 5 a player is given in poker
# list methods used: sort, reverse, insert, append
# no tuples used as all lists in this method have to be modified at some point
# method algorithims:
# rank: uses 10 separate methods each which checks one rank of a hand then returns true or false
# compare_hand: uses the rank method to check who wins if they have the same rank it does checking of each rank which checks
# which one has a greater hand as in higher cards then returns the one won wins with 1 or -1 or if they tie across the board them 0

class Hand:

    def __init__(self):
        self.delt_cards = []

    def get_hand(self):
        return self.delt_cards

    def print_hand(self):
        self.delt_cards.sort(key=getKey)
        self.delt_cards.reverse()
        for i in self.delt_cards:
            print(i.get_name())

    def add_card(self, card):
        self.delt_cards.insert(0, card)
        self.delt_cards.sort(key=getKey)
        self.delt_cards.reverse()

    def rank(self):
        if self.check_RF():
            return 9
        elif self.check_SF():
            return 8
        elif self.check_four():
            return 7
        elif self.check_FH():
            return 6
        elif self.check_flush():
            return 5
        elif self.check_S():
            return 4
        elif self.check_three():
            return 3
        elif self.check_two_pair():
            return 2
        elif self.check_pair():
            return 1
        else:
            return 0

    def check_RF(self):
        suit = [x.get_suit() for x in self.delt_cards]
        RF_60 = self.delt_cards[0].get_value() + self.delt_cards[1].get_value() + self.delt_cards[2].get_value() + \
                self.delt_cards[3].get_value() + self.delt_cards[4].get_value()
        if RF_60 == 60:
            if suit[0] == suit[1] and suit[0] == suit[2] and suit[0] == suit[3] and suit[0] == suit[4]:
                return True
            else:
                return False
        else:
            return False

    def check_S(self):
        i = self.delt_cards[0].get_value()
        if i == 14 and self.delt_cards[1].get_value() == 5:
            self.delt_cards[0].value = 1
        self.delt_cards.sort(key=getKey)
        self.delt_cards.reverse()
        i = self.delt_cards[0].get_value()
        if i - 1 == self.delt_cards[1].get_value() and i - 2 == self.delt_cards[2].get_value() and i - 3 == \
                self.delt_cards[3].get_value() and i - 4 == self.delt_cards[4].get_value():
            return True
        else:
            return False

    def check_SF(self):
        suit = [x.get_suit() for x in self.delt_cards]
        if self.check_S():
            if suit[0] == suit[1] and suit[0] == suit[2] and suit[0] == suit[3] and suit[0] == suit[4]:
                return True
            else:
                return False
        else:
            return False

    def check_four(self):
        value = [x.get_value() for x in self.delt_cards]
        if value[0] == value[3] or value[4] == value[1]:
            return True
        else:
            return False

    def check_FH(self):
        value = [x.get_value() for x in self.delt_cards]
        if value[0] == value[2] and value[3] == value[4] or value[2] == value[4] and value[1] == value[0]:
            return True
        else:
            return False

    def check_flush(self):
        suit = [x.get_suit() for x in self.delt_cards]
        if suit[0] == suit[1] and suit[0] == suit[2] and suit[0] == suit[3] and suit[0] == suit[4]:
            return True
        else:
            return False

    def check_three(self):
        value = [x.get_value() for x in self.delt_cards]
        if value[0] == value[2] or value[2] == value[4] or value[1] == value[3]:
            return True
        else:
            return False

    def check_two_pair(self):
        value = [x.get_value() for x in self.delt_cards]
        num_of_pairs = 0
        for x in range(len(value) - 1):
            if value[x] == value[x + 1]:
                num_of_pairs += 1
        if num_of_pairs > 1:
            return True
        else:
            return False

    def check_pair(self):
        value = [x.get_value() for x in self.delt_cards]
        num_of_pairs = 0
        for x in range(len(value) - 1):
            if value[x] == value[x + 1]:
                num_of_pairs += 1
        if num_of_pairs == 1:
            return True
        else:
            return False

    def get_hand_type(self):
        i = self.rank()
        if i == 9:
            return "Royal Flush"
        elif i == 8:
            return "Straight Flush"
        elif i == 7:
            return "Four-of-a-Kind"
        elif i == 6:
            return "Full House"
        elif i == 5:
            return "Flush"
        elif i == 4:
            return "Straight"
        elif i == 3:
            return "Three-of-a-kind"
        elif i == 2:
            return "Two Pair"
        elif i == 1:
            return "One Pair"
        elif i == 0:
            return f"High Card: \n{self.delt_cards[0].get_name()}"

    def compare_hand(self, hand):
        if hand.rank() > self.rank():
            return -1
        elif hand.rank() < self.rank():
            return 1
        elif hand.rank() == self.rank():
            if self.rank() == 8 or self.rank() == 4:
                if hand.delt_cards[4].value > self.delt_cards[4].value:
                    return -1
                elif hand.delt_cards[4].value < self.delt_cards[4].value:
                    return 1
                else:
                    return 0
            elif self.rank() == 7:
                if hand.delt_cards[2].value > self.delt_cards[2].value:
                    return -1
                elif hand.delt_cards[2].value < self.delt_cards[2].value:
                    return 1
                else:
                    return self.check_highest_card(hand)
            elif self.rank() == 3:
                if hand.delt_cards[2].value > self.delt_cards[2].value:
                    return -1
                elif hand.delt_cards[2].value < self.delt_cards[2].value:
                    return 1
                else:
                    return self.check_highest_card(hand)

            elif self.rank() == 5:
                return self.check_highest_card(hand)

            elif self.rank() == 6:
                if hand.delt_cards[2].value > self.delt_cards[2].value:
                    return -1
                elif hand.delt_cards[2].value < self.delt_cards[2].value:
                    return 1
                else:
                    return self.check_highest_card(hand)
            elif self.rank() == 0:
                return self.check_highest_card(hand)

            elif self.rank() == 2:
                self_pairs = self.check_pairs()
                hand_pairs = hand.check_pairs()
                for i in range(2):
                    if hand_pairs[i] > self_pairs[i]:
                        return -1
                    elif hand_pairs[i] < self_pairs[i]:
                        return 1
                return self.check_highest_card(hand)
            elif self.rank() == 1:
                self_pairs = self.check_pairs()
                hand_pairs = hand.check_pairs()
                for i in range(1):
                    if hand_pairs[i] > self_pairs[i]:
                        return -1
                    elif hand_pairs[i] < self_pairs[i]:
                        return 1
                return self.check_highest_card(hand)
            elif self.rank() == 9:
                return 0
            elif self.rank() == 0:
                return self.check_highest_card(hand)

    def check_pairs(self):
        pairs = []
        for i in range(4):
            if self.delt_cards[i].value == self.delt_cards[i + 1].value:
                pairs.append(self.delt_cards[i].value)
        pairs.sort()
        pairs.reverse()
        return pairs

    def check_highest_card(self, hand2):
        for i in range(4):
            if self.delt_cards[i].value > hand2.delt_cards[i].value:
                return 1
            elif self.delt_cards[i].value < hand2.delt_cards[i].value:
                return -1
        return 0


def getKey(obj):
    return obj.value
