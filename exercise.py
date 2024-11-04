# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
# print_greeting()


# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
    letter = input('Vowel or Consonant (a-z or A-Z): ')
    if letter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        print(f'Letter {letter} is a vowel!')
    elif not letter.isalpha():
        print('Enter a letter next time')
    else:
        print(f'Letter {letter} is a consonant!')

# Call the function
# check_letter()


# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
    age = int(input('Please enter your age: '))
    if age > 0 and age >= 18:
        print('You are eligible')
    elif age < 0:
        print('Please input a valid age')
    else:
        print('You are not eligible')
    

# Call the function
# check_voting_eligibility()


# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    human_years = int(input('Input a dog\'s age: '))
    if human_years < 0:
        print('Please provide a valid age')
        exit()
    elif human_years <= 2:
        dog_years = human_years * 10
    else:
        dog_years = 6 + (human_years * 7)
    
    print(f'The dog\'s age in dog years is {dog_years}')


# Call the function
# calculate_dog_years()


# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    # Your control flow logic goes here
    temp = input('Is it cold? (y/n): ').lower()
    weather = input('Is it raining? (y/n): ').lower()
    if temp == 'y' and weather == 'y':
        print('Wear a waterproof!')
    elif temp == 'y' and weather == 'n':
        print('Wear a warm coat!')
    elif temp == 'n' and weather == 'y':
        print('Carry an umbrella!')
    elif temp == 'n' and weather == 'n':
        print('Wear light clothing!')
    else:
        print('Please just y or n next time')

# Call the function
# weather_advice()


# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # Your control flow logic goes here
    month = input('Enter the month of the year (Jan - Dec): ')
    date = int(input('Enter the date of the month (1 - 31): '))
    try:
    # if month in ['Dec', 'Jan', 'Feb', 'Mar'] and (date > 18):
    #     print(f'{month} {date} is in Winter!')
    # elif month in ['Mar', 'Apr', 'May', 'Jun'] and (date > 19):
    #     print(f'{month} {date} is in Spring!')
    # elif month in ['Jun', 'Jul', 'Aug', 'Sep'] and (date > 20):
    #     print(f'{month} {date} is in Summer!')
    # elif month in ['Sep', 'Oct', 'Nov', 'Dec'] and (date > 19):
    #     print(f'{month} {date} is in Autumn!')
    # else:
    #     print('Invalid month or date.  Example: May 24')
    
        if month in ('Dec', 'Jan', 'Feb') and date <= 31:
            season = 'winter'
        elif month in ('Mar', 'Apr', 'May') and date <= 31:
            season = 'spring'
        elif month in ('Jun', 'Jul', 'Aug') and date <= 31:
            season = 'summer'
        elif month in ('Sep', 'Oct', 'Nov') and date <= 31:
            season = 'autumn'
    # else:
    #     print('Invalid month.  Example: May 24')
    #     exit()

        if month == 'Mar' and date <= 19:
            season = 'winter'
        elif month == 'Jun' and date <= 20:
            season = 'spring'
        elif month == 'Sep' and date <= 21:
            season = 'summer'
        elif month == 'Dec' and date <= 20:
            season = 'autumn'
    # else:
    #     print('Invalid date.  Example: May 24')
    #     exit()

    # season = 'winter' if month == 'Dec' and date >= 21 else 'autumn'
    # season = 'spring' if month == 'Mar' and date >= 20 else 'winter'
    # season = 'summer' if month == 'Jun' and date >= 21 else 'spring'
    # season = 'autumn' if month == 'Sep' and date >= 22 else 'summer'

        print(f'{month} {date} is in {season}!')
    except:
        print('Invalid month and/or date. Example: May 24')
# Call the function
determine_season()
