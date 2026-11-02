// Section 2: Function Declaration
Question:1
// Create a function declaration named displayCourse that returns "JavaScript Fundamentals". Call it and print the result.
Answer:1 
// function displayCourse(){
//     return "JavaScript Fundamentals";
// }
// console.log(displayCourse())


Question:2 
// Write a function declaration getStudentStatus that returns the string "Active Learner". Store the returned value in a variable and print it.

// function getStudentStatus(){
//     return "Active Learner";
// }
// let value = getStudentStatus()
// console.log(value)



Question:3 
// Write a function declaration and call it before its definition. What happens and why? Explain briefly.
Answer:3 
// function greet(){

// }
// console.log(greet())

// give answer "undefined"



//Function Expression
Question:1 
// Create a function expression named showMotto that returns "Code. Learn. Grow.". Call it and print the output.
// const showMotto = function(){
//     return "code. Learn. Grow."
// }
// console.log(showMotto())


Question:2 
// Write a function expression getSemester that returns the number 3. Print the value returned by the function.
Answer:2 
// const getSemester = function(){
//     return 3;

// }
// console.log(getSemester())


Question:3 
// Create a function expression and try to call it before writing the expression. What error do you get and why?
Answer:3 
// console.log(getSemester())
// const getSemester = function(){
//     return 3;
// }

// ReferenceError: Cannot access 'getSemester' before initialization
// it error occurs because function expression is not hoisted. 


// Function Calling (Invocation)

Question:1 
// Write a function declaration greetStudent that returns "All the best for your coding journey!". Call this function four times.
// function greetStudent(){
//     return "All the best for your coding journey"
// }
// console.log(greetStudent())
// console.log(greetStudent())
// console.log(greetStudent())
// console.log(greetStudent())


Question:2 
// Create a function expression todayFocus that returns "Focus on functions today". Store the result in a variable and print that variable
Answer:2 
// function todayFocus(){
//     return "Focus on function today"
// }
// let value = todayFocus()
// console.log(value)


// Parameters vs Arguments ///******************* */
Question:1 
// Write a function declaration subtract(a, b) that returns the difference of two numbers. Call it with arguments 50 and 18 and print the result.
Answer:1 
// function subtract(a,b){
//     return a-b
// }
// console.log(subtract(50 , 18))


Question:2
// Create a function expression greetUser(name) that returns "Welcome, " + name + "!". Call it with the argument "Aarav".
Answer:2  
// const greetUser = function(name){
//     return "Welcome, "+ name + "!"
// }
// console.log(greetUser("Aarav"))

Question:3 
// Write a function calculateArea(length, breadth) that returns the area of a rectangle. Call it twice with different pairs of arguments: (12, 5) and (8, 9).
// function area(length,breadth){
//     return length*breadth

// }
// console.log(area(12 , 5))


Question:4 
// What is the difference between a parameter and an argument? Explain with a short example.
Answer:4 
// parameter = Variables defined inside the function definition.
// function add(a, b) {

// Arguments = Actual values passed while calling the function.
// add(10, 20);


Question:5 
// Can a function have parameters but be called without arguments? What happens in that case? Explain briefly.
Answer:5 

// function area(length,breadth){
//     return length*breadth

// }
// console.log(area())

// it show NaN
// When this happens, JavaScript does not throw an error; instead, any parameters that do not receive a corresponding argument are automatically assigned the value NaN.


// Return Statement
Question:1 
// Write a function squareOfNumber(n) that returns the square of the given number. Call it with 9 and print the returned value.

Answer:1 
// function squareOfNumber(n){
//     return n**2
// }
// console.log(squareOfNumber(9))


Question:2 
// Create a function isAdult(age) that returns true if age is 18 or above, otherwise returns false. Test it with 17 and 20.
Answer:2 
// function isAdult(age){
//     if (age>=18){
//         return true
//     }
//     else{
//         return false
//     }
    
// }
// console.log(isAdult(28))


Question:3 
// Write a function getFullName(firstName, lastName) that returns the full name. Call it with "Rohit" and "Sharma" and print the result.
Answer:3 
function getFullName(firstName , lastName){
    return firstName+ " "+lastName
}
console.log(getFullName(Rohit))


























































