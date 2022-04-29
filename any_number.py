#!/usr/bin/env python3

# Created by Devin Jhu
# Created on April 2022
# The area and perimeter calculator


def main():
    # this shows if its a square or not
    # input
    width = int(input("Enter width: "))
    height = int(input("Enter height: "))

    # process
    if width == height:
        print("it is a square")
    else:
        print("it is a rectangle")

    print("\nDone.")


if __name__ == "__main__":
    main()
