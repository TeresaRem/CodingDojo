//
//  ViewController.swift
//  chatchat
//
//  Created by Jennifer Zeller on 9/28/16.
//  Copyright © 2016 Alex. All rights reserved.
//

import UIKit
import SocketIO

class ChatViewController: UIViewController,UITextViewDelegate{
    
    @IBAction func updateButton(sender: UIButton) {
        self.socket.emit("username", withItems: [self.usernameField.text!.stringByReplacingOccurrencesOfString("\n", withString: "<br>")])
        self.usernameField.text = ""
    }
    
    @IBOutlet weak var usernameField: UITextField!
    @IBOutlet weak var chatView: UITextView!
    @IBOutlet weak var sendButton: UIButton!
    @IBOutlet weak var sendField: UITextView!
    @IBAction func pasteButtonPressed(sender: UIBarButtonItem) {
        sendField.text = pasteBoard.string
    }
    
    let socket = SocketIOClient(socketURL: NSURL(string: "http://192.168.1.150:8080")!, config: [.Log(true), .ForcePolling(true)])
    
    override func viewDidLoad() {
        super.viewDidLoad()
        sendField.autocorrectionType = .No
        sendField.autocapitalizationType = .None
        sendField.becomeFirstResponder()
        sendField.delegate = self
        addHandlers()
        self.socket.connect()
        self.chatView.layoutManager.allowsNonContiguousLayout = false
        chatView.editable = false
        
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

