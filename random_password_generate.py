'''

Create a command-line app that generates secure random passwords based on user preferences. The user can specify the password length and
whether to include uppercase letters, numbers, and special characters. This project focuses on randomness, string operations, and user input
validation.

'''

import random
import string
# special characters in string
from string import punctuation
# Numbers
from string import digits

'''
# testing
print(punctuation)
print(digits)
print(''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5)))

'''

def generate_password(length: int, uppercase: str, nums: str, symbols: str):
    text= string.ascii_lowercase

    if uppercase == "yes":
        text+= string.ascii_uppercase
    if nums == "yes":
        text+= string.digits
    if symbols== "yes":
        text+= string.punctuation
    if length >= 6:
        password = ''.join(random.choices(text, k=length))
        return password



def main():
    print("Welcome to the Random Password Generator!")
    length= int(input("Enter desired password length (minimum 6): "))
    if length < 6:
        print("Minimum length of password should be 6")
        return
    else:
        uppercase_letters= input("Include uppercase letters (yes/no): ")
        inc_nums= input("Include numbers? (yes/no): ")
        inc_symbols= input("Include special symbols (yes/no): ")
        password= generate_password(length=length, uppercase= uppercase_letters, nums=inc_nums, symbols=inc_symbols)
        print("Generated password is: ", password)

# Calling main function
main()



