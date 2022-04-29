#!/usr/bin/env python3

# Created by Devin Jhu
# Created on April 2022
# The greatest number finder


def main():
    # this function finds the greatest number

    # input
    number1_string = input("Enter number 1: ")
    number2_string = input("Enter number 2: ")
    number3_string = input("Enter number 3: ")

    # process & output
    try:
        number1 = int(number1_string)
        number2 = int(number2_string)
        number3 = int(number3_string)

        if number1 > number2 and number3:
            print("{} was the greatest number".format(number1))
        elif number2 > number1 and number3:
            print("{} was the greatest number".format(number2))
        elif number3 > number1 and number2:
            print("{} was the greatest number".format(number3))
        else:
            print("All numbers are the same")
    except Exception:
        print("Not a number")
    print("\nDone.")


if __name__ == "__main__":
    main()
