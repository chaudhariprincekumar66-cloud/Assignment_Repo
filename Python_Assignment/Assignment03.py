Question:1
#Predict the output before running the code.

a = 15
b = 20

#print(a < b)
#print(a > b)
#print(a == b)
#print(a != b)
#print(a <= b)
#print(a >= b)
Answer:1
#True
#False
#False
#True
#True
#False
Question:2
#Predict the output:

#x = 10
#y = 10

#print(x == y)
#rint(x != y)
#print(x < y)
#print(x <= y)
#print(x >= y)
#Pay special attention to the difference between == and =.
Answer:2
#True
#False
#False
#True
#True
Question:3
#Predict the output:

#a = 10
#b = 5

#print(a + b == 15)
#print(a * b > 40)
#print(a - b != 5)
#print(a // b == 2)
#True
#True
#False
#True
Question:4
#Predict the output:

#print("Python" == "Python")
#print("Python" == "python")
#print("Hello" != "hello")
#What does this tell you about string comparison and case sensitivity?
Answer:4
#True
#False
#True
Question:5
#Predict the final value of x:

x = 20

x += 10
x -= 5
x *= 2
x //= 5

#print(x)
#Write the value of x after each statement.
Answer:5
10
Question:6
#Start with:

#marks = 50
#Use assignment operators to:

#Increase marks by 10
#Decrease marks by 5
#Multiply marks by 2
#Print the final value.
Answer:6
#marks=50
#marks+=10
#marks-=5
#marks*=2
#print(marks)
Question:7
#Predict the output:

#text = "Python Programming"

#print("Python" in text)
#print("Java" in text)
#print("Python" not in text)
#True
#False
#False
Question:8
#Given:

#word = "computer"
#Write expressions to check:

#Whether "p" is present.
#Whether "x" is present.
#Whether "c" is not present.
Answer:8
#word="computer"
#print("p" in word)
#print("x" in word)
#print("c" not in word)
#True
#False
#False
Question:9
#Predict the output:

text = "Python"

#print("P" in text)
#print("p" in text)
#print("Python" in text)
#print("python" in text)
#Explain why some results are different.
#True
#False
#True
#False
Question:10
Email="student@yahoo.com"
print("@" in  Email)
Question:11
#Use ord() to find the Unicode code point of:

#A
#a
#Z
#z
#0
#9
#@
Answer:11
#print(ord("A"))
#print(ord("a"))
#print(ord("Z"))
#print(ord("z"))
#print(ord("0"))
#print(ord("9"))
#print(ord("@"))
65
97
90
122
48
57
64
Question:12
#Use chr() to find the character represented by:

#65
#66
#97
#98
#48
#57
#64
Answer:12
#print(chr(65))
#print(chr(66))
#print(chr(97))
#print(chr(98))
#print(chr(48))
#print(chr(57))
#rint(chr(64))
Answer:12
#A
#a
#b
#0
#9
#@
Question:13
#unicod_of_Y=ord("Y")
#print(chr(unicod_of_Y+1))
Answer:13
#"z"
Question:14
#Predict the output:

#print("A" < "B")
#print("a" < "b")
#print("A" < "a")
#print("0" < "9")
#Then use ord() to understand why the results occur.
Answer:14
#True
#True
#True
#True
Question:15
#Use chr() to display the characters represented by:

9731
9829
8377
#Then use ord() on those characters to verify the values.
Answer:15
#print(chr(9731))
#print(chr(9829))
#print(chr(8377))
#☃
#♥
#₹
Question:16
#Given:

#text = "PYTHON"
#Print:

#First character
#Second character
#Last character
#Second-last character
Answer:16
#text="PYTHON"
#print(text[:1])
#print(text[1:2])
#print(text[-1:])
#print(text[4:5])
#P
#Y
#N
#O
Question:17
#Given:

text = "COMPUTER"
#Find the characters at:

0
3
-1
-3
#Write the Python expressions.
Answer:17
#print(text[:1])
#print(text[3:4])
#print(text[-1:])
#print(text[-3:-4:-1])
#C
#P
#R
#T
Question:18
text = "PYTHON"

#print(text[0])
#print(text[2])
#print(text[-1])
#print(text[-2])
Answer:18
#P
#T
#N
#O
Question:19
#Given:

word = "PROGRAM"
#Without running the code, determine:

word[0]
word[2]
word[-1]
word[-4]
Answer:19
"P"
"O"
"M"
"G"
Question:20
#Given:

text = "PYTHON"
#Predict:

#print(text[2:5])
#print(text[1:6])
Answer:20
#PYT
#THO
#YTHON
Question:21
#Given:

text = "PROGRAMMING"
#Predict:

#print(text[:4])
#print(text[4:])
#print(text[:])
Answer:21
#PROG
#RAMMING
#PROGRAMMING
Question:22
#Given:

text = "PYTHON"
#Predict:

#print(text[::2])
#print(text[1::2])
#print(text[::-1])
Answer:22
#PTO
#YHN
#NOHTYP
Question:23
#Take a string as input and reverse it using slicing.
Answer:23
#text="PYTHON"
#print(text[:-1:-1])
#NOHTYP
Question:24
#Take a string as input and print every second character starting from index 0.
Answer:24
#number="12345678"
#print(number[0:9:2])
Question:25
#Take a string as input and print:

#First three characters
#Last three characters
Answer:25
#text="Programing"
#print("first three letters:",text[:3])
#print("Last three letters:",text[-3:])
#first three letters: Pro
#Last three letters: ing
Question:26
#Given:

text = "ABCDEFGHIJ"
#Predict the output:

#print(text[2:8:2])
#print(text[8:2:-2])
#print(text[::-2])
#For each expression, identify:
Answer:26

text_1="start"
text_2="stop"
text_3="step"
#print(text_1[2:8:2])
#print(text_2[8:2:-2])
#print(text_3[::-2])
#at
#p
#pt
Question:27
#Take the string:

text = "BTECH-CSE-2026"
#Use slicing to extract:

#BTECH
#CSE
#2026
#Do not manually write the extracted strings.
Answer:27
#print(text[:5])
#print(text[6:9])
#print(text[10:])
#BTECH
#CSE
#2026
Question:28
#Predict the output:

#text = "Python is easy"

#print(text.split())
#Explain what separates the words.
Answer:28
#['Python', 'is', 'easy']
Question:29
#Predict the output:

#data = "apple,banana,mango"

#print(data.split(","))
Answer:28
#['apple', 'banana', 'mango']
Question:30
#Predict the output:

#text = "Python is easy"

# print(text.split(","))
#Why does it not split at the spaces?
Answer:30
#['Python is easy']
Question:31
#Take:

#Rahul Kumar Sharma
#as input.

#Use .split() and print each word on a separate line.
Answer:31
#text="Rahul , kumar , sharma"
#print(text.split(","))
Question:32
#Take two values from the user in one line.

#Example:

#Input:
#Rahul Kumar
#Store them in:

#first_name
#last_name
#Then display:

#First Name: Rahul
#Last Name: Kumar
Answer:32
#Data= input("Enter your  name:").split( )
#first_name, Last_name=Data
#print("First_Name:",first_name,"\nLast_Name:",Last_name)
Answer:32
#Enter your  name:Rahul Kumar
#First_Name: Rahul 
#Last_Name: Kumar
Question:33
#Take three integers in one line using .split().

#Example:

#10 20 30
#Convert them to integers and print their sum.
Answer:33
#Data= (input("Enter any three numbers:").split( ))
#first,second,third=Data
#print(int(first)+int(second)+int(third))
Answer:33
#Enter any three numbers:10 20 30
#60
Question:34
#Input:

#Rahul,20,BTech,Ahmedabad
#Use:

#.split(",")
#to separate the information.

#Display:

#Name: Rahul
#Age: 20
#Course: BTech
#City: Ahmedabad
Answer:34
#Data=input("Enter your personal data:").split(",")
#Name, Age, Course, City=Data
#print("Name:",Name,"\nAge:",Age,"\nCourse:",Course,"\nCity:",City)
#Enter your personal data:Prince Kumar, 18, B.Tech, Ahmedabad
#Name Prince Kumar 
#Age  18 
#Course  B.Tech 
#City  Ahmedabad
Question:35
#Take a sentence from the user.

#Example:

#Python is very powerful
#Use .split() to obtain the words.

#Display:

#First word: Python
#Last word: powerful
#Also display the total number of words using the appropriate built-in operation.
Answer:35
#Data=input("Enter your sentence:").split( )
#First_word,miseed,miss, Last_word,= Data
#print("First word:", First_word,"\nLast word:",Last_word)
#Enter your sentence:python is very powerful.
#First word: python 
#Last word: powerful.
Question:36
#Write a statement that produces exactly:

#Hello
#world
#Use \n.
Answer:36
#print("Hello\nworld")
#Hello
#world
Question:37
#Write a program that produces:

#Name:   Rahul
#Age:    20
#City:   Ahmedabad
#Use \t.
#nswer:37
#Name="Rahul"
#Age=20
#CIty="Ahmadabad"
#print("Name:\t",Name,"\nAge:\t",Age,"\nCIty:\t",CIty)
#Name:    Rahul 
#Age:     20 
#CIty:    Ahmadabad
Question:38
#Write a program that displays exactly:

#C:\Python\Programs
#Use \\.
Answer:38
#print("C:\\Python\\Programs")
#C:\Python\Programs
Question:39
#Write a statement that displays:

#It's Python
#Use an appropriate escape sequence.
Answer:38
#print("It\'s Python")
Question:39
#Write a statement that displays:

#He said "Hello"
#Use an appropriate escape sequence.
Answer:39
#print("He said \"Hello\"")
#He said "Hello"
Question:40
#print("Python\nProgramming")
Answer:40
#Python
#Programming
Question:41
#Write a program that displays:

#Student Details

#Name:   Rahul
#Age:    20
#Course: B.Tech
#Use \n and \t.
Answer:41
#Data=input("Enter your data:").split( )
#Name,Age,Course=Data
#print("Name:\t",Name,"\n Age:\t",Age,"\nCourse: ",Course)
#Name:    Prinice 
# Age:    18 
#Course:  B.tech
Question:42
#Predict the output:

print("2026", "09", "09", sep="-")
Answer:42
#2026-09-09
Question:43
#Predict the output:

print("Hello", end=" ")
print("Python")
Answer:43
#Hello Python
Question:44
#Write a program that produces exactly:

#10-20-30
#40-50-60
#Use sep and end.
print("10","20","30", sep="-")
print("40","50","60", sep="-")
Answer:44
10-20-30
40-50-60
Question:45
#Take:

#ame
#Age
#City
#Course
#Display them using an f-string:

#Name= "Rahul"
#Age= 20
#City= "Ahmedabad"
#Course= "B.Tech"
#Answer:45
#print(f"Name: {Name}\n Age: {Age}\n City: {City}\n Course: {Course}")
#Name: Rahul
#Age: 20
#City: Ahmedabad
#Course: B.Tech
Question:46
#Take a price as input and display it with exactly two decimal places.
Answer:46
#print(f"45.00 \n 25.04")
45.00 
25.04
Question:47
#Find and correct the error:

#age = input("Enter age: ")
#print("Age after 5 years:", age + 5)
Answer:47
#age = input("Enter age: ")
#print("Age after 5 years:", int(age) + 5)
Question:48
#Find and correct the error:

#print('It's Python')
Answer:48
#print("'It's Python'")
Question:49
#Find and correct the error:

#text = "Python"
#print(text[1,4])
Answer:49
text = "Python"
#print(text[1:4])
Question:50
#The program is:

#a, b = input().split(",")
#The user enters:

#10 20
#Why does the program fail?

#Rewrite it correctly for the given input.
Answer:50

#print(a,b)
#10 20
Question:51
#What will this program print?

#a, b = input().split()

#print(a + b)
#Input:

#10 20
#Then modify the program so that it performs numeric addition.
Answer:51
# a, b = input().split( )
# print(int(a) + int(b))
Question:52
# Find and correct the problem:

# print("C:\new\test")
# The programmer wants to display:

# C:\new\test
# What special-character problem can occur here?
Answer:52
#print("C:\\new\\text")
Question:53
#Take:

#Student name
#Three subject marks
#Calculate:

#Total
#Average
#Display the student's information using an f-string.

#Test Case
#Input:
#Rahul
#70 80 90
#Expected:

#Name: Rahul
#Total: 240
#Average: 80.00
#Use:

#input()
#.split()
#Type casting
#Arithmetic operators
#f-strings
Answer:53
Data=input("Enter your data:").split(",")
student_Name, maths, history, physics=Data
print("NAme",student_Name)
print("Total MArks=",int(maths)+int(history)+int(physics))
print("Average marks", (int(maths)+int(history)+int(physics))/3)
#Enter your data:Prince kumar, 50,30,60
#NAme Prince kumar
#Total MArks= 140
#Average marks 46.666666666666664
Question:54
# A student enters:

# BTECH-24-CSE-105
# Write a program that:

# Takes the ID as input.
# Uses .split("-") to separate the parts.
# Displays:
# Degree
# Batch
# Branch
# Roll Number
# Uses string slicing to extract the last three characters from the original ID.
# Converts the roll number into an integer.
# Prints the roll number.


















