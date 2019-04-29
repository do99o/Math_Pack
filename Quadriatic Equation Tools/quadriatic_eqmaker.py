# This program generates a quadratic equation with the parameters you set.

import sys
import time
import math
import random

print("Hello! This program generates a quadratic equation using the parameters you set!")
time.sleep(5)
print("Are you ready? [y/n]")
ready_ans = input()
if ready_ans == "y":
    print("OK!")
else:
    print("OK then. Bye!")
    sys.exit()

print("How many solutions should there be? [0,1,2,]")

while True:
    sol_ans = input()

    if sol_ans == "0":
        # Parameters
        while True:
            print("What is the maximum size for the a, b, and c values? [a.e. 60]")
            int_max = input()
            print("What is the minimum size for the a, b, and c values? [a.e. -45]")
            int_min = input()
            # generate a, b, c values
            a = random.randint(int_min, int_max)
            b = random.randint(int_min, int_max)
            c = random.randint(int_min, int_max)
            neg = i_b ** 2 - 4 * i_a * i_c
            if neg < 0:
                print("Your equation is: " + str(a) + "x² + " + str(b) + "x + " + str(c))
                break
            else:
                print()
    elif sol_ans == "1":
        # IDK
        break
    elif sol_ans == "2":
        # IDK
        break
    else:
        print("That is not a valid answer! Try again.")
print("done.")