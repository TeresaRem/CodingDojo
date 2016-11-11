//
//  ViewController.swift
//  travel
//
//  Created by Jennifer Zeller on 9/21/16.
//  Copyright © 2016 Alex. All rights reserved.
//

import UIKit

class ViewController: UIViewController, UIImagePickerControllerDelegate, UINavigationControllerDelegate {

    @IBOutlet weak var currentImage: UIImageView!
    
    let imagePicker: UIImagePickerController! = UIImagePickerController()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        imagePicker.delegate = self
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    @IBAction func takePicture(_ sender: UIButton){
        if (UIImagePickerController.isSourceTypeAvailable(.camera)){
            if UIImagePickerController.availableCaptureModes(for: .rear) != nil{
                imagePicker.allowsEditing = false
                imagePicker.sourceType = .camera
                imagePicker.cameraCaptureMode = .photo
                present(imagePicker, animated: true, completion: {})
            } else{
                print("no")
            }
            
        } else{
            print("Camera inaccessable")
        }
    }
    
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [String : Any]) {
        print("Got an image")
        if let pickedImage:UIImage = (info[UIImagePickerControllerOriginalImage]) as? UIImage{
            let selectorToCall = #selector(ViewController.imageWasSavedSuccessfully(_:didFinishSavingWithError:context:))
            UIImageWriteToSavedPhotosAlbum(pickedImage, self, selectorToCall, nil)
        }
        imagePicker.dismiss(animated: true, completion: {})
    }
    
    func imagePickerControllerDidCancel(_ picker: UIImagePickerController) {
        print("user cancelled image")
        dismiss(animated: true, completion: {})
    }
    
    func imageWasSavedSuccessfully(_ image: UIImage, didFinishSavingWithError error: NSError!, context: UnsafeMutableRawPointer){
        print("image saved")
        if let theError = error{
            print("error happened for image = \(theError)")
        } else{
            DispatchQueue.main.async(execute: {() -> Void in self.currentImage.image = image})
        }
    }


}

