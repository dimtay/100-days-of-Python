## conditional

### Example 1
# water_level = 50
# if water_level > 80:
#     print("Drain water")
# else:
#     print("Continue")
###    
    
    
### Example 2
print("Welcome to the rollercoaster!")    

height = int(input("What is your heighy in cm?"))

# # >, <, >=, <=, !=, ==
if height >= 120:
    print("You can ride the rollercoaster")
    
    age = int(input("What is your age?"))
    bill = 0
    if age < 12:
        bill = 7
    elif age <= 18:
        bill = 12
    else:
        bill = 15  
    
    if input("Photo?") == "Y":
        bill += 3
    
    print(f"Your bill is {bill}")
else:
    print("Sorry, you have to grow a bit :-)")
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