//
//  snippetEditViewController.swift
//  snippet
//
//  Created by Elliot Young on 9/28/16.
//  Copyright © 2016 Elliot Young. All rights reserved.
//

import UIKit

class EditSnippetViewController: UIViewController, UITextViewDelegate{
    @IBOutlet weak var textViewText: UITextView!
    @IBOutlet weak var copiedToClipBoardView: UIView!
    @IBOutlet weak var titleTextField: UITextField!
    weak var editSnippetDelegate: EditSnippetDelegate?
    weak var cancelButtonDelegate: CancelButtonDelegate?
    var recievedSnippetTextToEdit:String?
    var recievedSnippetTitleToEdit:String?
    weak var snippetToEdit:Snippets?
    override func viewDidLoad() {
        super.viewDidLoad()
        KOKeyboardRow.applyToTextView(textViewText)
        textViewText.autocorrectionType = .No
        textViewText.autocapitalizationType = .None
        textViewText.becomeFirstResponder()
        textViewText.delegate = self
        copiedToClipBoardView.alpha = 0
        if recievedSnippetTextToEdit != nil{
            textViewText.text = recievedSnippetTextToEdit
            titleTextField.text = recievedSnippetTitleToEdit
        }
        super.viewDidLayoutSubviews()
        self.automaticallyAdjustsScrollViewInsets = false
    }
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    //
    //UI ACTIONS
    @IBAction func doneButtonPressed(sender: UIBarButtonItem) {
        if textViewText.text != ""{
            if recievedSnippetTextToEdit != nil{
                //Edits existing snippet
                editSnippetDelegate?.editSnippetDelegate(textViewText.text, editedSnippetTitle:titleTextField.text!, snippetToEdit: snippetToEdit!)
                print("Edited Snippet")
            }
            else{
                //Adds new snippet to core data if an existing note was not passed.
                editSnippetDelegate?.editSnippetDelegate(textViewText.text, newSnippetTitle: titleTextField.text!)
                print("Created Snippet")
                
            }
        }
        cancelButtonDelegate!.cancelButtonPressedFrom(self)
    }
    @IBAction func cancelButtonPressed(sender: UIBarButtonItem) {
        cancelButtonDelegate!.cancelButtonPressedFrom(self)

    }
    @IBAction func shareButtonPressed(sender: UIBarButtonItem) {
        animateCopiedToClipBoardView()
        pasteBoard.string = textViewText.text
    }
    //UI ACTIONS
    //
    //
    //ANIMATE FUNCTIONS
    func animateCopiedToClipBoardView(){
        copiedToClipBoardView.alpha = 1
        UIView.animateWithDuration(1,
                                   delay: 0.5,
                                   usingSpringWithDamping: 1,
                                   initialSpringVelocity: 10.0,
                                   options: [],
                                   animations: ({
                                    self.copiedToClipBoardView.alpha = 0
                                   }), completion: nil)
    }
    //ANIMATE FUNCTIONS
    //
}
