//
//  editSnippetDelegate.swift
//  snippet
//
//  Created by Elliot Young on 9/28/16.
//  Copyright © 2016 Elliot Young. All rights reserved.
//

import UIKit

protocol EditSnippetDelegate:class{
    func editSnippetDelegate(newSnippetText:String, newSnippetTitle:String)
    func editSnippetDelegate(editedSnippetText:String, editedSnippetTitle:String, snippetToEdit: Snippets)
}
