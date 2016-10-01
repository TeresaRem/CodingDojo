//
//  ViewController.swift
//  map_test
//
//  Created by Jennifer Zeller on 9/15/16.
//  Copyright © 2016 Alex. All rights reserved.
//

import UIKit
import MapKit

class ViewController: UIViewController, MKMapViewDelegate {
    
    // set initial location
    let initialLocation = CLLocation(latitude: 37.375400, longitude: -121.910158)
    // specify radius for view
    let regionRadius: CLLocationDistance = 500
    // helper function for map center
    func centerMapOnLocation(location: CLLocation) {
        let coordinateRegion = MKCoordinateRegionMakeWithDistance(location.coordinate,regionRadius * 2.0, regionRadius * 2.0)
        mapView.setRegion(coordinateRegion, animated: true)
    }
    //
    var mapCenter = CLLocationCoordinate2DMake(37.376592, -121.909859)

    
    override func viewDidLoad() {
        
        let latitude: CLLocationDegrees = 37.375400
        let longitude: CLLocationDegrees = -121.910158
        let location: CLLocationCoordinate2D = CLLocationCoordinate2DMake(latitude, longitude)
        
        let annotation: MKPointAnnotation = MKPointAnnotation()
        
        annotation.coordinate = location
        annotation.title = "Coding Dojo"
        annotation.subtitle = "Ninja Den"
        self.mapView.addAnnotation(annotation)
        
        let circle = MKCircle(centerCoordinate: location, radius: 100)
        
        mapView.addOverlay(circle)
        

        
        // add an array of annotations
//        
//        var pinsArray: [MKPointAnnotation] = []
//        
//        for i in 0...(myFeed.count-1)
//        {
//            let pointAnnotation = MKPointAnnotation() // First create an annotation.
//            
//            pointAnnotation.title = myFeed.objectAtIndex(i).objectForKey("NOMBRE")!.stringValue
//            pointAnnotation.coordinate = CLLocationCoordinate2D(latitude: myFeed[i].objectForKey("LATITUD")!.doubleValue, longitude: myFeed[i].objectForKey("LONGITUD")!.doubleValue)
//            pointAnnotation.subtitle = ""
//            
//            pinsArray.append(pointAnnotation) // Now append this newly created annotation to array.
//        }
//        
//        mapView.addAnnotations(pinsArray)
        
        // var annotation_array: [MKPointAnnotation] = []
        // self.mapView.addAnnotations(annotation_array)
        
//        let codingDojo: MKPointAnnotation
//        let location: CLLocationCoordinate2D
        
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    
        // center map based on intial location input
        centerMapOnLocation(initialLocation)
        
        // Set map view delegate with controller
        self.mapView.delegate = self
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    @IBOutlet weak var mapView: MKMapView!
    
    func mapView(mapView: MKMapView, rendererForOverlay overlay: MKOverlay) -> MKOverlayRenderer{
        let circleView:MKCircleRenderer = MKCircleRenderer()
        circleView.strokeColor = UIColor.redColor();
        return circleView;
    }

}