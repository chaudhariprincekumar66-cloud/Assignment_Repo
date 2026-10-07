Question:1
# Without running the code, write the values printed:

# for i in range(2, 15, 3):
#     print(i)
Answer:1
#2, 5, 8, 11, 14
Question:2
# Predict the output:

# for i in range(15, 2, -3):
#     print(i)
Answer:2
#15, 12, 9, 6,3
Question:3
# Without running the program, determine how many times the loop executes and list the values of i.

# for i in range(4, 31, 5):
#     print(i)
Answer:3
#4, 9, 14, 19, 24, 29
Question:4
# A student wants to print every third number from 3 through 18:

# for i in range(3, 18, 3):
#     print(i)
Answer:4
#3, 6, 9, 12, 15
Question:5
# Print each number from 5 to 10 along with its distance from 20.
# for i in range(5,11):
#     print(i,"1"+str(10-i) )

Question:6
# For every number from 1 to 6, print the number, its square, and its cube on one line.
Answer:6
# for i in range(1,7):
#     print(i,i*i,i*i*i)


Question:7
# Take start and end. Find the sum of all integers from start to end using one for loop.
Answer:7
# num = int(input("Enter a intiger:"))
# s = 0
# for i in range(num+1):
#     s = s+i
# print(s)

Question:8
# Take N and count how many numbers from 1 to N are divisible by 3.
# N = int(input("Enter an intiger:"))
# for i in range(N+1):
#     if i%3==0:
#         print(i)

Question:9
# Take N and calculate the sum of all numbers from 1 to N divisible by 4.
# s=0
# N = int(input("Enter an intiger:"))
# for i in range(1,N+1):
#     if i%4==0:
#         s=s+i
# print(s)

Question:10
# Take N and count numbers from 1 to N that are divisible by both 3 and 5.
# N = int(input("Enter an intiger:"))
# s = 0
# for i in range(1,N+1):
#     if i%3==0 and i%5==0:
#         s = s+1
# print(s)

Question:11
# Take N. Using one loop, count how many numbers from 1 to N are even and how many are odd.
# s = 0
# p = 0
# N = int(input("Enter an intiger:"))    
# for i in range(1,N+1):
#     if i%2==0:
#         s = s+1
#     else:
#         p=p+1
# print("Even number:",s)
# print("Odd number:",p)

Question:12
# Take N. Print the running sum after every number from 1 to N.
Answer:12
# N = int(input("Enter an intiger:"))
# s = 0 
# for i in range(N+1):
#     s = s+i
#     print(s)

Question:13
# Take N. Starting with 1, multiply by every number from 1 to N and print the product after each iteration.
Answer:13
# N = int(input("Enter an intiger:"))
# s = 1
# for i in range(1,N+1):
#     s = s*i
# print(s)


Question:14
# Take N and print the factorial of every number from 1 to N.
Answer:14
# N = int(input("Enter an intiger:"))
# s = 1
# for i in range(1,N+1):
#     s = s*i
#     print(s)

Question:15
# Take N and find the product of all even numbers from 2 to N.
Answer:15
# N = int(input("Enter an intiger:"))
# s = 1
# for i in range(2,N+1):
#     if i%2==0:
#         s = s*i
# print(s)

Question:16
# Take an even number N. Calculate:

# N × (N-2) × (N-4) × ... × 2

# Use one for loop.

Answer:16
# N = int(input("Enter a even number:"))
# s = 1
# for i in range(N,0,-1):
#     if i % 2==0:
#         s=s*i
# print(s)

Question:17
# Take N and calculate:

# 1² + 2² + 3² + ... + N²
Answer:17
# N = int(input("Enter an intiger:"))
# s = 0
# for i in range(1,N+1):
#     s = s + i**2
# print(s)

Question:18
# Take a positive integer and count its digits using a for loop. Do not convert the number to a string.
Answer:18
# N = int(input("Enter an intiger:"))
# s = 0
# import math
# val = int(math.log10(N))+1
# for i in range(1, val+1):
#     s = s +1
# print(s)

Question:19
# Take an integer and find the sum of its digits using one for loop.
Answer:19
# N = (input("Enter an intiger:"))
# s = 0
# for i in N:
#     s = s+int(i)
# print(s)

Question:20
# N = int(input("Enter an number:"))
# s = 1
# import math
# val = int(math.log10(N))+1
# for i in range(1,val+1):
#     p = N%10
#     s = s*p
#     N=N//10
# print()

Question:21
# Count how many digits of a given integer are even.
Answer:21
# N = int(input("Enter an intiger:"))
# s = 0
# import math
# val = int(math.log10(N))+1
# for i in range(1,val+1):
#     if N!=0:
#       N = N//10
#       if (N%10)%2==0:
#         s = s+1
# print(s)

Question:22
# Find the largest digit of a number using one for loop. Do not use max() and do not convert the number to a string.
Answer:22
# N = (input("Enter a number:"))
# for i in N:
#     print(i)






Question:24
# Reverse the digits of a positive integer using one for loop and % / //.
Answer:24
# N = int(input("Enter a number:"))
# s = ""
# import math
# val = int(math.log10(N))+1
# for i in range(0,val+1):
#    if N!=0:
      
#       s = s + str(N%10)
#       N = N//10

# print(s)

Question:25
# Check whether a number reads the same from left to right and right to left. Use one for loop.
# N = int(input("Enter a number:"))
# p = N
# s = ""
# import math
# val = int(math.log10(N))+1
# for i in range(0,val+1):
#     if N!=0:
#         s = s + str(N%10)
#         N = N//10
# if int(s)==p:
#     print("Palindrome Number")
# else:
#     print("Not a Palindron Number")

Question:26
# Take an integer and a target digit. Count how many times that digit occurs.
Answer:26
N = int(input("Enter a number:"))
digit = int(input("Enter digit for which you want to repeatation:"))
l=0
import math
val = int(math.log10(N))+1
for i in range(0,val+1):
    if N!=0:
        s = N%10
        N= N//10
        if s == digit:
            l = l+1
print(l)

Question:27















