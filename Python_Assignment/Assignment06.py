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
# m = 0
# j = 2*N-2
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
# m = 2
# j = 2*(N)-4
# for i in range(N):
#     for j in range(2*(N-1)+1):
#         if p>j or q<j:
#             print(" ", end="")
#         else:
#             print("*", end="")
#     p += 1
#     q -= 1
#     print()















































































































































































