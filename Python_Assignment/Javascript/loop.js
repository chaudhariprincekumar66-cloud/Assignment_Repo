// JavaScript Assignment: for Loop// **********************************************************************************************
Question:1 
// A teacher wants students to practice counting. Write a program to print all numbers from 1 to 15.
Answer:1 
// for (i = 1; i<=15; i++){
//     console.log(i)
// }


Question:2 
// A school has lockers numbered with even numbers for a special activity. Write a program to print all even numbers from 2 to 40.
Answer:2 
// for (i = 2; i<=40; i = i + 2){
//     console.log(i)
// }


Question:3 
// A fitness coach assigns odd numbers to participants for a special activity. Write a program to print all odd numbers from 1 to 35.
Answer:3 
// for (i = 1;i<=35 ; i = i + 2){
//     console.log(i)
// }

Question:4 
// You save ₹10 on Day 1, ₹20 on Day 2, ₹30 on Day 3, and continue increasing your daily savings by ₹10. Write a program to calculate your total savings after 10 days.
Answer:4 
// let p = 0
// for (i = 1; i <=10; i++){
//     p = p + 10

// }
// console.log("Total saving after 10 days:",p)


Question:5 
// You want to practice multiplication. Write a program to print the multiplication table of 12, from 12 × 1 to 12 × 10.
Answer:5 
// for (i = 1; i <= 10; i++){
//     console.log("12 X",i, "=",12*i)
// }

Question:6 
// You drink 3 glasses of water every day. Write a program to calculate the total number of glasses you drink over 7 days. Print the cumulative total after each day
Answer:6 
// let p = 0
// for (i =1 ; i<=7; i++){
//     p = p + 3 
//     console.log("Day",i,":",p,"glasses")
// }

Question:7 

// Q8. Sum of Even Numbers ➕

// You want to calculate the sum of all even numbers between 2 and 30, including both 2 and 30. Write a program to calculate and print the total.

// Sample Output:


Answer:7
// let p = 0
// for (i= 0;i<=30;i= i+2){
//     p = p+ i


// }
// console.log("Sum of even numbers = ",p)


Question:8 
// Q10. Movie Tickets 🎬

// One movie ticket costs ₹150. Write a program to print the total ticket cost for 1 to 8 people.

// Sample Output:

// 1 person: ₹150
// 2 people: ₹300
// 3 people: ₹450
// 4 people: ₹600
// 5 people: ₹750
// 6 people: ₹900
// 7 people: ₹1050
// 8 people: ₹1200

Answer:8 
// let p = 0
// for (i = 1; i<=8; i++){
//     p = p + 150
//     console.log(i,"people:",p)

// }



// Part B] For Loop (Additional advanced questions)******************************************

Question:1 
// Given an array of temperatures [28, 32, 25, 40, 18, 35], use a for loop to count how many days were hotter than 30°C.
Answer:1 
// let arr = [28, 32, 25, 40, 18, 35]
// let i = 0;
// let q = 0;
// for (i=0;i<6;i++){
//     if (arr[i]>30){
//         q =q +1

//     }

// }
// console.log(q)

Question:2 
// Write a for loop that calculates the sum of all digits of a given number (example: 4729 → 4+7+2+9 = 22).
Answer:2 
// let N = "4729"
// let q= 0
// let i = 0

// for (i=0;i<N.length;i++){
//     p = N[i]
//     q = q + Number(p);
// }
// console.log(q)


//Other mathod ************************************************************* 
// let N = "4729"
// let p = 0;
// for (i=1; i<=N.length; i++){
//     q = Number(N)%10
//     N = Math.floor(Number(N)/10) 
//     p = p + q

// }
// console.log(p)




Question:3 
//Create a for loop that prints only the numbers between 1 and 100 that are divisible by both 3 and 5, but not by 7.
Answer:3 
// for (i = 0; i<=100; i++){
//     if (i%3==0 && i%5==0 && i%7 !=0){
//         console.log(i)
//     }
// }

Question:4 
// Given the string "JavaScript", use a for loop to create a new string that contains only the consonants (remove vowels).
Answer:4 
// let string = "JavaScript"
// let q = "";
// let arr =["a", "e","i","o","u","A","E","I","O","U"]
// for (i = 0; i<string.length; i++){
//     if (arr.includes(string[i])){
//         q = q + string[i]

//     }
    
// }
// console.log(q)


Question:5 
// Write a for loop that finds the largest number in an array of positive integers without using any sorting method.
Answer:5 
// let arr = [1, 2, 3, 4, 8, 5];
// let max = arr[3];
// for (let i = 0; i < arr.length; i++) {
//     if (arr[i] > max) {
//         max = arr[i];
//     }
// }

// console.log(max);


Question:6 
// Use a for loop to check whether a given number is a perfect number (a number equal to the sum of its proper divisors). Example: 28.
Answer:6 
// let number = 28;
// let p = 0

// for (i = 1;i<number; i++){
//     if (number%i===0){
//         p = p + i

//     }

// }
// if(p == number){
//     console.log("Number is perfect")
// }else{
//     console.log("Number is not perfect")
// }











Question:7 
// Print the following series using a single for loop:
// 1 2 4 8 16 32 64 128
// p = 1
// for (i = 1; i<=8; i++){
//     console.log(p)
//     p = 2*p

// }


Question:8 
// Write a for loop that prints the first 20 Fibonacci numbers (starting with 0 and 1).
Answer:8
// let p = 0;
// let q = 1;
// for (i=1; i<=20; i++){
//     console.log(p)
    // [p, q] = [q, p + q];


// }


//other method **************************************************

// let p = 0;
// let q  = 1;
// let fib_series = " 0 1 ";
// for (i=1; i<=18; i++){
//     let c = p + q;
//     fib_series += c+" ";
//     p = q 
//     q = c


// }
// console.log(fib_series)


Question:9 
// Write a for loop that converts a decimal number to its binary representation (without using built-in methods like toString(2)).
Answer:9 
// let number = 96;
// str = " "
// for(i=1;number!=0;i++){
//     p = number%2
//     number = Math.floor(number/2)
//     str = String(p) + str


// }
// console.log(str)


// Part C-a] break inside a for Loop// ************************************************************** 

Question:1 
// Write a for loop that searches for the first occurrence of the number 7 in an array. As soon as it finds 7, print its index and stop the loop using break.
Answer:1 
// let arr = [59, 67, 28, 35 , 856,7, 56, 13]
// for (i=1; i<=arr.length ; i++){
//     if (arr[i] == 7){
//         console.log(7)
//         break
//     }

// }



















































