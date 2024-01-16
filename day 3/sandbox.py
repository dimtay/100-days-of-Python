## conditional

### Example 1
# water_level = 50
# if water_level > 80:
#     print("Drain water")
# else:
#     print("Continue")
###    
    
    
### Example 2
# print("Welcome to the rollercoaster!")    

# height = int(input("What is your heighy in cm?"))

# # # >, <, >=, <=, !=, ==
# if height >= 120:
#     print("You can ride the rollercoaster")
    
#     age = int(input("What is your age?"))
#     bill = 0
#     if age < 12:
#         bill = 5
#     elif age <= 18:
#         bill = 7 
#     elif age >= 45 and age <= 55:
#         print('FREE RIDE!!!!')
#     else:
#         bill = 12   
    
#     if input("Photo?") == "Y":
#         bill += 3
    
#     print(f"Your bill is {bill}")
# else:
#     print("Sorry, you have to grow a bit :-)")
###    


### Example 3
# number = int(input())

# if number % 2:
#     numberType = 'odd'   
# else:
#     numberType = 'even'
    
# print(f"This is an {numberType} number.")
###


### Example 4
# # Enter your height in meters e.g., 1.55
# height = float(input())
# # Enter your weight in kilograms e.g., 72
# weight = int(input())

# bmi = weight / height ** 2

# if bmi < 18.5:
#   interpretation = 'you are underweight.'
# elif bmi < 25:
#   interpretation = 'you have a normal weight.'
# elif bmi < 30:
#   interpretation = 'you are slightly overweight.'
# elif bmi < 35:
#   interpretation = 'you are obese.'  
# else:
#   interpretation = 'you are clinically obese.'  

# print(f"Your BMI is {bmi}, {interpretation}")

### 


### Example 5
# Which year do you want to check?
# year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         print("Leap year")
#       else:
#         print("Not leap year")
#     else:  
#       print("Leap year")  
# else:
#   print("Not leap year")
  
# # alternative based on the result history
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#       print("Leap year")  
# else:
#   print("Not leap year")
###

### Example 6
# print("Thank you for choosing Python Pizza Deliveries!")
# size = input() # What size pizza do you want? S, M, or L
# add_pepperoni = input() # Do you want pepperoni? Y or N
# extra_cheese = input() # Do you want extra cheese? Y or N
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇

# priceSmall = 15
# priceMedium = 20
# priceLarge = 25
# extraCheese = 1

# bill = 0
# if size == "S":
#   bill += priceSmall  
# elif size == "M":
#   bill += priceMedium;  
# else:  
#   bill += priceLarge
  
# if add_pepperoni == "Y":
#     if size == "S":        
#         bill += 2
#     else:
#         bill += 3
        
# if extra_cheese == 'Y':
#   bill += extraCheese

# print(f"Your final bill is: ${bill}.")
###


### Example 7
# print("The Love Calculator is calculating your score...")
# name1 = input() # What is your name?
# name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

# combined_names = name1 + name2
# lower_names = combined_names.lower()

# trueCount = lower_names.count('t') \
# + lower_names.count('r') \
# + lower_names.count('u') \
# + lower_names.count('e')

# loveCount = lower_names.count('l') \
# + lower_names.count('o') \
# + lower_names.count('v') \
# + lower_names.count('e')

# score = int(f"{trueCount}{loveCount}") # or str(trueCount) + str(loveCount)

# if score < 10 or score > 90:
#    print(f"Your score is {score}, you go together like coke and mentos.")
# elif score >=40 and score <= 50:
#    print(f"Your score is {score}, you are alright together.")
# else:
#    print(f"Your score is {score}.")    
###

### Example 8
direction = input("left or right?")

if direction == "left":
  print("You have reached a river. Do you want to swim or wait?")
  swim_or_wait = input().lower()
  if swim_or_wait == "wait":
    print("You have reached a house with three doors. Which door do you want to enter? Red, blue or yellow?")
    door = input().lower()
    if door == "yellow":
      print("You have found the treasure. You win!")      
    else:
      print("Game over.")
  else:
    print("Game over.")
else:
  print("Game over.")

###