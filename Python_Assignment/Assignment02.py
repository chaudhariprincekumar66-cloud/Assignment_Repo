Question:1
#Convert "25" into an integer and print its value and type.
Answer:1
print(int("25"))
25

Question:2
#Convert "75.5" into a float and print its value and type.
Answer:2
print(float("75.5"))
75.5

Question:3
#Convert 50 into a float.
Answer:3
print(float(50))
50.0

Question:4
#Convert 85.9 into an integer.
Answer:4
print(int(89.9))
89

Question:5
#Convert the integer 101 into a string and print its value and type.
print(type(str(101)))

Question:6
#Convert the following values:

#"18" → int
#"92.5" → float
#100 → str
#45.8 → int
#Print every converted value with its type.
Answer:6
print(type(int("18")))
print(type(float("92.5")))
print(type(str(100)))
print(type(int(45.8)))
#<class 'str'>
#<class 'int'>
#<class 'float'>
#<class 'str'>
#<class 'int'>

Question:7
#Find the error and write one correct version of the complete code.
#age = "19"
#new_age = age + 1

#print("Age:", new_age)
#can only concatenate str (not "int") to str
age = 19
increases_in_age=1
new_age = (age + increases_in_age)

print("Age:", new_age)
Question:8
#Marks are stored as a string:              
#marks = " 85"      
# Convert the marks into an integer and add 5 bonus marks.
# Answer:8
marks=85
bonus=5
total_marks=(marks+bonus)
print(total_marks)  
#90

Question:9
#A product price is stored as a string:

#price = "1499.50"
#Convert it into a float and add 99.50 delivery charges.    
Answer:9
price=1499.50
delivery_charge=99.50
total_charge=(price+delivery_charge)    
print(total_charge)      
#1599.0

Question:10
#Create:

a = 20
b = 6
#Perform and print:

#Addition
#Subtraction
#Multiplication
#Division
#Floor division
#Remainder
#Power                                   
Answer:10
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)
#26
#14
#120
#3.3333333333333335
#2
#3
#64000000

Question:11
#Predict the output:

a = 17
b = 5

print(a / b)
print(a // b)
print(a % b)
Answer:11
#Explain in one or two sentences why the three results are different.
#/--> for divition   
#//--> for after divition take modulus
#%--> for get remainder

Question:12
#Predict  output:

#result = 10 + 5 * 2
#print(result)
#Now rewrite the expression so that addition happens first.
Answer:12
print((10+5)*2)
#30

Question:13
#Predict the output:

#result = 20 - 4 * 3 + 2
#print(result)
#Then rewrite the expression using parentheses to make the order of calculation clear.
Answer:13
print(20-(4*3)+2)

Question:14
#Predict the output:

#print(2 ** 3)
#print(3 ** 2)
#print(10 ** 2)
#Then create:

#side = 5
#and calculate the area of a square.
Answer:14
print(2 ** 3)
print(3 ** 2)
print(10 ** 2)

area_of_square=(5*5)
print(area_of_square)
#25
Question:15
#A student buys:

Notebook = 80
Pen = 20
Pencil = 10
#Create variables andcalculate the total amount.
Answer:15
total=(Notebook+Pen+Pencil)
print(total)
#110

Question:16
#A student buys:

#2 pens at ₹15 each
#1 calculator at ₹500
#Calculate the cost of each category and the total bill.
per_pen=(15/2)
calculator_at=500
total_bill=(2*per_pen+calculator_at)
print(per_pen)
print(calculator_at)
print(total_bill)
Question:17
#A class has 47 students. They are divided into groups of 5.

#Find:

#Complete groups
#Students left over
Answer:17
complete_group=(47//5)
students_left_over=(47%5)
print(complete_group)
print(students_left_over)
Question:18
#A student scored:

#Python = 85
#Mathematics = 78
#Physics = 92
#Calculate total and average marks.
Answer:18
total_marks=(85+78+92)
average_marks=((85+78+92)/3)
print(total_marks)
print(average_marks)


Question:19
#A student scored:

#English = 78
#Mathematics = 85
#Python = 92
#Physics = 81
#Chemistry = 74
#Each subject is out of 100.

#Calculate total marks and percentage.
Answer:19
total_marks=(78+85+92+81+74)
persentage=((78+85+92+81+74)/500)*100
print(total_marks)
print(persentage)
Question:20
#Given:

#number = 583
#Find the ten digit.
Answer:20
ones_digit_number=((583%100)//10)
print(ones_digit_number)

Question:21
#Given:

#number = 746
#Find:

#Ones digit
#Tens digit
#Hundreds digit
Answer:21
ones_digit_number=((746%100)%10)
ten_digit_number=((746%100)//10)
hundread_digit_number=(746//100)
print(ones_digit_number)
print(ten_digit_number)
print(hundread_digit_number)
Question:22
#Given:

#number = 5829
#Find:

#Ones digit
#Tens digit
#Hundreds digit
#Thousands digit
Answer:22
ones_digit_number=(((5829%1000)%100)%10)
ten_digit_number=(((5829%1000)%100)//10)
hundread_digit_number=((5829%1000)//100)
thousand_digit_number=(5829//1000)

Question:23
#Given:

#number = 583
#Find the three digits and calculate their sum.
Answer:23
ones_digit_number=((583%100)%10)
ten_digit_number=((583%100)//10)
hundread_digit_number=(583//100)
print(ones_digit_number)
print(ten_digit_number)
print(hundread_digit_number)
print(ones_digit_number+ten_digit_number+hundread_digit_number)
Question:24
#Given:

#number = 4726
#Find all four digits and calculate their sum.
Answer:24
ones_digit_number=(((4726%1000)%100)%10)
ten_digit_number=(((4726%1000)%100)//10)
hundread_digit_number=((4726%1000)//100)
thousand_digit_number=(4726//1000)
print(ones_digit_number)
print(ten_digit_number)
print(hundread_digit_number )
print(thousand_digit_number)
print(ones_digit_number+ten_digit_number+thousand_digit_number+hundread_digit_number)

Question:25
#Given:

#number = 234
#Find the three digits and calculate their product.
Answer:25
ones_digit_number=((234%100)%10)
ten_digit_number=((234%100)//10)
hundread_digit_number=(234//100)
print(ones_digit_number)
print(ten_digit_number)
print(hundread_digit_number)
print(ones_digit_number*ten_digit_number*hundread_digit_number)
Question:26
#Given:

#number = 583
#Create the reversed number using arithmetic operators.
Answer:26
ones_digit_number=((583%100)%10)
ten_digit_number=((583%100)//10)
hundread_digit_number=(583//100)
hundread_digit_number*100+ten_digit_number*10+ones_digit_number
print(ones_digit_number,ten_digit_number,ones_digit_number)
# print(ones_digit_number*100+ten_digit_number*10+hundread_digit_number)
str(hundread_digit_number)+str(ten_digit_number)+str(ones_digit_number)
print(str(hundread_digit_number)+str(ten_digit_number)+str(ones_digit_number)
)
Question:27
#Given:

#number = 4726
#Reverse the number using arithmetic operators.
Answer:27
print("6"+"2"+"7"+"4")
Question:28
#Given:

#number = 5834
#Display the place-value contribution of every digit.
Answer:28
place_value_of_thousand_digit=(5834//1000)*1000
place_value_of_hundread_digit=(5834%1000)//100*100
place_value_of_ten_digit=((5834%1000)%100)//10*10
place_value_of_one_digit=((5834%1000)%100)%10*1
print(place_value_of_thousand_digit)
print(place_value_of_hundread_digit)
print(place_value_of_ten_digit)
print(place_value_of_one_digit)
Question:29
#Given:

#number = 583
#Find the hundreds digit and ones digit and calculate their difference.
Answer:29
place_value_of_hundread_digit=(583//100)*100
place_value_of_onedigit_digit=(583%100)%10
print(place_value_of_hundread_digit)
print(place_value_of_one_digit)
Question:30
#The program is intended to print the ones digit.

#Find the error and correct the code.

#number = 583
#ones = number / 10

#print("Ones Digit:", ones)
Answer:30
number= 583
ones= (number%100)%10
print(ones)
Question:31
#Write a program for:

#number = 9365
#Print:

#Thousands Digit:
#Tens Digit:
#Ones Digit:
Answer:31
ones_digit_number=(((4726%1000)%100)%10)
ten_digit_number=(((4726%1000)%100)//10)
thousand_digit_number=(4726//1000)
print("Thousands Digit:",thousand_digit_number)
print("Tens Digit:",ten_digit_number)
print("Ones Digit:",ones_digit_number)
Question:32
#Given:

hundreds = 5
tens = 8
ones = 3
#Use arithmetic operators to create the number 583.
Answer:32
print(hundreds*100+tens*10+ones*1)
Question:33
#Given:

Principal = 10000
Rate = 5
Time=2

#Use:

#Simple Interest = (Principal × Rate × Time) / 100
Answer:33
simple_interest=(Principal*Rate*Time)/100
print(simple_interest)
Question:34
#A rectangle has:

Length = 15 
Width = 8 
#Calculate:

#Area
#Perimeter
Answer:34
Area=(Length*Width)
Perimeter=2*(Length+Width)
print(Area)
print(Perimeter)
Question:35
#A circle has radius 7 cm.

#Use:

#pi = 3.14
#and:

#Area = π × r²
#Calculate the area.
Answer:35
pi=3.14
r=7
Area=(pi*r*r)
print(Area)

Question:36
#Given:

celsius = 35
#Convert Celsius into Fahrenheit.
Answer:35
Fahrenheit=(celsius*9/5)+32
print(Fahrenheit)
Question:36
#A video is 367 seconds long.

#Use // and % to find complete minutes and remaining seconds.
Answer:36
complete_minutes=(367//60)
remaining_seconds=(367%60)
print(complete_minutes)
print(remaining_seconds)
Question:37
#Given:

#total_seconds = 7384
#Convert into:

#Hours
#Minutes
##SecondsGiven:

#total_seconds = 7384
#Convert into:

#Hours
#Minutes
#Seconds
Answer:37
hours=(7384/3600)
minutes=(7384/60)
print(hours)
print(minutes)
Question:38
#An employee has:

#Basic Salary = ₹25000
#HRA = ₹5000
##Travel Allowance = ₹2500
#Tax Deduction = ₹3000
#Calculate:

#Gross salary
#Net salary
Answer:38
Gross_salary=25000-2500-3000-5000
net_salary=25000
print(Gross_salary)
print(net_salary)
Question:39
#A person travels 120 km.

#The vehicle gives 20 km per litre and fuel costs ₹100 per litre.

#Calculate:

#Fuel required
#Total fuel cost
Answer:39
Fuel_required=(120/20)
Total_fuel_cost=(Fuel_required*100)
print(Fuel_required)
print(Total_fuel_cost)
Question:40
#Given:

#price = "2500"
#discount = "10"
#Convert the values into suitable numeric types.

#Calculate:

#Discount amount
#Final price
Answer:40
Discount_amount=(2500*10)/100
Final_price=2500-(2500*10)/100
print(Discount_amount)
print(Final_price)
Question:41
#Given:

price = "1200"
quantity = "4"
#Convert both into integers and calculate the total price.
Answer:41
print(int(price))
print(int(quantity))
total_price=(1200*4)
print(total_price)
Question:42
#Marks are stored as strings:

python_marks = 85
math_marks = 78
physics_marks = 91
#Convert them into integers and calculate:

#Total marks
#Average marks
Answer:42
total_marks=(python_marks+math_marks+physics_marks)
average_marks=(python_marks+math_marks+physics_marks)/3
print(total_marks)
print(average_marks)
Question:43
#Given:

#price = "1500"
#quantity = "2"
#tax_rate = "5"
#Convert the values and calculate:

#Subtotal
#Tax amount
#Final bill
Answer:43
subtotal= (1500-(1500*5/100))*2
Tax_amount=(1500*5/100)
final_bill=(subtotal+Tax_amount)
print(subtotal)
print(Tax_amount)
print(final_bill)
Question:44
#A product costs ₹2000.

#Discount = 15%

#GST = 18%

#Apply the discount first and calculate GST on the discounted price.

#Display:

#Discount amount
#Price after discount
#GST amount
#Final price
Answer:45
Discount_amount=(2000*15)/100
price_after_discount=2000-(2000*15)/100
GST_amount=((price_after_discount)*18)/100
final_price=(price_after_discount+GST_amount)
print(Discount_amount)
print(price_after_discount)
print(GST_amount)
print(final_price)










