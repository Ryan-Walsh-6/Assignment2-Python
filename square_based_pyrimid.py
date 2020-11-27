#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: November 2020
# this program calculates the volume of a square based pyramid


def main():
    # this program calculates the volume of a square based pyramid

    # input
    base_edge = int(input("Enter the base edge of square based pyramid:"))
    height = int(input("Enter the height of square based pyramid:"))

    # process
    volume = base_edge**2 * (height * 1/3)

    # output
    print()
    print("The volume is: {:,.2f}cm3".format(volume))


if __name__ == "__main__":
    main()
