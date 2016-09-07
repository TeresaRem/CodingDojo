import UIKit

struct Card{
    var value:String
    var Suit:String
    var numerical_value:Int
}

class Deck{
    var cards:[Card] = [Card]()
    init(){
        self.buildDeck()
    }
    
    func deal() -> Card{
        let top = self.cards.removeLast()
        return top
    }
    
    func reset(){
        self.cards.removeAll()
        self.buildDeck()
    }
    
    func buildDeck(){
        let suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        let values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        let value_card = ["A","2","3","4","5","6","7","8","9","10","J","Q", "K"]
        for suit in suits{
            for i in 0...12{
                self.cards.append(Card(value:value_card[i],Suit:suit,numerical_value:values[i]))
            }
        }
    }
    
    func shuffle(){
        var random: UInt32 = 0
        for _ in 0...104{
            random = arc4random_uniform(51);
            let top = self.cards.removeAtIndex(Int(random))
            self.cards.append(top);
        }
    }
}

class Player{
    var name:String
    var hand:[Card] = [Card]()
    init(name:String){
        self.name = name
    }
    func draw(deck:Deck) -> Card{
        let new_card = deck.deal()
        self.hand.append(new_card)
        return new_card
    }
    func discard(card:Card)->Bool{
        var count = 0
        if self.hand.count == 0 {
            return false
        }
        for card_in_hand in self.hand{
            if card_in_hand.numerical_value == card.numerical_value && card_in_hand.Suit == card.Suit {
                self.hand.removeAtIndex(count)
                return true
            }
            count+=1
        }
        return false
    }
}
var deck1:Deck = Deck()
deck1.shuffle()

var alex:Player = Player(name:"Alex")
// alex.draw(deck1)
alex.hand.append(Card(value:"A",Suit:"Spades",numerical_value:1))
alex.discard(Card(value:"A",Suit:"Spades",numerical_value:1))

