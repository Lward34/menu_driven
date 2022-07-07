"""The function prompts the user for input if they select
   a mathematical performance or generate a secure password.
   Otherwise, if the user selects category 3,
   there would be no input other than the menu selection.

    Args:None
    Returns:None
 """

from datetime import date
import random
import math

i = 0
while i != 6:
    # menu options offered for the user
    print("*********************************************")
    print("Welcome to the lab Math and Secret Generation")
    print("What would you like to do today?")
    print("1: Generate Secure Password")
    print("2: Calculate and Format Percentage")
    print("3: How many Days from Today until July 4, 2025")
    print("4: Use the law of Cosine to calculate the leg of a triangle")
    print("5: Calculate the Volume of a Right Circular Cylinder")
    print("6: ""'EXIT' this program""")
    print("********************************************")
# prompt the user and get the selected choice
    category = int(input("Enter the selected option: "))
# check and gets selected category
    if category == 1:
# prompts the user and gets Generated password
        length = int(input("Enter the length of the password: "))
        NUMBERS = int(input("To add NUMBERS in the password enter 1 else enter 0:  "))
        upper_case = int(input("To add UPPER case letters in the password enter 1 else enter 0:  "))
        lower_case = int(input("To add LOWER case letters in the password enter 1 else enter 0:  "))
        characters = int(input("To add SPECIAL CHARACTERS in the password enter 1 else enter 0:  "))
        PASSWORD = ""
        Dict = []
# gets random numbers
        if NUMBERS == 1:
            NUMBERS = chr(random.randint(48, 57))
            PASSWORD = PASSWORD + NUMBERS
            length -= 1
# check and handle answer
            if length < 0:
                print("invalid inputs")
                print("Please re-enter the information")
                continue
        Dict.append([48, 57])
# gets random Upper Cases
        if upper_case == 1:
            upper_case = chr(random.randint(65, 90))
            PASSWORD = PASSWORD + upper_case
            length -= 1
            if length < 0:
                print("invalid inputs")
                print("Please re-enter information")
                continue
        Dict.append([65, 90])
# gets random lower cases
        if lower_case == 1:
            lower = chr(random.randint(97, 122))
            PASSWORD = PASSWORD + lower
            length -= 1
            if length < 0:
                print("invalid inputs")
                print("Please re-enter information")
                continue
        Dict.append([97, 122])
# gets random special characters
        if characters == 1:
            characters = chr(random.randint(33, 46))
            PASSWORD = PASSWORD + characters
            length -= 1
            if length < 0:
                print("invalid inputs")
                print("Please re-enter information")
                continue
        Dict.append([33, 46])
        for i in range(length):
            R = random.randint(0, len(Dict) - 1)
            PASSWORD = PASSWORD + chr(random.randint(Dict[R][0], Dict[R][-1]))
        PASSWORD = ''.join(random.sample(PASSWORD, len(PASSWORD)))
        print(f"The new Secure Password: ", PASSWORD)
        print()
# prompts the user to calculate and gets percentage format
    elif category == 2:
        NUMERATOR = float(input("Enter the Numerator: "))
        denominator = float(input("Enter the Denominator: "))
        decimal = int(input("The number of decimal points for formatting: "))
        TOTAL = NUMERATOR / denominator * 100
        TOTAL = round(TOTAL, decimal)
        print(f"Percentage: ", TOTAL)
        print()
# prompts the user and gets selected choice 
    elif category == 3:
        START = date.today()
        END = date(2025, 7, 4)
        count = END - START
        print(f"From today until July 4, 2025, there are: {count.days} days.")
        print()
# prompts the user and gets selected choice
    elif category == 4:
        A = int(input("Enter the length of side A: "))
        B = int(input("Enter the length of side B: "))
        ANGLE = int(input("Enter the Angle: "))
        C = A * A + B * B - 2 * A * B * math.cos(math.pi / 180 * ANGLE)
        square_root = math.sqrt(C)
        print(f"The leg of the triangle: ", square_root)
        print()
# prompts the user and gets selected choice
    elif category == 5:
        radius = int(input("Enter the Circular radius: "))
        HEIGHT = int(input("Enter the Cylinder Height: "))
        VOL = radius * radius * HEIGHT * math.pi
        print(f"The Cylinder Volume: ",VOL)
        print()
# check and handle the answer
    elif category == 6:
        print("Thank you for visiting this Application!!!")
        print("Good Bye")
        break
# check and handle the answer
    else:
        print("Ops! Invalid option")
        print("Options are from 1-6")
        continue
