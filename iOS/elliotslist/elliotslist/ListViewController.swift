//
//  ViewController.swift
//  elliotslist
//
//  Created by Jennifer Zeller on 9/20/16.
//  Copyright © 2016 Alex. All rights reserved.
//

import UIKit

class ListViewController: UITableViewController, CancelButtonDelegate, DetailsViewControllerDelegate {
    var tasks = [String]()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        tasks.append("test")
        tableView.reloadData()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    // add two tableview controller methods
    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return tasks.count
    }
    
    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCellWithIdentifier("protoCell")!
        cell.textLabel?.text = tasks[indexPath.row]
        return cell
    }
    
    override func tableView(tableView: UITableView, commitEditingStyle editingStyle: UITableViewCellEditingStyle, forRowAtIndexPath indexPath: NSIndexPath) {
        tasks.removeAtIndex(indexPath.row)
        self.tableView.reloadData()
    }
    
    // cancel button delegate
    func cancelButtonPressedFrom(controller: UIViewController) {
        dismissViewControllerAnimated(true, completion: nil)
    }

    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // for addSegue
        if segue.identifier == "addSegue" {
            // assign destination controller
            let navigationController = segue.destinationViewController as! UINavigationController
            let controller = navigationController.topViewController as! DetailsViewController
            controller.cancelButtonDelegate = self
            controller.delegate = self
        }
    }
    
    func detailsViewController(controller: DetailsViewController, didFinishAddingTask mission: String) {
        dismissViewControllerAnimated(true, completion: nil)
        tasks.append(mission)
        tableView.reloadData()
    }
}

