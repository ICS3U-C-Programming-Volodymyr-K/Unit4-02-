#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 04, 15, 2025
# This program  calculates factorial.


def main():
    # Declares counter and factorial variable
    looprun = 0
    factorial = 1
    # Gets input number for loops from user
    number = input("Enter the number by how much you want to know your factorial.")
    # Catches any other input besides integer
    try:
        number = int(number)
        # Catches if number is negative
        if number < 0:
            print("Enter positive number.")
            # Calculates the factorial with the use of loop
        while True:
            factorial = factorial * looprun
            looprun = 1 + looprun
            # Displays factorial and on what loop it finished
            print(f"Your factorial during the {looprun} is {factorial}")
            if looprun <= number:
                break
            # Displays this statement when number is not an integer
    except Exception:
        print("Enter integer.")


if __name__ == "__main__":
    main()
