var person = {
  name: 'Alex',
  distance_traveled: 0,
  say_name: function(){console.log(person.name);return person},
  say_something: function(phrase){console.log(person.name,phrase);return person},
  walk: function(){
    console.log(person.name,"is walking")
    person.distance_traveled=person.distance_traveled+3
    return person},
  run: function(){
    console.log(person.name,"is running")
    person.distance_traveled=person.distance_traveled+10
    return person},
  crawl: function(){
    console.log(person.name,"is crawling")
    person.distance_traveled=person.distance_traveled+1
    return person}
}

person.run().crawl().walk().say_something("wants ice cream").say_name()
console.log(person.distance_traveled)