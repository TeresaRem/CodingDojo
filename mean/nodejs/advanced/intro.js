// function myOriginalFunction(){
//   console.log('hello');
// }

// function invokedFunction(callback){
//   var x = setInterval(function(){
//     callback();
//   }, 4000)
// }

// invokedFunction(myOriginalFunction);
// invokedFunction(function(){console.log('world')});



// console.log("NOW: ");
// console.log("Declaring and assigning variable 'ninja'.");
// var ninja = 'Libby';

// setTimeout( function myCallbackFunction(){
//   console.log("LATER: ")
//   console.log(ninja, "LATER"); }, 2000
// );

// console.log("Printing ninja value.");
// console.log(ninja, "NOW");



function makePasta(pasta, makeSauce) {
  console.log("Boiling water");
  console.log("Putting " + pasta + " pasta in the water");
  // create a variable for sauce!
  var sauce = makeSauce();          // invoke makeSauce, our callback
  console.log("Mixing sauce");
  console.log("Pasta is done!");
  return pasta + " Pasta with " + sauce + " sauce! Voila!";
}
function makePesto() {
  console.log("Making Pesto");
  return "pesto";
}
function makeAlfredo() {
  console.log("Making Alfredo");
  return "alfredo";
}


// we pass the whole makePesto recipe to makePasta!
console.log(makePasta("Penne", makePesto));


// notice lack of parentheses after makeAlfredo.
// Remember: we want to pass the function, not execute it and pass a return value.
console.log(makePasta("Farfalle", makeAlfredo));
