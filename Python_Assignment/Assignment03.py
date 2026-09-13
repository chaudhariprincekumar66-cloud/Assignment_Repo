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
number="12345678"
print(number[0:9:2])
Question:25
#Take a string as input and print:

#First three characters
#Last three characters
Answer:25
text="Programing"
print("first three letters:",text[:3])
print("Last three letters:",text[-3:])
#first three letters: Pro
#Last three letters: ing