Question:1
# Task: Print the pattern shown, adjusting its size based on the input.
# A
# BB
# CCC
# DDDD
# EEEEE
Answer:1
# Alphabate = input("Enter a limited alphabate=").split(",")
# for i in Alphabate:
#     for j in range(ord(i)-ord("A")+1):
#         print(i,end="")
#     print()
    


Question:2
# Task: Print the pattern shown, adjusting its size based on the input.
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
Answer:2

# n = int(input("Enter N: "))
# num = 1

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(num, end=" ")
#         num += 1
#         if num > 15:
#             break
#     if num>15:
#         break
#     print()


# Question:3
# # Task: Print the pattern shown, adjusting its size based on the input.
# Answer:3
# N = int(input("Enter an intiger = "))
# k = 0
# for i in range(1,N):
    
#     for j in range(i):
#         print(k,end="")
#         if k == 1:
#             k=0
#         else:
#             k=1
#     print()


# other***********************************

# N = int(input("Enter an integer = "))

# for i in range(1, N + 1):
#     k = 1 if i % 2 != 0 else 0

#     for j in range(i):
#         print(k, end=" ")
#         k = 1 - k
#     print()


Question:4
# Task: Print the pattern shown, adjusting its size based on the input.
Answer:4
# N = int(input("Enter an integer = "))

# for i in range(0,N):
#     for j in range(N,i,-1):
#         print("*",end="")
#     print()


Question:5
# Task: Print the pattern shown, adjusting its size based on the input.
Answer:5
# N = int(input("Enter an integer = "))


# for i in range(N, 0,-1):
#     for j in range(0,N+1):
#         if i>j:
#             print(" ",end="")
#         else:
#             print("*",end="")
#     print()
        
Question:6
# Task: Print the pattern shown, adjusting its size based on the input.
Answer:6    
# N = int(input("Enter an integer = "))

# for i in range(0, N+1):
#     for j in range(0,N+1):
#         if i<j :
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
        

Question:7
# Task: Print the pattern shown, adjusting its size based on the input.
Answer:7



Question:8
# N = int(input("Enter a number="))
# p = N-1
# q = N+1
# for i in range(N):
#     for j in range(2*(N-1)+2):
#         if p<j and q>j:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     p -= 1
#     q += 1
#     print()


Question:9
# Task: Print the pattern shown, adjusting its size based on the input.
Answer:9
# N = int(input("Enter a number="))
# p = 0
# q = 2*N-2
# for i in range(N):
#     for j in range(2*(N-1)+1):
#         if p>j or q<j:
#             print(" ", end="")
#         else:
#             print("*", end="")
#     p += 1
#     q -= 1
#     print()


# Question:10
# N = int(input("Enter a number="))
# p = N-1
# q = N+1
# for i in range(N):
#     for j in range(2*(N-1)+2):
#         if p<j and q>j:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     p -= 1
#     q += 1
#     print()

# w = 2
# k = 2*(N-1)
# for i in range(N-1):
#     for j in range(2*(N-2)+5):
#         if w>j or k<j:
#             print(" ", end="")
#         else:
#             print("*", end="")
#     w += 1
#     k -= 1
#     print()



Question:11 
# Task: Print the pattern shown, adjusting its size based on the input.
Answer:11 
# N = int(input("Enter an intiger = "))
# p=0
# q=0

# for i in range(N):
#     for j in range(0,2*(N-1)+2):
#         if (N-p)<=j and j<=(2*(N-1)+1-q):
#             print("*",end="")
#         else:
#             print(" ", end="")
#     print()
#     p+=1
#     q+=1

Question:12
# Print the pattern shown, adjusting its size based on the input.
# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321
Answer:12
# N = int(input("Enter an intiger = "))
# p = ""
# q = ""
# c = 2*N-2
# for i in range(1,N+1):
#     p = p + str(i)

#     q = str(i) + q

#     for j in range(0,2*N-2*(len(p)-1)):
#         if j<1:
#             print(p,end="")
#         elif j>=2*N-2*(len(p)-1)-1:
#             print(q,end="")
#         else:
#             print(" ",end="")
#     print()



Question:13
# Print the pattern shown, adjusting its size based on the input.
#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5
Answer:13

# a  = int(input())
# p = a-1
# q = a-1
# k=1
# l=1
# for i in range (a):
#     for j in range((a*2)-1):
#         if (j>=p and j<=q):
#             if(l==1):
#                 print(k,end="")
#                 l+=1
#                 k+=1
#             elif(l%2==0):
#                 print(" ",end="")
#                 l+=1
#             else:
#                 print(k,end="")
#                 l+=1
#                 k+=1
               

#         else:
#             print(" ",end="")
#             l=1
#             k=1
#     p-=1
#     q+=1
#     print()

           
Question:14 
# Task: Print the pattern shown, adjusting its size based on the input.
#     1
#    121
#   12321
#  1234321
# 123454321
Answer:14 
# N = int(input("Enter an intiger = "))
# p = ""
# b = ""
# for i in range(1,N+1):
#     q = len(p)
#     l = 2*(N-1)+2-q
#     for j in range(-1,l-1):
#         if j == (N)-q:
#             print(i,end="")
#         elif j==(N)-q-1:
#             print(p,end="")
#         elif j == (N)-q+1:
#             print(b,end="")
#         else:
#             print(" ",end="")
#     p = p+str(i)
#     b = str(i)+b

#     print()



Question:15 
# Task: Print the pattern shown, adjusting its size based on the input.
#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA

Answer:15 

# word = (input("Enter an intiger = "))
# N = len(word)
# p = ""
# b = ""
# for i in range(0,N):
#     q = len(p)
#     l = 2*(N-1)+2-q
#     for j in range(-1,l-1):
#         if j == (N)-q:
#             print(word[i],end="")
#         elif j==(N)-q-1:
#             print(p,end="")
#         elif j == (N)-q+1:
#             print(b,end="")
#         else:
#             print(" ",end="")
#     p = p+ word[i]
#     b =  word[i]+b

#     print()

Question:16 
# Task: Print the pattern shown, adjusting its size based on the input.
# E
# D E
# C D E
# B C D E
# A B C D E
Answer:16 
# N = int(input("Enter a word for print as ="))
# p = 0
# q = ""
# for i in range(N):
#     p = p + 1
#     q = chr(65+N-1-i) + q
#     for j in range(N):
#         print(q,end= "")
#         if j == 0:
#             break
#     print()


Question:17 
# Task: Print the pattern shown, adjusting its size based on the input.
# 12345
# 1234
# 123
# 12
# 1
# 12
# 123
# 1234
# 12345
Answer:17 
# N = int(input("ENter an intiger ="))
# for i in range(N,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# for i in range(1,N):
#     for j in range(1,i+2):
#         print(j,end="")
#     print()


Question:18
# Task: Print the pattern shown, adjusting its size based on the input.
# *#*#*
# #*#*#
# *#*#*
# #*#*#
# *#*#*

Answer:18 

# n = int(input("Enter the size of the grid: "))

# for i in range(n):
#     for j in range(n):
#         if (i + j) % 2 == 0:
#             print("*", end="")
#         else:
#             print("#", end="")
#     print() 

Question:19 
# 1
# 21
# 123
# 4321
# 12345

# N = int(input("ENter an intiger = "))
# for i in range(1,N+1):
#     for j in range(1,i+1):
#         if i%2 != 0:
#             print(j,end="")
#         else:
#             print(i+1-j,end="")
#     print()


Question:20 
# Task: Print the pattern shown, adjusting its size based on the input.
Answer:20
# N = int(input("Enter an intiger = "))
# q = 0
# p = 2*(N-1)+1
# for i in range(N):  
#     q = 0
#     for j in range(p):
#         if j<=i :
#             print(N-j,end=" ")

#         elif j>=p-i-1:
#             if i== N-1:
#                 print(N-i+1+q,end=" ")
#                 q = q + 1

#             else:

          
#                 print(N-i+q,end=" ")
#                 q = q + 1

#         else:
#             print(N-i, end=" ")
#     print()

# q = 0
# p = 2*(N-1)+1
# for i in range(1,N):  
#     q = 0
#     for j in range(p):
#             if j<N-i:
#                 print(N-j,end=" ")
#             elif j>=N+i:
#                 q = q + 1

#                 print(N+1+i-(N-q),end=" ")



#             else:
#                 print(i + 1,end=" ")

#     print()


Question:21 
# Task: Print the pattern shown, adjusting its size based on the input.
Answer:21 
# *****
# *   *
# *   *
# *   *
# *****
# N = int(input("Enter an intiger = "))
# for i in range(N):
#     for j in range(N):
#         if i == 0 or i == N-1:
#             print("*",end="")
#         else:
#             if j == 0 or j == N-1:
#                 print("*",end="")
#             else:
#                 print(" ",end="")
#     print()

        
Question:22
# Task: Print the pattern shown, adjusting its size based on the input.     
# *
# **
# * *
# *  *
# *****

# N = int(input("Enter an integer = "))

# for i in range(N):
#     for j in range(i + 1):
#         if j == 0 or j == i or i == N - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()  


Question:23
# Task: Print the pattern shown, adjusting its size based on the input.
Answer:23 
# N = int(input("Enter an integer = "))


# for i in range(N,0,-1):
#     for j in range(1,i+1):
#         if i == N or i == j or j == 1:
#             print("*", end="")
#         else:
#             print(" ",end="")
#     print()
        


Question:24
# Task: Print the pattern shown, adjusting its size based on the input.
#     *
#    * *
#   *   *
#  *     *
# *********
Answer:24 
# N  = int(input("Enter an intiger = "))
# p = 0
# for i in range(N):
#     for j in range(2*(N-1)+1):

#         if  j == N-1-p or j == N-1+p or i == N-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     p = p + 1

#     print()




Question:25 
# Task: Print the pattern shown, adjusting its size based on the input.
Answer:25 
# N = int(input("Enter an intiger = "))
# p = 0
# for i in range(N):
#     p = p + 1
#     for j in range(N):
#         if i == j or j == N-p:
#             print("*", end="")
#         else: 
#             print(" ",end="")
#     print()




Question:26 
# Task: Print the pattern shown, adjusting its size based on the input.
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *


Answer:26 
# N = int(input("Enter an intiger = "))
# p=0
# for i in range(N):
#     p = p +1
#     for j in range(2*N):
#         if j<p or j>2*N-1-p:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
# q = 0
# for i in range(N-1):
#     q = q + 1
#     for j in range(2*N):
#         if j<N-q or j >= N+q:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()



Question:27 
# Task: Print the pattern shown, adjusting its size based on the input.
#  **   **
# **** ****
# *********
#  *******
#   *****
#    ***
#     *
Answer:27 
# N = int(input("Enter an odd intiger = "))
# p = 0
# for i in range(N-2):
#     p = p + 1

#     for j in range(0,2*(N-1)+2):

#         if (N-1)/2-p-1<j<(N-1)/2+p or N+(N-1)/2-p< j<=N+(N-1)/2+p:
#             print("*",end="")
#         else:
#             print(" ",end="")

#     print()
# q = 0
# for i in range(N):
#     for j in range(2*(N-1)+2):
#         if q+1<=j<=2*(N-1)+1-q:
#             print("*",end="")
#         else:
#             print(" ", end="")
#     q = q + 1

#     print()


#  First N Fibonacci Numbers*******************************************************
Question:28 
# Task: Print the first N Fibonacci numbers, starting with 0, 1, 1, 2, 3, ....
Answer:28 
# N  = int(input("Enter an intiger = "))
# p = 0
# s = 1
# for i in range(N):
#     print(p,end=" ")
#     p ,s= s + p,p




# GCD of Two Numbers // *************************************************************************
Question:29 
# Task: Find the greatest common divisor (GCD) of two positive integers using a loop.
# a = int(input("Enter an intiger = "))
# b = int(input("Enter an intiger = "))
# p=0
# q=0
# if a>b:
#     for i in range(b,0,-1):
#         if a%i == 0:
#             p = i
#         if b%i == 0:
#             q = i
#         if p == q:
#             print("GCD=",p)
#             break

# else:
#     for i in range(a,0,-1):
#         if a%i == 0:
#             p = i
#         if b%i == 0:
#             q = i
#         if p == q:
#             print("GCD=",p)
#             break


#LCM of Two Numbers *****************************************************************8888888

Question:30 
# Task: Find the least common multiple (LCM) of two positive integers.
# Answer:30 
# a = int(input("Enter an intiger = "))
# b = int(input("Enter an intiger = "))
# p = 0
# q = 0
# if a>b:
#     for i in range(a,a*b+1):
#         if i%a == 0:
#             p = i
#         if i%b == 0:
#             q = i 
#         if p == q :
#             print("LCM =",p)
#             break

# else:
#     for i in range(b,a*b+1):
#         if i%a == 0:
#             p = i
#         if i%b == 0:
#             q = i 
#         if p == q :
#             print("LCM =",p)
#             break
































































