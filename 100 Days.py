#Day 5: Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the random password generator!")

#Ask user for number of letters, numbers and symbols
num_letters = int(input("How many letters would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like?\n"))
num_symbols = int(input("How many symbols would you like?\n"))

#Empty list to hold password characters
password_list = []

#For loop cycles through each character type and appends a random choice to the password list
for char in range(0, num_letters):
    password_list.append(random.choice(letters))

for char in range(0, num_numbers):
    password_list.append(random.choice(numbers))

for char in range(0, num_symbols):
    password_list.append(random.choice(symbols))

#Empty string to hold final password
password = ""

#Shuffle the password list to ensure randomness and then concatenate each character to form the final password
random.shuffle(password_list)
for char in password_list:
    password += char

print(f"Your password is: {password}")
