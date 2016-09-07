// var nums = [1,2,3,4]
// nums.append(5)
// print("\(nums[0..<nums.count])")
import UIKit
var numbers = Array(1...255)
// var one = arc4random_uniform(254) + 1;
// var two = arc4random_uniform(254) + 1;

// numbers[Int(one)-1] = Int(two)
// numbers[Int(two)-1] = Int(one)
// print(numbers)
var random: UInt32 = 0
var random2: UInt32 = 0
var temp = 0
for i in 0...99{
    random = arc4random_uniform(254) + 1;
    random2 = arc4random_uniform(254) + 1;
    temp = numbers[Int(random)-1]
    numbers[Int(random)-1] = numbers[Int(random2)-1];
    numbers[Int(random2)-1] = temp;
}

let answer = numbers.indexOf(42)
print("We found the answer to the ultimate question of life, the universe, and everything at index \(answer!)")

var present: String! = "Apple Watch"         // We don't have to unwrap to use the value,
print("\(present)")
present = nil                                // but we can still set it to nil.
print("\(present)")

var jerseyNumbers = [
    "Kobe": 24,
    "Lebron": 23,
    "Rondo": 9
]

if let jerseyNumber = jerseyNumbers["Kobe"]{
    print(jerseyNumber)
}

func printDescription(width w: Int, height h: Int) {
    print("My width is \(w) and my height is \(h)")
}
// SWIFT-LIKE because first parameter name is inside function name
func printDescriptionWithWidth(w: Int, andHeight h: Int) {
    print("My width is \(w) and my height is \(h)")
}
printDescriptionWithWidth(10, andHeight: 20)

func lookForSomethingIn(dictionary: [String: Int], forKey key: String) -> Int? {
    if let value = dictionary[key] {
        return value
    } else {
        return nil
    }
}
var jerseyNumber = lookForSomethingIn(jerseyNumbers, forKey: "Kobe")
if let num = jerseyNumber {
    print(num)
}

class Person {
    var species = "H. Sapiens"
    var name: String
    init(name: String) {   // Note this function doesn't get called explicitly. It is called
        // when creating an instance using initialization syntax -- "Person()".
        self.name = name     // Note use of "self" here to refer to the name property.
    }
    func speak() {
        print("Hello! I am a \(self.species) and my name is \(self.name)")
        // Note how we refer to the properties using "self".
    }
}
var myPerson: Person = Person(name: "Jay")   // Now we have to pass a param to Person initialization.
myPerson.speak()                             // Note we call method similar to how we access properties.
struct Card{
    var value:String
    var Suit:String
    var numerical_value:Int
}
var cards:[Card] = [Card]()
func buildDeck(){
    let suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    let values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    let value_card = ["A","2","3","4","5","6","7","8","9","10","J","Q", "K"]
    for suit in suits{
        for i in 0...12{
            cards.append(Card(value:value_card[i],Suit:suit,numerical_value:values[i]))
        }
    }
}

buildDeck()
print(cards)
