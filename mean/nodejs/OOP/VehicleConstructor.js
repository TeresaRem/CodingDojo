// We are going to create our very own constructor. Create a VehicleConstructor that takes in the name, 
// number of wheels, and the number of passengers. Then complete the following tasks:
//  Each vehicle should have a makeNoise method
//  Using the constructor, create a Bike
//  Redefine the Bike’s makeNoise method to print “ring ring!”
//  Create a Sedan
//  Redefine the Sedan’s makeNoise method to print “Honk Honk!”
//  Using the constructor, create a Bus
//  Add a method to Bus that takes in the number of passengers to pick up and adds them to the passenger count​

// Have the Vehicle constructor also take in a “speed”
// Store the speed as an attribute
// Create a private variable called distance_travelled that starts at 0
// Create a private method called updateDistanceTravelled that increments distance traveled by speed
// Add a method to the Vehicle called “move” that calls updateDistanceTravelled and then makeNoise
// Add a method called checkMiles that console.logs the distance_travelled

// Now modify your code to use Prototype and the recommended way of OOP we showed in the previous chapter.
// You may have to change some private variables/methods to attributes to make all of the functionality work.
// Then make the following additions:
// Have each vehicle generate a random VIN number (study Math.random & Math.floor). Don’t worry about potential duplicates for now.


function VehicleConstructor(name, wheels, passengers, speed) {
  var self = this;
  self.distance_travelled = 0;
  this.name = name || 'vehicle';
  this.wheels = wheels || 1;
  this.passengers = passengers || 0;
  this.speed = speed || 5;
  this.vin = "${Math.floor(Math.random()*10)}${Math.floor(Math.random()*10)}${Math.floor(Math.random()*10)}${Math.floor(Math.random()*10)}${Math.floor(Math.random()*10)}${Math.floor(Math.random()*10)}${Math.floor(Math.random()*10)}${Math.floor(Math.random()*10)}${Math.floor(Math.random()*10)}${Math.floor(Math.random()*10)}${Math.floor(Math.random()*10)}${Math.floor(Math.random()*10)}${Math.floor(Math.random()*10)}${Math.floor(Math.random()*10)}${Math.floor(Math.random()*10)}${Math.floor(Math.random()*10)}"

}

VehicleConstructor.prototype.updateDistanceTravelled = function(){
    this.distance_travelled += this.speed
  }
VehicleConstructor.prototype.move = function(){
    this.updateDistanceTravelled()
    this.makeNoise()
    return this
  }
VehicleConstructor.prototype.checkMiles = function(){
    console.log(this.distance_travelled)
  }
VehicleConstructor.prototype.makeNoise = function(){};

var Bike = new VehicleConstructor('Bike',2,0,10);

Bike.makeNoise = function(){
  console.log("ring ring!");
}

var Sedan = new VehicleConstructor('Sedan',4,0,65)
Sedan.makeNoise = function(){
  console.log("honk honk!");
}

var Bus = new VehicleConstructor('Bus',4,0,55)
Bus.pickUp = function(newpassengers){
  this.passengers += newpassengers;
  console.log(this.passengers)
}
Bus.move().move().move().checkMiles()
