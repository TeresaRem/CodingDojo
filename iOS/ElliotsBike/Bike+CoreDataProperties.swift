//
//  Bike+CoreDataProperties.swift
//  ElliotsBike
//
//  Created by Jennifer Zeller on 9/23/16.
//  Copyright © 2016 Alex. All rights reserved.
//
//  Choose "Create NSManagedObject Subclass…" from the Core Data editor menu
//  to delete and recreate this implementation file for your updated model.
//

import Foundation
import CoreData

extension Bike {

    @NSManaged var name: String?
    @NSManaged var picpath: String?

}
