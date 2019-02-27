#!/usr/bin/env python

import time
import math

def print_number_structure(number):
    digits = int(math.log10(number)) + 1  
    print("Number:", number)
    print("Digits:", digits)
    complexity = number**0.5 * math.log(number)
    print("Complexity:", complexity)
     
def get_prime_factors(number):
    multipliers = []
    divisor = 2
    while divisor**2 <= number:
        while (number % divisor) == 0:
            multipliers.append(divisor)
            number //= divisor
        divisor += 1
    if number > 1:
       multipliers.append(number)
    return multipliers

def main():

    """
    -------------------------------------------------------
    Digits:   Number:               Prime factors:
    -------------------------------------------------------
    12,       456602595409,         501701 * 910109
    13,       7789641255881,        1998881 * 3897001
    15,       924380743486033,      10253011 * 90157003
    16,       1881956496924121,     39807011 * 47277011
    18,       157651985594392609,   171775771 * 917777779 
    20,       33458492606927587889, 3371703817 * 9923319017
    """

    numbers = (456602595409, 7789641255881, 924380743486033)
    for number in numbers:
        print_number_structure(number)
        time_start = time.time()
        print("Prime factors:", get_prime_factors(number))
        time_spent = time.time() - time_start
        print("Spent time: %.3f sec." % time_spent)
        print("")

if __name__ == "__main__":
	main()