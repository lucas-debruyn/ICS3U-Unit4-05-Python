#!/usr/bin/env python3

# Created by: Lucas DeBruyn
# Created on: Oct 2021
# This is the loop addition program


def main():
    # This is the loop addition function

    counter = 0
    total = 0

    # Input, Process and Output
    times_added_s = input("How many positive numbers would you like to add: ")
    print("")
    try:
        times_added = int(times_added_s)
        for counter in range(times_added):
            user_s = input("Enter a positive integer to add: ")
            print("")
            positive_integer = int(user_s)
            if positive_integer < 0:
                continue
            elif positive_integer > 0:
                total = total + positive_integer
                continue
            else:
                break
        if positive_integer > 0 or positive_integer < 0:
            print("Sum of all positive integers is {0}.".format(total))
        else:
            print("Do not add the number 0.")
    except Exception:
        print("Invalid input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
