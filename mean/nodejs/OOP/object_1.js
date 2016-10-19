/* Vehicle Constructor declares an initial variable, vehicle as an object.
  public properties that can be set:
    name, wheels, passengersNumber
  public method:
    makeNoise
  returns vehicle.
*/

function VehicleConstructor(name, wheels, passengerNumber){
  var vehicle = {};
/*
  Properties
*/
  vehicle.name = name || "unicycle";
  vehicle.wheels = wheels || 1;
  vehicle.passengerNumber = passengerNumber || 0;
  /*
    methods
  */
  vehicle.makeNoise = function(noise){
    var noise = noise || "Honk Honk";
    console.log(noise)
  }
  /*
  return
  */
  return vehicle;
}

var unicycle = VehicleConstructor();

var bike = VehicleConstructor("bicycle", 2, 0);
bike.makeNoise = function(){
  console.log('ring, ring');
}
// or simply: bike.makenoise("ring, ring");
var sedan = VehicleConstructor("sedan", 4, 4);
sedan.makeNoise = function(){
  console.log('Honk Honk');
}

var bus = VehicleConstructor('bus',6, 0);
bus.pickupPassengers = function(newPassengers){
  bus.passengerNumber += newPassengers;
}

console.log(bus.passengerNumber);
bus.pickupPassengers(6);
console.log(bus.passengerNumber);
