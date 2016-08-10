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
        self.cards=[]
        suits = ['s','h','d','c']
        types = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        for card_suit in suits:
            for card_value in types:
                self.cards.append(Card(card_suit, card_value))
        return self

    def shuffle(self):
        if len(self.cards)>1:
            i=len(self.cards)-1
            while i > 0:
                s = random.randint(0,i)
                self.cards[i],self.cards[s] = self.cards[s], self.cards[i]
                i-=1

    def deal(self):
        if len(self.cards)==0:
            return false
        else:
            return self.cards.pop()
    def show_Deck(self):
        for i in self.cards:
            i.displayCard()
        return self
class Player(object):
    def __init__(self,name):
        self.name = name
        self.hand = []
    def draw(self, deck):
        card = deck.deal()
        if card:
            self.hand.append(card)
        else:
            print "no cards in deck"
        return self
    def discard(self):
        self.hand.pop()
    def show_hand(self):
        for i in self.hand:
            i.displayCard()
##-------------------
##CODE BELOW EXECUTES
##-------------------

Elliot_deck = Deck()

Elliot_deck.shuffle()

print "Cards in Deck:", len(Elliot_deck.cards)
ricky = Player("ricky")

##Ricky draws cards here 3 times
ricky.draw(Elliot_deck).draw(Elliot_deck).draw(Elliot_deck)

print "---------------------"
print "Below is Ricky's Hand:"
print "---------------------"


ricky.show_hand()
print len(ricky.hand), "Cards in Ricky's hand, shown above."



print "---------------------"
print "Cards in Deck:", len(Elliot_deck.cards)
print "---------------------"
print "below is the new deck"



Elliot_deck.build()
print len(Elliot_deck.cards)
