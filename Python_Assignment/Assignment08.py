Question:1 
# A registration form asks the user for their name.

# Requirements:

# The name must not be empty.
# Remove spaces from the beginning and end.
# If the input is empty or contains only spaces, display an error and ask again.
# Accept any non-empty name for this question; character validation is not required yet.
# Sample Output:

# Enter your name:    
# Name cannot be empty. Please try again.
# Enter your name:   Aman   
# Name accepted: Aman

Answer:1 
# while True:
#     name = input("Enter your name:").strip()
#     if name == "":
#         print("Invalid name")
        
#     else:
#         print("Name accepted")
#         break


Question:2 
# A website asks for the user's age.

# Requirements:

# The age must be a whole number.
# The age must be greater than 0.
# If the user enters text such as twenty, handle the conversion error.
# Ask again until a valid age is entered.
# Sample Output:

# Enter your age: abc
# Please enter a whole number.
# Enter your age: -5
# Age must be greater than 0.
# Enter your age: 18
# Age accepted: 18


Answer:2 
# while True:
#     try:
#         age = int(input("Enter your age in whole number:"))
#         if age > 0:
#             print("Age accepted")
#             break
#         else:
#             print("Age must be greater than zero. Try again.")
#     except ValueError:
#         print("Please enter a valid integer. Try again.")


Question:3
# A teacher enters a student's exam marks.

# Requirements:

# Marks must be a valid number.
# Marks must be between 0 and 100, inclusive.
# Decimal marks are allowed.
# Ask again until valid marks are entered.
# Sample Output:

# Enter marks: 105
# Marks must be between 0 and 100.
# Enter marks: eighty
# Please enter a valid number.
# Enter marks: 86.5
# Marks accepted: 86.5

Answer:3
# while True:
#     try:
#         marks = float(input("Enter your marks:"))
#         if 0<=marks<=100:
#             print("Marks accepter:",marks)
#             break
#         else:
#             print("marks must be between 0 and 100")
            

#     except ValueError:
#         print("invalid input")




Question:4 
# A student is registering for a college event and must enter their full name.

# Requirements:

# The name must not be empty.
# Remove extra spaces from the beginning and end.
# Only English letters and spaces are allowed.
# Names may contain spaces between words.
# Do not use lists or split().
# Ask again until a valid name is entered.
# Sample Output:

# Enter your full name:    
# Name cannot be empty. Please try again.
# Enter your full name: Aman123
# Name should contain English letters and spaces only.
# Enter your full name: Aman Verma
# Name accepted: Aman Verma

Answer:4 



Question:5 
# A website asks the user to create a username.

# Requirements:

# The username must not be empty.
# Only English letters and digits are allowed.
# Spaces and special characters are not allowed.
# Use string methods such as isalnum().
# Ask again until a valid username is entered.
# Sample Output:

# Create username: aman verma
# Username can contain only letters and digits.
# Create username: aman@123
# Username can contain only letters and digits.
# Create username: aman123
# Username accepted: aman123

Answer:5 
# while True:
#     username = input("Enter username:").strip()
#     if username!="" and username.isalnum():
#         print("username accepted")
#         break
#     else:
#         print("not accept")

    
Question:6 
# A registration page asks for an email address.

# Required regex pattern:

# r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
# Requirements:

# Use import re.
# Use re.fullmatch() with the provided pattern.
# Ask again until the email matches the pattern.
# Display an error message for invalid input.


Answer:6
# while True: 
#     import re 
#     email = input("Enter emailaddress:").strip()

#     if re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",email):
#         print("Email format looks valid")
#     else:
#         print("Invalid email format")


Question:7 
# A delivery application asks for the customer's Indian mobile number.

# Required regex pattern:

# r"[6-9][0-9]{9}"
# Requirements:

# The number must match the pattern exactly.
# It must contain ten digits and begin with a digit from 6 to 9.
# Spaces, letters, and extra digits are not allowed.
# Ask again until a valid-format number is entered.
# Sample Output:

# Enter mobile number: 1234567890
# Invalid mobile number. Please try again.
# Enter mobile number: 987654321
# Invalid mobile number. Please try again.
# Enter mobile number: 9876543210
# Mobile number format accepted.

Answer:7
# while True:
#     import re
#     mobile_number = input("Enter an intiger:").strip()
#     if re.fullmatch(r"[6-9][0-9]{9}",mobile_number):
#         print("mobile number accepted")
#         break
#     else:
#         print("in correct format")



Question:8 
# A user is booking movie tickets.

# Requirements:

# The number of tickets must be a whole number from 1 to 8, inclusive.
# Handle text and decimal input without crashing.
# Allow a maximum of 3 invalid attempts.
# If all three attempts are invalid, display Booking cancelled due to invalid input.

Answer:8 
# i=0
# while i<3:
#     try:
#         ticket_number = int(input("Enter an intiger:"))
#         if 1<=ticket_number<=8:
#             print("ticket aproved")
#             break
#         else:
#             print("Enter a quantity from 1 to 8")
#     except ValueError:
#         print("Please enter a whole number.")
#     i+=1
# else:
#     print("Booking cancelled due to invalid input")


Question:9 
# A user enters a four-digit PIN to continue.

# Required regex pattern:

# r"[0-9]{4}"
# Requirements:

# Use the provided regex pattern and re.fullmatch().
# Give the user a maximum of 3 attempts.
# Count each invalid PIN entry as one failed attempt.
# If all attempts fail, display Access locked.

Answer:9 
# i = 0
# while i<3:
#     import re
#     ATM_pin= input("Enter atm pin:")
#     if re.fullmatch(r"[0-9]{4}",ATM_pin):
#         print("ATM pin accepted")
#         break
#     else:
#         print("invalid format")
#     i+=1

# else:
#     print("access locked")



Question:10
# A banking application asks how much money the user wants to transfer.

# Requirements:

# The amount must be numeric.
# It must be greater than 0.
# It must not exceed 50000.
# Decimal amounts are allowed.
# Allow a maximum of 3 invalid attempts.
# If all attempts fail, display Transfer cancelled.

Answer:10 
# i = 0
# while i<3:
#     try:
#         amount = float(input("Enter how much amout you want to transfer:"))
#         if 0<amount<50000:
#             print("Transfer amount accepted:",amount)
#             break
#         elif amount<0:
#             print("Amount must be greater than 0.")
#         else:
#             print("Amount cannot exceed 50000.")
#     except ValueError:
#         print("invalid transfer amount")
#     i+=1

# else:
#     print("Transfer cancelled")




