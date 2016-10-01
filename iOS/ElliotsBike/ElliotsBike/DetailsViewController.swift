//
//  DetailsViewController.swift
//  ElliotsBike
//
//  Created by Jennifer Zeller on 9/23/16.
//  Copyright © 2016 Alex. All rights reserved.
//

import UIKit
import CoreData

class DetailsViewController: UIViewController, CancelButtonDelegate,DoneButtonDelegate,EditViewControllerDelegate{
    
    func EditViewControllerD(controller: DetailsViewController, didFinishEditingBike bike: Bike){
        scraperBikeLabel.text = bike.name!

    }

    
    @IBAction func cancelButtonPressed(sender: UIBarButtonItem) {
        cancelButtonDelegate?.cancelButtonPressedFrom(self)
    }
    
    weak var cancelButtonDelegate: CancelButtonDelegate?
    var bikeName:String?
    var elliotBike:UIImage?
    var thisBike:Bike?

    override func viewDidLoad() {
        super.viewDidLoad()
        scraperBikeImage.image = elliotBike
        scraperBikeLabel.text = thisBike!.name!
    }
    

    @IBOutlet weak var scraperBikeLabel: UILabel!
    
    @IBOutlet weak var scraperBikeImage: UIImageView!
    
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        if segue.identifier == "editEntry"{
            let navigationController = segue.destinationViewController as! UINavigationController
            // assign top view controller
            let controller = navigationController.topViewController as! EditViewController
            
            // set variables (ACCORDING TO ELLIOT) to details view controller
            controller.cancelButtonDelegate = self
            controller.doneButtonDelegate = self
            controller.editViewControllerDelegate = self
            controller.elliotBike = elliotBike
            controller.bikeName = bikeName
            controller.thisBike = thisBike
        }
    }
    
    func cancelButtonPressedFrom(controller: UIViewController) {
        dismissViewControllerAnimated(true, completion: nil)
    }
    
    func doneButtonPressedFrom(controller:UIViewController) {
        // change name and picpath for elliot's scraper bike
        if bikeName != nil && scraperBikeLabel.text != ""{
            let bike = NSEntityDescription.insertNewObjectForEntityForName("Bike", inManagedObjectContext: managedObjectContext) as! Bike
            bike.picpath = NSBundle.mainBundle().pathForResource("3", ofType: "jpg")
            bike.name = scraperBikeLabel.text
            save()
        }
        dismissViewControllerAnimated(true, completion: nil)
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
