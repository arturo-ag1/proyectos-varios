// 1 - Creating a simple object and accesing it's properties.

//Creating simple function
function vehicle(name,maker,engine){
    this.name = name;
    this.maker = maker;
    this.engine = engine;
}

//Creating object
let car  = new vehicle('GT','BMW','1998cc');

//Property accessors
console.log(car.name);
console.log(car.maker);
console.log(car['engine']);


////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////

// 2 - Removing items from an array.

var array = [2,5,9];

console.log(array);

array.splice(0,1);

console.log(array);


////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
