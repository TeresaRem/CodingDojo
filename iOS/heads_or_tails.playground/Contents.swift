import UIKit


func tossCoin() -> String {
    var C = ""
    print ("Tossing a Coin!")
    let result = arc4random_uniform(2)
    if result == 0 {
        C += "Heads"
    } else{
        C += "Tails"
    }
    print(C)
    return C
}

func tossMultipleCoins(num:Int) -> Double {
    var count = 0.0
    for _ in 1...num{
        let coin = tossCoin()
        if coin == "Heads"{
            count+=1
        }
    }
    let ratio:Double = count/Double(num)
    print(ratio)
    return ratio
}

tossMultipleCoins(5)
 