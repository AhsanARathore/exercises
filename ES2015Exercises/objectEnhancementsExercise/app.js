// Same keys and values
// function createInstructor(firstName, lastName){
//     return {
//       firstName: firstName,
//       lastName: lastName
//     }
//   }
//   /* Write an ES2015 Version */

const createInstructor = (firstname, lastname) => {
    return {
        firstname,
        lastname,
    }
}

// Computed Property Names
// var favoriteNumber = 42;

// var instructor = {
//   firstName: "Colt"
// }

// instructor[favoriteNumber] = "That is my favorite!"
// /* Write an ES2015 Version */

let favoriteNumber = 42;
const instructor = {
    firstName : "Colt",
    [favoriteNumber] : "thats my favorite number!"
}

// Object Methods
// var instructor = {
//   firstName: "Colt",
//   sayHi: function(){
//     return "Hi!";
//   },
//   sayBye: function(){
//     return this.firstName + " says bye!";
//   }
// }

// /* Write an ES2015 Version */

const instructors = {
    firstName : "Colt",
    sayHi() {return "hi"},
    sayBye() {return this.firstName + "bye"}
}

// createAnimal function
// Write a function which generates an animal object. The function should accepts 3 arguments:

// species: the species of animal (‘cat’, ‘dog’)
// verb: a string used to name a function (‘bark’, ‘bleet’)
// noise: a string to be printed when above function is called (‘woof’, ‘baaa’)
// Use one or more of the object enhancements we’ve covered.

function createAnimal(species, verb, noise) {
    return {
        species,
        [verb]() { 
            return  noise;
        }
    }
}

