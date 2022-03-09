#!/usr/bin/env python3
# Created by: Sarah
# Created on: Mar 8, 2022
# This program asks the user for the radius of
# a circle in cm. It then calculates and displays
# the circumference using tau.
import constants


def main():
    # get the radius from the user
    radius = float(input("Enter the radius of the circle (cm): "))

    # calculate the circumference
    circumference = constants.TAU * radius

    # display the circumference
    print("")
    print("Circumference = {} cm".format(circumference))


if __name__ == "__main__":
    main()
