# num_char = len(input("What's your name?"))

# new_num_char = str(num_char)

# print("Your name has " + new_num_char + " characters." )

# a = 123
# print(type(a))

# two_digit_num = input()

# first = int(two_digit_num[0])
# second = int (two_digit_num[1])

# total = first + second

# print(total)

# ***********Body Mass index (BMI)**************

# height = input()

# weight = input()

# weight_as_int = int(weight)
# height_as_float = float(height)


# bmi = weight_as_int / height_as_float ** 2
# bmi_as_int = int(bmi)
# print(bmi_as_int)

# ****************Your Life in Weeks***************

# your_age = input()

# years = 90 - int(your_age)
# weeks = years * 52

# print(f"You have {weeks} weeks left.")


# **************Tip Calculator******************

# print("\n*****Welcome to print calculator!********")

# bill = float(input("\nWhat was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 15 or 18? "))
# people = int(input("How many people to split the bill? "))

# total_tip_amount = tip / 100 * bill
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people

# final_amount = round(bill_per_person, 2)
# final_amount = "{:.2f}".format(bill_per_person)

# print(f"Each person should pay: ${final_amount}")


# *************Conditions******************

# print("Check to see if the number is odd or even, type a number? ")

# number = int(input())

# if number % 2 == 0:
#     print("You got it")
# else:
#     print("No no!")


# ************Rollercoaster Ride****************

# print("******* Welcome to RollerCoaster! **********")

# height = int(input("What is your height in cm? "))
# bill = 0
# if height >= 120:
#     print("You can ride the rollercoaster! ")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Kid tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Young adult tickets are $7.")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")
#     photo_added = input("Do you want to add photo? It's extra $3. 'Y' or 'N' ")
#     if photo_added == "Y":
#         bill += 3
#     print(f"Your final bill is ${bill}.")
# else:
#     print("Sorry, you can't ride!")


# **************Love Calculator***************

# print("\nWelcome to love calculator, it will calculate you compatibility, let's get started!\n")
# # Hint: program matches with the letters of 'True Love'

# your_name = str(input("What is your name? "))
# their_name = str(input("What is their name? "))

# combined_names = your_name + their_name

# lower_names = combined_names.lower()

# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")

# first_digit = t + r + u + e

# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")
# second_digit = l + o + v + e

# *****************Treasure Island Game********************

# print('''
# *******************************************************************************
#           |                   |                  |                     |
# __________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.") 

# choice1 = input('You\'re at the crossroad, where do you want to go? Type "left" or "right": \n').lower()

# if choice1 == "left":
#     choice2 = input("You have come to the lake, do you want to wait for boat or swim to the island? Type 'wait' or 'swim'? \n").lower()
#     if choice2 == "wait":
#         choice3 = input("Boat came, pick you up and drop you of at a castle, which door would you choose? Type 'red', 'yellow', 'blue'?: \n").lower()
#         if choice3 == "yellow":
#             print("\nYou win!")
#         elif choice3 == "red":
#             print("It's a fire room, game over!")
#         elif choice3 == "blue":
#             print("You enter a room of beasts. Game over!")
#         else:
#             print("You played very well but wrong answer, game Over!")
# else:
#     print("Game Over!")


# ***************Treasure Map***************

# line1 = [" "," "," "]
# line2 = [" "," "," "]
# line3 = [" "," "," "]

# map = [line1, line2, line3]

# print("Hiding your treasure X marks the spot.")
# print(f"{line1}\n{line2}\n{line3}")
# position = input("Where do you want to put your treasure?:\n")

# letter = position[0].lower()
# index_num = int(position[1]) - 1

# abc = ["a","b","c"]
# letter_index = abc.index(letter)

# map[index_num][letter_index] = "X"

# print(f"{line1}\n{line2}\n{line3}")

# ************Rock, Paper, Scissors*****************

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

game_images = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors game!\n")

player_choice = int(input("Please type 0 'Rock', 1 for 'Paper' or 2 for 'Scissors' to see if you win or lose the game, let's get started!\n"))

if player_choice >= 3 or player_choice < 0: 
  print("You typed an invalid number, you lose!") 
else: 
    print(game_images[player_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])


    if player_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and player_choice == 2:
        print("You lose")
    elif computer_choice > player_choice:
        print("You lose")
    elif player_choice > computer_choice:
        print("You win!")
    elif computer_choice == player_choice:
        print("It's a draw")