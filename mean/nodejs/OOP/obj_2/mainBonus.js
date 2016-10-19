'use strict'
// note the lack of private variables/methods: heres some helpful info!
// https://developer.mozilla.org/en-US/Add-ons/SDK/Guides/Contributor_s_Guide/Private_Properties

class Vehicle {
  constructor(name, wheels, passengerNumber, speed) {
    this.speed = speed;
    this.name = name || "unicycle";
    this.wheels = wheels || 1;
    this.passengerNumber = passengerNumber || 0;
    this.distanceTraveled = 0;
  }
  updateDistanceTraveled(){
    this.distanceTraveled += this.speed;
    console.log(this.distanceTraveled);
  }
  makeNoise (noise){
    var noise = noise || "Honk Honk";
    console.log(noise);
  };
  move (){
    this.makeNoise();
    this.updateDistanceTraveled();
  };
  checkMiles (){
    console.log(this.distanceTraveled);
  };
}

let vehicle = new Vehicle("Prius", 4, 4, 60); // we all know that a prius can't go this fast though...
vehicle.updateDistanceTraveled();
vehicle.move();
vehicle.checkMiles();
