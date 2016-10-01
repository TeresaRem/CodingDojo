//
//  ViewController.swift
//  chatchat
//
//  Created by Jennifer Zeller on 9/28/16.
//  Copyright © 2016 Alex. All rights reserved.
//

import UIKit
import SocketIO

class ViewController: UIViewController {
    
    @IBAction func updateButton(sender: UIButton) {
        self.socket.emit("username", withItems: [self.usernameField.text!.stringByReplacingOccurrencesOfString("\n", withString: "<br>")])
        self.usernameField.text = ""
    }
    
    @IBOutlet weak var usernameField: UITextField!
    @IBOutlet weak var chatView: UITextView!
    @IBOutlet weak var sendButton: UIButton!
    @IBOutlet weak var sendField: UITextView!
    
    let socket = SocketIOClient(socketURL: NSURL(string: "http://localhost:8080")!, config: [.Log(true), .ForcePolling(true)])
    
    override func viewDidLoad() {
        super.viewDidLoad()
        addHandlers()
        self.socket.connect()
        self.chatView.layoutManager.allowsNonContiguousLayout = false

    }
    
    override func viewWillAppear(animated: Bool) {
        let bottom = chatView.contentSize.height
        
        chatView.setContentOffset(CGPoint(x: 0, y: bottom), animated: true) // Scrolls to end

    }
    
    @IBAction func sendButton(sender: UIButton) {
        self.socket.emit("chat message", withItems: [self.sendField.text!.stringByReplacingOccurrencesOfString("\n", withString: "<br>")])
        self.sendField.text = ""
    }
    
    func addHandlers() {
        self.socket.on("connect") {data, ack in
            // self?.chatView.text?.appendContentsOf(replaced + "\n")
        }
        
        self.socket.on("chat message") {[weak self] data, ack in
            if let value = data.first as? String {
                let replaced = (value as NSString).stringByReplacingOccurrencesOfString("<br>", withString: "\n")
                self?.chatView.text?.appendContentsOf(replaced + "\n")
                let stringLength:Int = self!.chatView.text.characters.count
                self!.chatView.scrollRangeToVisible(NSMakeRange(stringLength-1, 0))
            }
        }
        
        self.socket.on("total users") {[weak self] data, ack in
            if let value = data.first as? String {
                let replaced = (value as NSString).stringByReplacingOccurrencesOfString("<br>", withString: "\n")
                self?.chatView.text?.appendContentsOf(replaced + "\n")
                let stringLength:Int = self!.chatView.text.characters.count
                self!.chatView.scrollRangeToVisible(NSMakeRange(stringLength-1, 0))
            }
        }
    }
}

