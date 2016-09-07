//: Playground - noun: a place where people can play

import UIKit

var str = "Hello, playground"
str += "you are so cool"

// this works

print("yes")

var name: String = "Anakin"
var num: Int = -42
var dec: Double = 4.2
let ice_cream = "mint"

var mutableString = "change"
let immutableString = "never change"
mutableString += "!"

var array = ["one"]
let array2 = ["uno"] // get error if you try to append
array.append("two")
array + ["three","four"]

var dict = ["one":1]
let dict2 = ["uno":1]
dict["one"] = 0
dict["two"] = 2

var type: String = "Rectangle"
var description: String = "A quadrilateral with four right angles"

var width: Double = 5
var height: Double = 10.5
var area: Double = width * height

height+=1
width+=1

area = width * height
// Note how you can "interpolate" variables into Strings using the following syntax
print("The shape is a \(type) or \(description) with an area of \(area)")

print("The maximum value \(Int.max)")
print("The minimum value \(Int.min)")
print("The maximum value \(Int32.max)")
print("The minimum value \(Int32.min)")
print("The maximum value \(UInt32.max)")
print("The minimum value \(UInt32.min)")
