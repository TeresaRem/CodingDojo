var Deck = function Deck(){
  this.deck = [];
  this.reset();
}

var Boot = function Boot(){
  this.deck = [];
}

Boot.prototype.reset = function(){
  // adds four decks to the boot
}

Deck.prototype.reset = function(){
  this.deck = [];
  var suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds'];
  var pips = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King'];

  for(var suit in suits){
    for(var pip in pips){
      var card = new Card(pips[pip], suits[suit]);
      this.deck.push(card);
    }
  }
  return this;
}
Deck.prototype.shuffle = function(){
  var m = this.deck.length, t, i;

  // While there remain elements to shuffle…
  while (m) {

    // Pick a remaining element…
    i = Math.floor(Math.random() * m--);

    // And swap it with the current element.
    t = this.deck[m];
    this.deck[m] = this.deck[i];
    this.deck[i] = t;
  }

  return this;
}
Deck.prototype.deal = function(){
  return this.deck.pop();
}

var Player = function Player(name){
  this.name = name;
  this.hand = [];
}

Player.prototype.draw = function(deck){
  this.hand.push(deck.deal());
  return this;
}
Player.prototype.discard = function(){
  this.hand = [];
  return this;
}

var Card = function Card(pip, suit){
  this.suit = suit;
  this.pip = pip;
  this.string = pip + ' of ' + suit;
}

var mydeck = new Deck();
var player1 = new Player('Brendan');

mydeck.reset().shuffle();

// player1.draw(mydeck).draw(mydeck);

console.log(mydeck);
