// Quick Question #1


// What does the following code return?

// new Set([1,1,2,2,3,4])

//          answer: [1,2,3,4]

// Quick Question #2

// What does the following code return?

// [...new Set("referee")].join("")

//      Answer:  "ref"

// Quick Questions #3
// What does the Map m look like after running the following code?

// let m = new Map();
// m.set([1,2,3], true);
// m.set([1,2,3], false);

//       Answer:  0: {Array(3) => true}
 //               1: {Array(3) => false}

// hasDuplicate
// Write a function called hasDuplicate which accepts an array and returns true or false if that array contains a duplicate

function hasDuplicate(arr) {
    new set(arr).size !== arr.length
}

// vowelCount
// Write a function called vowelCount which accepts a string and returns a map where the keys are numbers and the values are the count of the vowels in the string.

function vowels(char) {
    return "aeiou".includes(char);
}

function vowelCount (str) {
    const vowelMap = new Map();
    for (let char of str) {
        if (vowels(char)){
            if (vowelMap.has(char)){
                vowelMap.set(char, ++1)
                
            }
            else {
                vowelMap.set(char, 1)
            }
        }
    }
}