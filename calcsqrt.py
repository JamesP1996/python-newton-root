#! /usr/bin/env python3

# G00327095 James Porter
# Calculate the Square Root of a Number.


def sqrt(x):
    """
    Calculate the Square Root of Argument X
    """
    #Check That X Is Posistive
    if x < 0:
        print("Error: Negative Value Supplied")
    return -1

    #Initial Guess for Square Root.
    z = x / 2.0

    #Continously Improve the Guess.
    #Adapted from https://tour.golang.org/flowcontrol/8
    while abs(x - (z*z)) > 0.00001:
         z = z - (((z * z) - x) / (2 * z))

    return z\


myVal = 63.0
print("The Square Root of",myVal,"is",sqrt(myVal))
