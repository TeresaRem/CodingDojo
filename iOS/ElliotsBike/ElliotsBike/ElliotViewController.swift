//
//  ViewController.swift
//  ElliotsBike
//
//  Created by Jennifer Zeller on 9/23/16.
//  Copyright © 2016 Alex. All rights reserved.
//

import UIKit
import CoreData

// global variable that our fetch() writes to
var bikes = [Bike]()

// our magic sratchpad
let managedObjectContext = (UIApplication.sharedApplication().delegate as! AppDelegate).managedObjectContext


class ElliotViewController: UITableViewController, CancelButtonDelegate, DoneButtonDelegate {
    
    // conform to CancelButtonDelegate protocol
    func cancelButtonPressedFrom(controller: UIViewController) {
        dismissViewControllerAnimated(true, completion: nil)
    }

    // conform to DoneButtonDelegate protocol
    func doneButtonPressedFrom(controller: UIViewController) {
        fetch()
        tableView.reloadData()
        dismissViewControllerAnimated(true, completion: nil)
    }


    override func viewDidLoad() {
        super.viewDidLoad()
        fetch()
        tableView.reloadData()
        print("number of entries:",bikes.count)
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    // required tableview function (defines the number of rows)
    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return bikes.count
    }
    
    // required tableview function (the cell at indexpath.row is defined by this function)
    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        // Returns a reusable table-view cell object located by its identifier.
        let cell = tableView.dequeueReusableCellWithIdentifier("scraperBike") as! ScraperBikeCell
//        cell.scraperBikeImage.image = UIImage(named: "\(indexPath.row)")
        cell.nameLabel.text = bikes[indexPath.row].name
        // return cell is required by this function
        return cell
    }
    
    // this lets us perform stuff if we select a row
    override func tableView(tableView: UITableView, didSelectRowAtIndexPath indexPath: NSIndexPath) {
        print("we got elliot's scraper bike")
    }
    
    // delete function
    override func tableView(tableView: UITableView, commitEditingStyle editingStyle: UITableViewCellEditingStyle, forRowAtIndexPath indexPath: NSIndexPath) {
        managedObjectContext.deleteObject(bikes[indexPath.row])
        save()
        fetch()
        tableView.reloadData()
    }
    
    // details button
    override func tableView(tableView: UITableView, accessoryButtonTappedForRowWithIndexPath indexPath: NSIndexPath) {
        // when you tap the accessory button, perform the segue
        performSegueWithIdentifier("entryDetails", sender: indexPath)
    }
    
    // runs right before perform segue
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        
        // use IS for class comparison
        if segue.identifier == "addEntry"{
            // assign navigation controller
            let navigationController = segue.destinationViewController as! UINavigationController
            // assign top view controller
            let controller = navigationController.topViewController as! EditViewController
            
            // set variables (ACCORDING TO ELLIOT) to details view controller
            controller.cancelButtonDelegate = self
            controller.doneButtonDelegate = self
        }
        if segue.identifier == "entryDetails"{
            // reference tapped cell, you must downcast sender (anyobject to nsindexpath) and downcast the cell (uitableviewcell to scraperbikecell)
            let cellTapped = tableView.cellForRowAtIndexPath(sender as! NSIndexPath) as! ScraperBikeCell
            // assign navigation controller
            let navigationController = segue.destinationViewController as! UINavigationController
            // assign top view controller
            let controller = navigationController.topViewController as! DetailsViewController
            
            // send OBJECT BIKE to details view controller
            controller.cancelButtonDelegate = self
            controller.elliotBike = UIImage(named: "\(sender!.row)")
            controller.bikeName = cellTapped.nameLabel.text!
            controller.thisBike = bikes[sender!.row]
        }
    }
    
    func fetch(){
        let bikeRequest = NSFetchRequest(entityName: "Bike")
        do {
            // get the results by executing the fetch request we made earlier
            let results = try managedObjectContext.executeFetchRequest(bikeRequest)
            // downcast the results as an array of Bike objects
            bikes = results as! [Bike]
            // print the details of each bike
            for bike in bikes {
                print("\(bike.name)")
                print("\(bike.picpath)")
            }
        } catch {
            // print the error if it is caught (Swift automatically saves the error in "error")
            print("\(error)")
        }
    }
    
    func save(){
        if managedObjectContext.hasChanges {
            do {
                try managedObjectContext.save()
                print("Success")
            } catch {
                print("\(error)")
            }
        }
    }
    

}

