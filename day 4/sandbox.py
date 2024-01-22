### Example 1 
# import random

# randInt = random.randint(1,1000);
# rand = int(random.random() * 5) + 1;

# print(randInt, rand)
###    

### Example 2
# import my.myModule
# #from myModule import *

# print(my.myModule.pi)
###    

### Example 3
# import random

# if random.randint(0, 1):
#     print('Tail')
# else:
#     print('Head')
###    

### Example 4
#list = ['a', 'b', 'c']

# IndexError
#print(list[-5])
###

### Example 5

# import random
# names = 'a, b, c, d, e'.split(", ")

# print(f"{names[random.randint(0, len(names) - 1)]} is going to buy the meal today!")
###

### Example 6

# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = 'B1' # Where do you want to put the treasure?
# # 🚨 Don't change the code above 👆
# # Write your code below this row 👇

# x = int(position[1]) - 1 
# letter = position[0].lower()

# abc = ['a', 'b', 'c']

# map[x][abc.index(letter)] = 'X'


# # Write your code above this row 👆
# # 🚨 Don't change the code below 👇
# print(f"{line1}\n{line2}\n{line3}")

###


### Example 6
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choice = int(input("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors."))
pcGen = random.randint(0,2)

rps = [rock, paper, scissors]

# my native approach is  a matrix approach LoL
map = [
    [0, -1, 1],
    [1, 0, -1],
    [-1, 1, 0]
]

if choice >= 3 or choice <0:
    print("Wrong choice:")
else:
    print(rps[choice])
    print("Computer chose:")

    pcChoice = rps[pcGen];
    print(pcChoice)

    result = map[choice][pcGen];

    if choice == 0 and pcGen == 2:
        print("You win")    
    elif pcGen == 0 and choice == 2:
        print("You loose")        
    elif pcGen > choice:
        print("You loose")    
    elif pcGen < choice:
        print("You win")        
    else:
        print("Draw")

    # if result == 1:
    #     print("Win")
    # elif result == -1:
    #     print("Lost")
    # else:
    #     print("Draw")
    ###