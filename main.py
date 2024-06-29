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

# import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# game_images = [rock, paper, scissors]

# print("Welcome to Rock, Paper, Scissors game!\n")

# player_choice = int(input("Please type 0 'Rock', 1 for 'Paper' or 2 for 'Scissors' to see if you win or lose the game, let's get started!\n"))

# if player_choice >= 3 or player_choice < 0: 
#   print("You typed an invalid number, you lose!") 
# else: 
#     print(game_images[player_choice])

#     computer_choice = random.randint(0, 2)
#     print("Computer chose:")
#     print(game_images[computer_choice])


#     if player_choice == 0 and computer_choice == 2:
#         print("You win!")
#     elif computer_choice == 0 and player_choice == 2:
#         print("You lose")
#     elif computer_choice > player_choice:
#         print("You lose")
#     elif player_choice > computer_choice:
#         print("You win!")
#     elif computer_choice == player_choice:
#         print("It's a draw")

# **************Average Heights******************

# student_heights = input("What's the students heights? Type separately:\n").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])

# total_height = 0

# for height in student_heights:
#     total_height += height
# print(f"total height = {total_height}")

# number_of_students = 0

# for student in student_heights:
#    number_of_students += 1
# print(f"Number of students = {number_of_students}")

# average_height = round(total_height / number_of_students)
# print(f"Average height = {average_height}")


# **************Comparison of highest score**************

# student_scores = input().split()

# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])

# highest_score = 0

# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"Highest score is: {highest_score}")

# **************************************************
# target = int(input())
# even_sum = 0

# for num in range(2, target + 1):
#     if num % 2 == 0:
#         even_sum += num
# print(f"Total Number is: {even_sum}")

# ***************FizzBuzz************************

# target = 50

# for current_num in range(1, target + 1):
#     if current_num % 3 == 0 and current_num % 5 == 0:
#         print("FizzBuzz")
#     elif current_num % 3 == 0:
#         print("Fizz")
#     elif current_num % 5 == 0:
#         print("Buzz")
#     else:
#         print(current_num)


# ******************Password Generator**************

# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# password_list = []

# for char in range(1, nr_letters + 1):
#     password_list += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#     password_list += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#     password_list += random.choice(numbers)

# print(password_list)

# random.shuffle(password_list)

# password = ""

# for char in password_list:
#     password += char

# print(f"Your password is generated, it is: {password}")

# ********************** HANGMAN ********************
# import random
# from hangman_art import stages, logo
# from hangman_words import word_list
# import os

# end_of_game = False
# # word_list = ["conscience", "craftsman", "apparently"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

# # guess = input("\nWelcome to the 'Hangman' game, guess a letter: ").lower()

# lives = 6

# print(logo)

# print(f"\nFor testing, here is the word: {chosen_word}.")

# display = []
# for _ in range(word_length):
#     display += "_"
#     # print(display)



# while not end_of_game:
#     guess = input("\nWelcome to the 'Hangman' game, guess a letter: ").lower()

#     os.system('clear')

#     if guess in display:
#         print(f"You've already guessed {guess}")

#     for position in range(word_length):
#         letter = chosen_word[position]
#         # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter

#     if guess not in chosen_word:
#         print(f"You've guessed {guess}, that's not in the word. You lose a life.")
#         lives -= 1
#         if lives == 0:
#             end_of_game = True
#             print("You lose!")
#     print(f"{''.join(display)}")


#     # print(f"\n{display}")
#     if "_" not in display:
#         end_of_game = True
#         print("You win!")
#     print(stages[lives])

# ********************************************************
# ********************************************************
# ********************************************************

# import math
# def paint_calc(height, width, cover):
#     number_of_cans = (height * width) / cover
#     round_up_cans = math.ceil(number_of_cans)
#     print(f"You will need {round_up_cans} cans of paint.")


# test_h = int(input("Height of the wall?: "))
# test_w = int(input("Width of the wall?: "))

# coverage = 5

# paint_calc(height=test_h, width=test_w, cover=coverage)

# *********************************************************

# def prime_checker(num):
#     if num <= 1:
#         print(f"'{num}' is not a prime number")
#         return
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             print(f"'{num}' is not a prime number")
#             return
#     print(f"Your number {num} is a prime number!")

# n = int(input("Enter a number to see if it's a prime number: "))
# prime_checker(num=n)

# **************Caesar Cipher***********************
# from art import logo


# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encrypt (user_text, shift_amount):
#     cipher_text = ""
#     for letter in user_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")


# def decrypt (cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#     print(f"Your text in decrypted version is: {plain_text}")

# if direction == "encode":
#     encrypt(user_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)

# def caesar(start_text, shift_amount, cipher_direction):
#     end_text = ""
#     if cipher_direction == "decode":
#         shift_amount *= -1
#     for char in start_text:
#         if char in alphabet:
#             position = alphabet.index(char)
#             new_position = position + shift_amount
#             end_text += alphabet[new_position]
#         else:
#             end_text += char
#     print(f"Here's the {cipher_direction}d result: {end_text}")

# print(logo)

# should_end = False
# while not should_end:

#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))

#     shift = shift % 26

#     caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

#     restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
#     if restart == "no":
#         should_end = True
#         print("Goodbye")

# ************************************************************
# ************************************************************

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }

# for student in student_scores:
#     if student_scores[student] >= 91:
#         print(f" {student} 'Outstanding'")
#     elif student_scores[student] >= 81 and student_scores[student] <= 90:
#         print(f"{student} 'Exceeds Expectations'")
#     elif student_scores[student] >= 71 and student_scores[student] <= 80:
#         print(f"{student} 'Acceptable'")
#     elif student_scores[student] <= 70:
#         print(f"{student} 'Fail'")

# ************************************************

# travel_log = {
#     "Turkey": {"cities": ["Istanbul", "Alanya", "Antalya"], "Visit_time": 4},
#     "German": {"visited_cities": ["Berlin", "Hamm", "Dortmund"], "v_times": 2}
# }

# for city in travel_log:
#     print(city[1])

# country = input("What's the country that you visited?: ")
# visits = int(input("How many times you visited?: ")) 
# cities_input = input("Which cities you visited?: ")
# list_of_cities = eval(cities_input)

# travel_log = [
#   {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
#   },
#   {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
#   },
# ]

# def add_new_country(name, times_visited, cities_visited):
#     new_country = {}
#     new_country["country"] = name
#     new_country["visits"] = times_visited
#     new_country["cities"] = cities_visited
#     travel_log.append(new_country)


# add_new_country(country, visits, list_of_cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favorite city was {travel_log[2]['cities'][0]}.")
# ***************************************************************
# import os


# bids = {}
# bidding_finished = False

# def find_highest_bidder(bid_record):
#       highest_bid = 0
#       winner = ""
#       for bidder in bid_record:
#         bid_amount = bid_record[bidder]
#         if bid_amount > highest_bid:
#               highest_bid = bid_amount
#               winner = bidder
#       print(f"The winner is {winner} with a bid of ${highest_bid}")

# while not bidding_finished:
#   name = input("What is your name?: ")
#   price = int(input ("What is your bid? $"))
#   bids[name] = price
#   should_continue = input("Are there any other bidders? Type 'Yes' or 'No': \n")
#   if should_continue == "no":
#     bidding_finished = True
#     find_highest_bidder(bids)
#   elif should_continue == "yes":
#     os.system('clear')

# ****************************DAYS IN MONTH**********************
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 print("Leap year")
#             else:
#                 print("Not leap year")
#         else:
#             print("Leap year")
#     else:
#         print("Not leap year")
  
# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if month == 2 and is_leap(year):
#         return 29
#     else:
#         return month_days[month - 1]

# year = int(input())
# month = int(input())
# days = days_in_month(year, month)
# print(days)

# *****************CALCULATOR*************************

# def add(n1, n2):
#     return n1 + n2

# def subtract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1*n2

# def divide(n1, n2):
#     return n1 / n2

# operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide
# }

# def calculator():

#     num1 = float(input("What's the first number?: \n"))
#     for symbol in operations:
#         print(symbol)
#     should_continue = True

#     while should_continue:
#         operation_symbol = input("Pick another operation('+', '-', '*', '/'): \n")
#         num2 = float(input("What's the next number?: \n"))
#         calculation_function = operations[operation_symbol]
#         answer = calculation_function(num1, num2)

#         print(f"\n{num1} {operation_symbol} {num2} = {answer}\n")

#         if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
#             num1 = answer
#         else:
#             should_continue = False
#             calculator()
# calculator()

# ********************-BlackJack-***************************
# logo = """
# .------.            _     _            _    _            _    
# |A_  _ |.          | |   | |          | |  (_)          | |   
# |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
# | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
# |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
# `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
#       |  \/ K|                            _/ |                
#       `------'                           |__/           
# """


# import random
# import os

# def deal_card():
#     """Retuning random card from the deck."""
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card

# def calculate_score(cards):
#     """Taking list of cards and returning calculated score"""
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
#     if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)

#     return sum(cards)


# def compare(user_score, computer_score):
#       #Bug fixed. If I and the computer are both over, you lose.
#     if user_score > 21 and computer_score > 21:
#         return "You went over. You lose 😤"

#     if user_score == computer_score:
#         return "Draw 🙃"
#     elif computer_score == 0:
#         return "Lose, opponent has Blackjack 😱"
#     elif user_score == 0:
#         return "Win with a Blackjack 😎"
#     elif user_score > 21:
#         return "You went over. You lose 😭"
#     elif computer_score > 21:
#         return "Opponent went over. You win 😁"
#     elif user_score > computer_score:
#         return "You win!!! 😃"
#     else:
#         return "You lose... 😤"
# def play_game():
#     print(logo)

#     user_cards = []
#     computer_cards = []
#     is_game_over = False

#     for _ in range(2):
#         user_cards.append(deal_card())
#         computer_cards.append(deal_card())

#     while not is_game_over:

#         user_score = calculate_score(user_cards)
#         computer_score = calculate_score(computer_cards)

#         print(f"   Your cards: {user_cards}, current score: {user_score}")
#         print(f"   Computer's first card: {computer_cards[0]}")

#         if user_score == 0 or computer_score == 0 or user_score > 21:
#             is_game_over = True
#         else:
#             user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
#             if user_should_deal == "y":
#                 user_cards.append(deal_card())
#             else:
#                 is_game_over = True

#     while computer_score !=0 and computer_score < 17:
#         computer_cards.append(deal_card())
#         computer_score = calculate_score(computer_cards)

#     print(f"Your final hand: {user_cards}, final score: {user_score}")
#     print(f"\nComputer's final hand: {computer_cards}, final score: {computer_score}")
#     print(compare(user_score, computer_score))

# while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
#     os.system('clear')
#     play_game()


# ************************* SCOPE ***********************************
from random import randint

logo = """

   ___                             ___                     
  / _ \_   _  ___  ___ ___        / _ \__ _ _ __ ___   ___ 
 / /_\/ | | |/ _ \/ __/ __|_____ / /_\/ _` | '_ ` _ \ / _ \
/ /_\\| |_| |  __/\__ \__ \_____/ /_\\ (_| | | | | | |  __/
\____/ \__,_|\___||___/___/     \____/\__,_|_| |_| |_|\___|
                                                           

"""

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
def game():
    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f">>>>>>>>>>>>>>>{answer}")

    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("\nMake a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")
game()