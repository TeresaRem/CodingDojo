function Card(suit, val){
	this.suit = suit;
	this.value = val;
	this.picture;
};


function Deck(){
	this.cards = [];
	this.shuffle = function(){
		this.cards.shuffle();
	};
	
	this.deal = function(){
		return this.cards.pop();
	};
	this.reset();
	
};

function Player(name){
	var hand = [];

	this.name = name;
	
	this.draw = function(deck){
		hand.push(deck.deal());
		return this;
	};
	this.discard = function(suit, value){
		for (var i = 0; i < hand.length; i++){
			if (hand[i].suit == suit && hand[i].value == value){
				hand[i] = hand[hand.length-1]
				hand.pop();
				return;
			}
		}
		console.log("Card not found");
	};
	this.showHand = function(){
		for (var i = 0; i < hand.length; i++){
			console.log(hand[i]);
		}
	};
};

Deck.prototype.reset = function(){
		var arrSuits = ["Hearts","Diamonds","Spades","Clubs"];
		var arrValues = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
		for (var j = 0; j < arrSuits.length; j++){
			for (var i = 0; i < arrValues.length; i++){
				this.cards.push(new Card(arrSuits[j], arrValues[i]));
			}
		}
		return this;
	};

Array.prototype.shuffle = function () {
  var k, t, len;

  len = this.length;

  if (len < 2) {
    return this;
  }

  while (len) {
    k = Math.floor(Math.random() * len--);
    t = this[k];

    while (k < len) {
      this[k] = this[++k];
    }

    this[k] = t;
  }

  return this;
};

var deck = new Deck();
deck.cards.shuffle();
console.log(deck.cards);
console.log("---------------------------------");
var Elliot = new Player();
Elliot.draw(deck).draw(deck).draw(deck).draw(deck).draw(deck);
Elliot.showHand();
console.log("---------------------------------");
Elliot.discard();
Elliot.showHand();









































