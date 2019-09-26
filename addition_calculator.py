#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: September 2019
# This program adds two numbers


def main():
    # this function calculates the addition of 2 numbers

    # input
    num1 = int(input("Input the value of the first number: "))
    num2 = int(input("Input the value of the second number: "))

    # process
    answer = num1+num2

    # output
    print("")
    print("The answer is {}".format(answer))


if __name__ == "__main__":

    main()
