// problem 1
console.log("problem 1")
console.log(first_variable);
var first_variable = "Yipee I was first!";
function firstFunc() {
  first_variable = "Not anymore!!!";
  console.log(first_variable);
}
console.log(first_variable);

// my answer
console.log("my answer")

var first_variable = undefined;
function firstFunc() { // this isn't invoked
  first_variable = "Not anymore!!!";
  console.log(first_variable); 
}
console.log(first_variable); // returns undefined
first_variable = "Yipee I was first!";

console.log(first_variable); // returns i was first

// problem 2
console.log("problem 2")
var food = "Chicken";
function eat() {
  food = "half-chicken";
  console.log(food);
  var food = "gone";       // CAREFUL!
  console.log(food);
}
eat();
console.log(food);

// my answer
var food = undefined;
function eat() {
  var food = undefined;
  food = "half-chicken";
  console.log(food);
  food = "gone";       // CAREFUL!
  console.log(food);
}
food = "Chicken";
eat();              // returns half-chicken, gone
console.log(food); // returns chicken

// problem 3
console.log("problem 3")
var new_word = "NEW!";
function lastFunc() {
  new_word = "old";
}
console.log(new_word);

// my answer
var new_word;
function lastFunc() {
  new_word = "old";
}
new_word = "NEW!";
console.log(new_word); // NEW!






