var mathlib = require('./mathlib')();     //notice the extra invocation parenthesis!
var a = mathlib.add(1,5);
var b = mathlib.multiply(5,6);
var c = mathlib.square(3);
console.log('a is',a)
console.log('b is',b)
console.log('c is',c)