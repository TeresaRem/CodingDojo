//
//  ViewController.swift
//  I_WANT_TO_PLAY_MY_STORYBOARDS
//
//  Created by Jennifer Zeller on 9/7/16.
//  Copyright © 2016 Alex. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    var poem = ["I want to play my storyboards",
                "All over the Apple App Store",
                "And let my objects sing a song no one has heard before"]
    var pageCount = 0
    @IBOutlet weak var poemLabel: UILabel!
    @IBAction func nextButtonPressed(sender: AnyObject) {
        if pageCount < poem.count - 1{
            pageCount+=1
        } else{
            pageCount = 0
        }
        poemLabel.text = poem[pageCount]
        
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        poemLabel.text = poem[0]
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

