import random

class Card(object):
    def __init__(self, suit, number):
        self.suit=suit
        self.number=number
        self.visib=False

    def flip(self):
        if self.visib==True:
            self.visib=False
        else:
            self.visib=True
        return self

    def displayCard(self):
        print self.suit, str(self.number)
        return ""


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()
    def build(self):
        suits = ['s','h','d','c']
        types = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        for card_suit in suits:
            for card_value in types:
                self.cards.append(Card(card_suit, card_value))
                # print card_suit, card_value
        return self
    def shuffle(self):
        random.shuffle(self.cards)
        return self
    def deal(self, player):
        player.hand.append(self.cards[-1])
        print type(player.hand)
        for i in player.hand[i]:
            
        # print player.hand
        self.cards.pop()
        return self

class Player(object):
    def __init__(self,name):
        self.name = name
        self.hand = []
    def draw(self,deck):
        self.hand = deck.deal(self)
        return self
    def discard(self):
        self.hand.pop()
        print type(self.hand)
        return self

Deck1 = Deck()

Deck1.shuffle() #Deck.shuffle()

ricky = Player('ricky')

Deck1.deal(ricky).deal(ricky)

# ricky.draw(Deck1)