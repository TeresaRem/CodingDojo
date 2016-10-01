//
//  ViewController.swift
//  StarWarsEncyclopedia
//
//  Created by Jennifer Zeller on 9/19/16.
//  Copyright © 2016 Alex. All rights reserved.
//

import UIKit

class FilmViewController: UITableViewController {
    var films = [String]()
    override func viewDidLoad() {
        super.viewDidLoad()
        StarWarsModel.getAllFilms() { // Notice how we are passing a block to the function (this becomes "completionHandler" in the function definition in StarWarsModel.swift)
            data, response, error in
            do {
                // Try converting the JSON object to "Foundation Types" (NSDictionary, NSArray, NSString, etc.)
                if let jsonResult = try NSJSONSerialization.JSONObjectWithData(data!, options: NSJSONReadingOptions.MutableContainers) as? NSDictionary {
                    if let results = jsonResult["results"] {
                        let resultsArray = results as! NSArray
                        for i in 0..<resultsArray.count{
                            self.films.append(resultsArray[i]["title"] as! String)
                        }
                        dispatch_async(dispatch_get_main_queue(), {
                            self.tableView.reloadData()
                        })
                    }
                }
            } catch {
                print("Something went wrong")
            }
        }
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    ///////////////////////////////////
    //Function that recursively appends ALL the star wars people into our people array
    ///////////////////////////////////
    func appendAllToArrayGivenUrl(url:String){
        if let url = NSURL(string: url) {
            let session = NSURLSession.sharedSession()
            let task = session.dataTaskWithURL(url, completionHandler: {
                data, response, error in
                // We get data, response, and error back. Data contains the JSON data, Response contains the headers and other information about the response, and Error contains an error if one occured
                // A "Do-Try-Catch" block involves a try statement with some catch block for catching any errors thrown by the try statement.
                do {
                    // Try converting the JSON object to "Foundation Types" (NSDictionary, NSArray, NSString, etc.)
                    if let jsonResult = try NSJSONSerialization.JSONObjectWithData(data!, options: NSJSONReadingOptions.MutableContainers) as? NSDictionary {
                        if let results = jsonResult["results"] {
                            let resultsArray = results as! NSArray
                            for i in 0...(resultsArray.count-1){
                                self.films.append(resultsArray[i]["title"] as! NSString as String)
                            }
                            dispatch_async(dispatch_get_main_queue(), {
                                self.tableView.reloadData()
                            })
                            // 10 at a time
                            print(self.films.count)
                            if let nextone = jsonResult["next"] as? String! {
                                self.appendAllToArrayGivenUrl(nextone)
                            }
                        }
                    }
                    self.tableView.reloadData()
                } catch {
                    print("Something went wrong")
                }
            })
            task.resume()
        }
    }
    ///////////////////////////////////
    //
    ///////////////////////////////////
    
    ///////////////////////////////////
    //Functions that populate the table
    ///////////////////////////////////
    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // return the count of people
        return films.count
    }
    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        // Create a generic cell
        let cell = UITableViewCell()
        // set the default cell label to the corresponding element in the people array
        cell.textLabel?.text = films[indexPath.row]
        // return the cell so that it can be rendered
        return cell
    }
    ///////////////////////////////////
    //
    ///////////////////////////////////
}