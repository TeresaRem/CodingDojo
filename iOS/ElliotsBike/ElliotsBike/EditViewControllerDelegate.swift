//
//  EditViewControllerDelegate.swift
//  ElliotsBike
//
//  Created by Jennifer Zeller on 9/23/16.
//  Copyright © 2016 Alex. All rights reserved.
//

import UIKit

protocol EditViewControllerDelegate: class{
    func EditViewControllerD(controller: UIViewController, didFinishEditingBike bike: Bike)
}
