//
//  EditViewController.swift
//  ElliotsBike
//
//  Created by Jennifer Zeller on 9/23/16.
//  Copyright © 2016 Alex. All rights reserved.
//

import UIKit
import CoreData

class EditViewController: UIViewController{

    // this is your scratch pad
    let managedObjectContext = (UIApplication.sharedApplication().delegate as! AppDelegate).managedObjectContext

//    let bike = NSEntityDescription.insertNewObjectForEntityForName("Bike", inManagedObjectContext: managedObjectContext) as! Bike

    var bikeName:String?
    var elliotBike:UIImage?
    var imageToEdit:UIImage?
    var thisBike:Bike?

    
    weak var cancelButtonDelegate:CancelButtonDelegate?
    weak var doneButtonDelegate:DoneButtonDelegate?
    weak var editViewControllerDelegate:EditViewControllerDelegate?
    override func viewDidLoad() {
        super.viewDidLoad()
        // are we coming from the details page or creating a new object?
        if bikeName != nil{
            scraperBikeName.text = thisBike!.name!
            scraperBikeImage.image = elliotBike
        }else{
            // create new bike entity
            
        }
    }
    
    @IBOutlet weak var scraperBikeName: UITextField!
    
    
    @IBOutlet weak var scraperBikeImage: UIImageView!
    
    @IBAction func imageSelectPressed(sender: UIButton) {
    }
    
    @IBAction func cancelButtonPressed(sender: UIBarButtonItem) {
        cancelButtonDelegate?.cancelButtonPressedFrom(self)
    }
    
    @IBAction func doneButtonPressed(sender: UIBarButtonItem) {
        // change name and picpath for elliot's scraper bike
        if bikeName == nil && scraperBikeName.text != ""{
            let bike = NSEntityDescription.insertNewObjectForEntityForName("Bike", inManagedObjectContext: managedObjectContext) as! Bike
//            bike.picpath = NSBundle.mainBundle().pathForResource("3", ofType: "jpg")
            bike.name = scraperBikeName.text
            print("new entry created")
        }else{
            print("edited")
        }
        save()
        editViewControllerDelegate?.EditViewControllerD(self, didFinishEditingBike: thisBike!)
        doneButtonDelegate?.doneButtonPressedFrom(self)
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
