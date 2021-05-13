#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: May 2021
# This program squares integers from 0 to the user's input and use a for loop


def main():
    # This function squares the numbers
    loop_counter = 0

    # Input
    print("This program calculates the squares from 0 to the "
          "integer you enter.")
    number_as_string = input("Enter a positive integer: ")
    print("")

    # Process & Output
    try:
        number_as_integer = int(number_as_string)

        if number_as_integer >= 0:
            for loop_counter in range(number_as_integer + 1):
                answer = loop_counter ** 2
                print("{0}² = {1}".format(loop_counter, answer))
        else:
            print("{} is not a positive integer.".format(number_as_integer))
    except Exception:
        print("{} is not a valid input.".format(number_as_string))
    print("\nDone.")


if __name__ == "__main__":
    main()
