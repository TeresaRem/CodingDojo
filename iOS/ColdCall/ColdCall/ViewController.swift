//
//  ViewController.swift
//  ColdCall
//
//  Created by Jennifer Zeller on 9/7/16.
//  Copyright © 2016 Alex. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var nameLabel: UILabel!
    @IBOutlet weak var numberLabel: UILabel!
    @IBAction func callButton(sender: UIButton) {
        // logic for person to call
        if nameLabel.text == namesBank[Int(currentName)]{
            currentName = arc4random_uniform(4)
            nameLabel.text=namesBank[Int(currentName)]
        } else{
            nameLabel.text=namesBank[Int(currentName)]
        }
        // logic for number
        numberLabel.text = numbers[Int(currentNumber)]
        numberLabel.hidden = false
        if numberLabel.text == "1" || numberLabel.text == "2" {
            numberLabel.textColor = UIColor.redColor()
        } else if numberLabel.text == "3" || numberLabel.text == "4" {
            numberLabel.textColor = UIColor.orangeColor()
        } else{
            numberLabel.textColor = UIColor.greenColor()
        }
        // get random person and number
        currentName = arc4random_uniform(4)
        currentNumber = arc4random_uniform(5)
    }
    let namesBank = [
        "Elliot",
        "Phil",
        "Sonny",
        "Alex"
    ]
    let numbers = [
        "1",
        "2",
        "3",
        "4",
        "5"
    ]
    var currentName = arc4random_uniform(4)
    var currentNumber = arc4random_uniform(6)

    override func viewDidLoad() {
        super.viewDidLoad()
        nameLabel.text = "Ready?"
        numberLabel.hidden = true
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

}

