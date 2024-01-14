## TypeError
# len(123)

## Data Types

## String - string of characters
# print("Hello"[0]) # subscripting via index 
# str = "Hello"
# strLength = len(str)

## IndexError
# print(str[strLength])

# print("The last character of the string " + str + " is " + str[strLength - 1])

## Integer
#print(23 + 345)

## Large integers easy visualization
# print(123_456_789) 

## Float
# print(123.4_5678)

## Boolean
# print(True)

## TypeError
# num_char = len(input("What is your name?"))
# print("Your name has " + num_char + " characters.")

# Type casing or converting
# num_char = len(input("What is your name?"))
# print("Your name has " + str(num_char) + " characters.")

# <class 'int'>
# print(type(4355))

# a = float(234)
# print(70 + float("100.5"))

## two digit task
# two_digit_number = input();
# first_digit = int(two_digit_number[0])
# second_digit = int(two_digit_number[1])
# print(first_digit + second_digit)

## Math operations
# print(6/3) # always floating point number

# PEMDASLR
# P() 
# E** 
# LR => M* D/  
# LR => A+ S-

# print(3 * (3 + 3) / 3 - 3)


### BMI
# height = input()
# weight = input()

# height_as_float = float(height)
# weight_as_int = int(weight)

##  PEMDASLR !!! v1 
# bmi = weight_as_int / height_as_float ** 2

## PEMDASLR !!! v2
# bmi = weight_as_int / (height_as_float * height_as_float)

# bmi_as_int = int(bmi)
# print(bmi_as_int)
###

# print(round(8/3, 0)) 

## floor division
# print(8 // 3)
#result = 8 // 3
#result //= 2

# f-String
# print(f"Your is {result}")


### Weeks left task
# age = input()
# years = 90 - int(age)
# weeks = years * 52

# print(f"You have {weeks} weeks left.")

# print(6 + 4 / 2 - (1 * 2))

### TIP calculator
# print("Welcome to the tip calculator.")

# bill = float(input("What was the total bil? $"))
# tip = int(input("What percentage top would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill? "))
# tip_as_percent = tip / 100
# # here we have a % shortcut by multipliing total by 1.% which means [total * 1.12 => 12%, or total * 1.15 => 15% ...] 
# total_bill = bill * (1 + tip_as_percent)
# bill_per_person = total_bill / people;
# final_amount = round(bill_per_person, 2) 
# final_amount = "{:.2f}".format(final_amount)

# print(f"Each person should pay: ${final_amount}")*