// Conditional Statements //***************************************** */

// A] if Statement

Question:1
// Write a program to check if a number is divisible by 5. If yes, print “Divisible by 5”.
Answer:1
// let number = 10;
// if (number%5===0){
//     console.log("Divisible by 5")
// }



Question:2
// Check if a person’s age is greater than or equal to 60. If true, print “Senior Citizen”.
Answer:2
// let age = 65;
// if (age>=60){
//     console.log("Senior Citizen")
// }



Question:3
// Write a program that checks if a given number is greater than 100. If yes, print “Big Number”.
Answer:3
// let number = 70;
// if (number>100){
//     console.log("Big number")
// }

Question:4
// Check if the temperature is less than 10. If true, print “Very Cold”.
Answer:4
// let temperature = 5;
// if (temperature<10){
//     console.log("Very Cold")
// }


Question:5
// Write a program to check if a student scored full marks (100). If yes, print “Perfect Score”.
Answer:5
// let score = 70;
// if (score ===100){
//     console.log("Perfect Score")
// }


Question:6
// Check if a number is negative. If it is, print “Negative Number”.
Answer:6
// let Number = -7;
// if (Number<0){
//     console.log("Negative Number")
// }

Question:7
// Write a program that checks if a user has entered an empty string. If the string is empty, print “No input provided”.
Answer:7
// let string = "";
// if (string=== ""){
//     console.log("No input provided")
// }



Question:8
// Check if a given year is divisible by 100. If yes, print “Century Year”.
Answer:8
// let year = 2000;
// if (year%100===0){
//     console.log("Century Year")
// }

Question:9
// Write a program to check if a number is both positive and even using a single if condition. If true, print “Positive Even Number”.
Answer:9
// let number = -6;
// if (number%2===0 && number>0){
//     console.log("Positive Even Number")
// }



Question:10
// Check if the value of a variable marks is greater than or equal to 35 and less than or equal to 100. If true, print “Valid Marks”.
Answer:10
// let marks = 20;
// if (35<=marks && marks<=100){
//     console.log("Valid Marks")
// }
    




// B] if...else Statement

Question:1
// Write a program to check whether a number is even or odd.
// let number = 8;
// if (number%2 ===0){
//     console.log("Even")
// }else{
//     console.log("odd")
// }

Question:2
// Check if a person is eligible to vote (age ≥ 18). Print “Eligible” or “Not Eligible”.
Answer:2
// if (age>=18){
//     console.log("Eligible")
// }else{
//     console.log("Not Eligible")
// }


Question:3
// Write a program that checks whether a number is positive or negative.
Answer:3
// let number = 6;
// if (number>0){
//     console.log("Positive number")
// }else{
//     console.log("Negative number")
// }



Question:4
// Check if a student has passed or failed based on marks (pass mark = 35).
Answer:4
// let marks = 33;
// if (marks>=35){
//     console.log("Pass Marks")
// }else{
//     console.log("Failed")
// }



Question:5
// Write a program to check whether a given character is an uppercase letter or not.
// (Hint: Use character comparison)
Answer:5
// let ch = "b";
// if (ch>="A" && ch <="Z"){
//     console.log("Uppercase Letter")
// }else{
//     console.log("Not a uppercase letter")
// }



Question:6
// Check if a number is divisible by 3 or not. Print appropriate messages.
Answer:6
// let number = 8;
// if (number%3===0){
//     console.log("Divisible by 3")
// }else{
//     console.log("Not Divisible by 3")
// }



Question:7
// Write a program that takes a password as input. If the password is “admin123”, print “Login Successful”, otherwise print “Incorrect Password”.
Answer:7
// let password = "admin123";
// if (password=="admin123"){
//     console.log("Login Successful")
// }else{
//     console.log("Incorrect Password")
// }



Question:8
// Check whether a given year is a leap year or not using the basic rule (divisible by 4).
Answer:8
// let year = 2026;
// if (year%4 ==0){
//     console.log("Leap year")
// }else{
//     console.log("Not a leap year")
// }

Question:9
// Check if a number is positive, negative, or zero using only if...else (you may use nested or multiple conditions carefully).
Answer:9
// let number = -0;
// if (number>0){
//     console.log("positive number")
// }else if (number==0){
//     console.log("Zero")
// }else if (number<0){
//     console.log("Negative number")
// }


// if...else if...else // *******************


Question:1 
// Write a program that takes a month number (1–12) and prints the corresponding season:
// Winter (12, 1, 2), Summer (3, 4, 5), Monsoon (6, 7, 8), Autumn (9, 10, 11). 
// let month = 7;
// if (3<=month && month<=5){
//     console.log("Summer")
// }else if (6<=month && month<=8){
//     console.log("Monsoon")
// }else if (9<=month && month<=11){
//     console.log("Autumn")
// }else{
//     console.log("Winter")
// }


Question:2 
// Create a simple tax calculator based on income:
// Income < 3,00,000 → No tax
// 3,00,000 – 7,00,000 → 5% tax
// 7,00,000 – 10,00,000 → 10% tax
// Above 10,00,000 → 15% tax
// Print the tax amount.

Answer:2 
// let income = 800000;
// if (income<300000){
//     console.log("No tax")
// }else if(300000<=income && income<700000){
//     console.log("5% tax")
// }else if(700000<=income && income<1000000){
//     console.log("10% tax")
// }else {
//     console.log("15% tax")
// }




Question:3 
// Write a program that checks a student’s score and prints:
// “Outstanding” (90 and above), “Good” (70–89), “Average” (40–69), “Needs Improvement” (below 40).

Answer:3 
// let marks = 90;
// if (marks>=90){
//     console.log("Outstanding")
// }else if(89>=marks && marks>= 70){
//     console.log("Good")
// }else if(69>=marks && marks>=40){
//     console.log("Average")
// }else{
//     console.log("Need Improvement")
// }



Question:4 
// Check the speed of a vehicle and print:
// “Slow” (below 40), “Normal” (40–80), “Fast” (above 80).
Answer:4 
// let speed = 80;
// if (speed<40){
//     console.log("Slow")
// }else if (40<=speed && speed<80){
//     console.log("Normal")
// }else {
//     console.log("Fast")
// }



Question:5 
// Check the day number (1–7) and print whether it is a Weekday or Weekend
// (1 to 5 = Weekday, 6 and 7 = Weekend).
Answer:5 
// let number = 5;
// if (1<= number && number<=5){
//     console.log("weekday")
// }else{
//     console.log("Weekend")
// }


Question:7 
// Check a number and print one of the following:
// “Positive Even”, “Positive Odd”, “Negative Even”, “Negative Odd”, or “Zero”.
Answer:7 
// let number = 5;
// if (number>=0){
//     if (number%2 == 0){
//         console.log("Even Positive")
//     }else{
//         console.log("odd positive")
//     }
// }else if (number<0){
//     if (number%2 == 0){
//         console.log("Even negative")
//     }else{
//         console.log(" odd negative")
//     }
// }



// D] Nested if Statement //  ***************************************


Question:1 
// Check if a number is greater than 10.
// If yes, then check whether it is divisible by 3 and print the appropriate message.
Answer:1 
// let number = 15;
// if (number>10){
//     if (number%3==0){
//         console.log("number is greater than 10 and divisible by ")
//     }
// }


Question:2 
// Write a program that first checks if a person is 18 or older.
// If yes, then check if they have a voter ID. Print “Can Vote” only if both conditions are true.
Answer:2 
// let age = 19;
// let voterId ="yes";
// if (age>18){
//     if (voterId ==="yes"){
//         console.log("can vote")
//     }
// }


Question:3 
// Check if a student has scored 40 or more marks.
// If yes, then check if the score is 80 or above and print “Passed with Distinction”.
Answer:3 
// let score = 45;
// if (score >=40){
//     if (score>=80){
//         console.log("Passed with Distinction")
//     }
// }

Question:4 
// Create a simple ATM system:
// First check if the PIN is correct.
// If PIN is correct, then check if the account balance is sufficient for withdrawal.

Answer:4 
// let pin = 123456
// let balance = 200000;
// let withdrawal = 100000;
// if (pin == "123456"){
//     if (balance>=withdrawal){
//         console.log("withdrawal successful")
//     }
// }


Question:5 
// Write a program that checks if a year is divisible by 4.
// If yes, then further check if it is divisible by 100.
// If it is divisible by 100, then check if it is also divisible by 400 to confirm it is a leap year.
Answer:5 
// let year = 2026;
// if (year%4 ==0){
//     if (year%100 == 0){
//         if (year%400==0){
//             console.log("confirm it is a leap year")
//         }
//     }
// }


Question:6 
// let Email = "princejk@.com";
// if (Email.includes("@")){
//     if(Email.endsWith(".com")){
//         if(Email.length>10){
//             console.log("Valid Email")
//         }
//     }
        
// }



Question:7 
// Write a program for online shopping:
// First check if the cart total is ₹1000 or more.
// If yes, then check if the user is a premium member.
// If the user is premium, give 20% discount, otherwise give 10% discount.
// Finally print the final amount after discount.

Answer:7 
// let cart = 2000;
// let userType = "premium";
// if (cart>1000){
//     if (userType =="premium"){
//         console.log("Final amount =", cart -(cart*20)/100)

//     }else{
//         console.log("Final amount = ", cart - (cart*10)/100)

//     }
// }




// switch statement // **************************************************************
Question:1
// Write a program that takes a month number (1–12) and prints the number of days in that month using switch
// (Hint: Consider 28/29 for February as 28 for simplicity).
Answer:1 
// let month = 1;
// switch (month){
//     case 1:
//         console.log("31")
//         break
//     case 2:
//         console.log("28")
//         break
//     case 3:
//         console.log("31")
//         break
//     case 4:
//         console.log("30")
//         break
//     case 5:
//         console.log("31")
//         break
//     case 6:
//         console.log("30")
//         break
//     case 7:
//         console.log("31")
//         break
//     case 8:
//         console.log("30")
//         break
//     case 9:
//         console.log("31")
//         break
//     case 10:
//         console.log("30")
//         break
//     case 11:
//         console.log("31")
//         break
//     case 12:
//         console.log("30")
//         break
    
// }

Question:2
// Write a program that checks a character and prints whether it is a vowel or consonant using switch.
Answer:2 
// let letter =  "o";
// switch(letter){
//     case "a":
//         console.log("vowel")
//         break
//     case "e":
//         console.log("vowel")
//         break
//     case "i":
//         console.log("vowel")
//         break
//     case "o":
//         console.log("vowel")
//         break
//     case "u":
//         console.log("vowel")
//         break
//     case "A":
//         console.log("vowel")
//         break
//     case "E":
//         console.log("vowel")
//         break
//     case "I":
//         console.log("vowel")
//         break
//     case "O":
//         console.log("vowel")
//         break
//     case "U":
//         console.log("vowel")
//         break
//     default:
//         console.log("consonent")

// }


Question:3 
// Create a program that takes a number from 1 to 4 and prints the season using multiple cases together:
// 1 or 2 → Winter
// 3 or 4 → Summer

Answer:3
// let number = 3;
// switch (number){
//     case 1:
//         console.log("Winter")
//         break
//     case 2:
//         console.log("Winter")
//         break 
//     case 3:
//         console.log("summer")
//         break
//     case 4:
//         console.log("Summer")
//         break
// }



Question:4 
// Write a program using switch (true) to assign class based on marks:
// ≥ 75 → Distinction
// ≥ 60 → 1st class
// ≥ 50 → 2nd class
// ≥ 35 → 3rd class
// below 35 → Failed

Answer:4 
// let marks = 80;
// switch(true){
//     case marks>=75:
//         console.log("Distinction")
//         break
//     case 75>marks && marks>=60:
//         console.log("1st class")
//         break 
//     case 60>marks && marks >= 50:
//         console.log("2nd class")
//         break
//     case 50>marks && marks>=35:
//         console.log("3rd class")
//         break
//     default:
//         console.log("Failed")
//         break
//     }



Question:5
// Create a nested switch program:
// First take a role (“admin” or “user”).
// If role is “admin”, then take an action (“create”, “edit”, “delete”) and print the corresponding message.
// If role is “user”, print “Limited Access”.
Answer:5
// let role = "user";
// let action = "create";

// switch(role){
//     case "admin":
//         switch(action){
//             case "create":
//                 console.log("you are creator.")
//                 break
//             case "edit":
//                 console.log("you are editor.")
//                 break
            
//             case "delete":
//                 console.log("you are deleter.")


//         }
//         break
//     case "user":
//         console.log("Limited Access")
        
// }



Question:6 
// Predict and explain the output of the following code. Then correct it so that only one message is printed:
// let fruit = "mango";

// switch (fruit) {
//   case "apple":
//     console.log("Apple is red");
//   case "mango":
//     console.log("Mango is yellow");
//   case "banana":
//     console.log("Banana is yellow");
//   default:
//     console.log("Unknown fruit");
// }
Answer:6 
// let fruit = "mango";

// switch (fruit) {
//   case "apple":
//     console.log("Apple is red");
//     break
//   case "mango":
//     console.log("Mango is yellow");
//     break
//   case "banana":
//     console.log("Banana is yellow");
//     break
//   default:
//     console.log("Unknown fruit");
//     break
// }


// Question:7
// let value = "0";

// switch (true) {
//     case value === 0:
//         console.log("value is zero");
//         break;
//     case value === undefined:
//         console.log("value is undefined");
//         break;
//     case value === null:
//         console.log("null");
//         break;
//     case value === "0":
//         console.log("value is string '0'");
//         break;
//     default:
//         console.log("No match found");
//         break;
// }
// JavaScript mein switch statement values ko compare karne ke liye strict equality (===) ka use karta hai. Iski wajah se kuch values mein yeh issues aate hain:

// console.log(Boolean())




























