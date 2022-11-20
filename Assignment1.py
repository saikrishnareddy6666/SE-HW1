"""
Title: Assignment 1 - Fermat's Last Theorem Near Misses
File: homeWork1.py
External Files: N/A
External Files Created by Program: N/A
Programmers: Venkata Sai Krishna Reddy Sabbasani, Sumanth kurapati
email addresses: venkatasaikrishnareddyr@lewisu.edu, sumanthkurapati@lewisu.edu
Course Number and Section Number: 60500 and 004
Date: 11/19/2022
Explanation: The program checks for near misses given the power of a number and maximum value possible of x and y
References: https://docs.python.org/3/library/math.html
"""

print("""
Title: Assignment 1 - Fermat's Last Theorem Near Misses
File: homeWork1.py
External Files: N/A
External Files Created by Program: N/A
Programmers: Venkata Sai Krishna Reddy Sabbasani, Sumanth kurapati
email addresses: venkatasaikrishnareddyr@lewisu.edu, sumanthkurapati@lewisu.edu
Course Number and Section Number: 60500 and 004
Date: 11/19/2022
Explanation: The program checks for near misses given the power of a number and maximum value possible of x and y
References: https://docs.python.org/3/library/math.html
""")




# Importing required packages
import math

# Taking user input of n with constraints
while True:
    try:
        n = int(input('\n\nEnter value of n: '))
        assert 2 < n < 12
    except AssertionError:
        print("Please enter an integer between 2 and 12")
    except ValueError:
        print("Please enter an integer value for n")
    else:
        break


# Taking user input of k with constraints
while True:
    try:
        k = int(input('Enter value of k: '))
        assert 10 < k
    except AssertionError:
        print("Please enter an integer greater than 10")
    except ValueError:
        print("Please enter an integer value for n")
    else:
        break




# Function to get near misses with given n and k values.
def getNearMisses(n, k):

    # Initiating nearmiss as a large value to use for future smaller near misses
    nearmiss = math.pow(k, n)

    # Looping x values
    for x in range(10, k+1):

        # Looping y values
        for y in range(10, k+1):

            # Calculating x^n + y^n
            power_sum = math.pow(x, n) + math.pow(y, n)

            # Getting closest z value
            z = math.floor(power_sum**(1/n))

            # Getting near miss from z values
            if power_sum - math.pow(z, n) > math.pow(z+1, n) - power_sum:
                z = z + 1

            # Calculating near miss fraction
            miss = abs(math.pow(z, n) - power_sum)
            miss = miss / power_sum

            # Printing each near miss value
            if miss < nearmiss:
                nearmiss = miss
                print(str(x) +"\t"+ str(y) +"\t"+ str(z) +"\t"+ str(int(abs(math.pow(z, n) - power_sum))) +"\t\t"+ str(nearmiss))




# Starting the near miss calculation
print("x\ty\tz\tActual Miss\tRelative Miss")
getNearMisses(n, k)

input("Continue...")