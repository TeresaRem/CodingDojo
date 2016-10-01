//
//  DetailsViewControllerDelegate.swift
//  elliotslist
//
//  Created by Jennifer Zeller on 9/20/16.
//  Copyright © 2016 Alex. All rights reserved.
//

import Foundation
protocol DetailsViewControllerDelegate: class {
    func detailsViewController(controller: DetailsViewController, didFinishAddingTask mission: String)
}
