//
//  DetailsViewController.swift
//  elliotslist
//
//  Created by Jennifer Zeller on 9/20/16.
//  Copyright © 2016 Alex. All rights reserved.
//

import UIKit

class DetailsViewController: UITableViewController {
    
    weak var cancelButtonDelegate:CancelButtonDelegate?
    weak var delegate: DetailsViewControllerDelegate?
    
    @IBOutlet weak var taskText: UITextField!
    
    @IBAction func doneButtonPressed(sender: UIBarButtonItem) {
        delegate?.detailsViewController(self, didFinishAddingTask: taskText.text!)
    }
    @IBAction func cancelButtonPressed(sender: UIBarButtonItem) {
        cancelButtonDelegate?.cancelButtonPressedFrom(self)
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        tableView.reloadData()
    }
}

