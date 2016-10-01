//
//  ViewController.swift
//  snippet
//
//  Created by Elliot Young on 9/27/16.
//  Copyright © 2016 Elliot Young. All rights reserved.
//

import UIKit
import CoreData
//Global Variables
let pasteBoard = UIPasteboard.generalPasteboard()
class SnippetListTableViewController: UITableViewController, EditSnippetDelegate, CancelButtonDelegate {
    //
    //OUTLETS
    @IBAction func newSnippetButtonPressed(sender: UIBarButtonItem) {
        self.performSegueWithIdentifier("editSnippetSegue", sender: sender)
    }
    //OUTLETS
    //
    //
    //VARIABLES
    let managedObjectContext = (UIApplication.sharedApplication().delegate as! AppDelegate).managedObjectContext
    var snippetsArray = [Snippets]()
    var filteredSnippetsArray = [Snippets]()
    let searchController = UISearchController(searchResultsController: nil)
    let dateFormatter = NSDateFormatter()
    //VARIABLES
    //
    //
    //VIEW DID LOAD
    override func viewDidLoad() {
        super.viewDidLoad()
//        dateFormatter.dateFormat = "MM-dd-yyyy"
        dateFormatter.dateFormat = "EEEE, MMM d, yyyy h:mma"
        searchController.searchResultsUpdater = self
        searchController.dimsBackgroundDuringPresentation = false
        definesPresentationContext = true
        tableView.tableHeaderView = searchController.searchBar
        fetchAllSnippets()
        tableView.reloadData()
    }
    override func viewWillAppear(animated: Bool) {
        fetchAllSnippets()
        tableView.reloadData()
    }
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    //VIEW DID LOAD
    //
    //
    //TABLE VIEW FUNCTIONS
    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        if searchController.active && searchController.searchBar.text != "" {
            return filteredSnippetsArray.count
        }
        return snippetsArray.count
    }
    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCellWithIdentifier("prototypecell") as! SnippetTableViewCell
        let snippetToUse: Snippets
        if searchController.active && searchController.searchBar.text != "" {
            snippetToUse = filteredSnippetsArray[indexPath.row]
        } else {
            snippetToUse = snippetsArray[indexPath.row]
        }
        cell.snippetTextLabel.text = snippetsArray[indexPath.row].snippetTitle
        cell.snippetForCell = snippetsArray[indexPath.row]
        cell.snippetDateLabel.text = dateFormatter.stringFromDate(cell.snippetForCell!.dateCreated!)
        return cell
    }
    override func tableView(tableView: UITableView, commitEditingStyle editingStyle: UITableViewCellEditingStyle, forRowAtIndexPath indexPath: NSIndexPath) {
        let celltapped = tableView.cellForRowAtIndexPath(indexPath) as! SnippetTableViewCell
        managedObjectContext.deleteObject(celltapped.snippetForCell!)
        saveNotes()
        fetchAllSnippets()
        tableView.reloadData()
    }
    override func tableView(tableView: UITableView, didSelectRowAtIndexPath indexPath: NSIndexPath) {
        performSegueWithIdentifier("editSnippetSegue", sender: indexPath)
    }
    //TABLE VIEW FUNCTIONS
    //
    //
    //
    //CORE DATA FUNCTIONS
    func fetchAllSnippets(){
        let snippetsRequest = NSFetchRequest(entityName: "Snippets")
        do {
            // get the results by executing the fetch request we made earlier
            let results = try managedObjectContext.executeFetchRequest(snippetsRequest)
            snippetsArray = results as! [Snippets]
            snippetsArray = sortTableByRecentlyEdited(snippetsArray)
        } catch {
            // print the error if it is caught (Swift automatically saves the error in "error")
            print("\(error)")
        }
    }
    func saveNotes(){
        if managedObjectContext.hasChanges {
            do {
                try managedObjectContext.save()
                print("Success")
            } catch {
                print("\(error)")
            }
        }
    }
    //CORE DATA FUNCTIONS
    //
    //
    //DATE TIME FUNCTIONS
    func sortTableByRecentlyEdited(snippets:[Snippets]) -> [Snippets]{
        var count = snippets.count-1
        var newSnippetsArray = snippets
        while(count>0){
            for i in 0...count-1{
                print("array at \(i):")
                print(newSnippetsArray[i].dateUpdated)
                print("array at \(i+1):")
                print(newSnippetsArray[i+1].dateUpdated)
                if newSnippetsArray[i].dateUpdated!.compare(newSnippetsArray[i+1].dateUpdated!) == NSComparisonResult.OrderedAscending{
                    let temp = newSnippetsArray[i]
                    newSnippetsArray[i] = newSnippetsArray[i+1]
                    newSnippetsArray[i+1] = temp
                    print("swapped values")
                }
            }
            count = count-1
        }
        return newSnippetsArray
    }
    //DATE TIME FUNCTIONS
    //
    //
    //SEGUE FUNCTIONS
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        if segue.identifier == "editSnippetSegue" {
            let navigationController = segue.destinationViewController as! UINavigationController
            let destinationController = navigationController.topViewController as! EditSnippetViewController
            destinationController.editSnippetDelegate = self
            destinationController.cancelButtonDelegate = self
            if sender is NSIndexPath {
                let celltapped = tableView.cellForRowAtIndexPath(sender as! NSIndexPath) as! SnippetTableViewCell
                destinationController.recievedSnippetTextToEdit = celltapped.snippetForCell?.snippetText
                destinationController.snippetToEdit = celltapped.snippetForCell
                destinationController.recievedSnippetTitleToEdit = celltapped.snippetForCell?.snippetTitle
            }
            else if sender is UIBarButtonItem{
               //optional logic here for the "add new snippet" button. Currently everything is handled and it works without needing any logic here.
            }
        }
    }
    //SEGUE FUNCTIONS
    //
    //
    //DELEGATE FUNCTIONS
    func editSnippetDelegate(newSnippetText:String, newSnippetTitle:String){
        let newSnippet = NSEntityDescription.insertNewObjectForEntityForName("Snippets", inManagedObjectContext: managedObjectContext) as! Snippets
        print("An Object was Added to Core Data")
        newSnippet.snippetText = newSnippetText
        newSnippet.snippetTitle = newSnippetTitle
        newSnippet.dateCreated = NSDate()
        newSnippet.dateUpdated = NSDate()
        saveNotes()
        fetchAllSnippets()
        tableView.reloadData()
    }
    func editSnippetDelegate(editedSnippetText:String, editedSnippetTitle:String, snippetToEdit:Snippets){
        snippetToEdit.snippetText = editedSnippetText
        snippetToEdit.snippetTitle = editedSnippetTitle
        snippetToEdit.dateUpdated = NSDate()
        saveNotes()
        fetchAllSnippets()
        tableView.reloadData()
    }
    func cancelButtonPressedFrom(sender: UIViewController){
        dismissViewControllerAnimated(true, completion: nil)
    }
    //DELEGATE FUNCTIONS
    //
    //
    //SEARCH BAR FUNCTIONS
    func filterContentForSearchText(searchText: String, scope: String = "All") {
        filteredSnippetsArray = snippetsArray.filter { snippet in
            return snippet.snippetTitle!.lowercaseString.containsString(searchText.lowercaseString)
        }
        
        tableView.reloadData()
    }
    //SEARCH BAR FUNCTIONS
    //
}
extension SnippetListTableViewController: UISearchResultsUpdating {
    func updateSearchResultsForSearchController(searchController: UISearchController) {
        filterContentForSearchText(searchController.searchBar.text!)
    }
}

