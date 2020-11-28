#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: November 2020
# this program calculates the volume of a square based pyramid


def main():
    # this program calculates the volume of a square based pyramid

    # input
    print("We will be calculating the volume of a square based pyramid")
    base_edge = int(input("Enter the base edge (cm):"))
    height = int(input("Enter the height of square (cm):"))

    # process
    volume = base_edge**2 * (height * 1/3)

    # output
    print()
    print("The volume is: {:,.2f}cm3".format(volume))


if __name__ == "__main__":
    main()
