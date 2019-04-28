# This program does the quadriatic formula for you AND finds the Axis of Symmetry (AOS) and Vertex

import sys
import time
import math

print("Hello!")
time.sleep(1)
print("This is a quadriatic equation solver!")
print("We just need a little information about the equation!")
time.sleep(2)
print("Are you ready? [y/n]")
ready_ans = input()

if ready_ans == "y":
    print("ok!")
else:
    print("oh well, bye!")
    sys.exit()

print("What is the a value? (ax² + bx + c)")
a = input()
time.sleep(2)
print("What is the b value? (ax² + bx + c)")
b = input()
time.sleep(2)
print("What is the c value? (ax² + bx + c)")
c = input()
time.sleep(2)
print("ok")

i_a = int(a)
i_b = int(b)
i_c = int(c)

# Solve the equation using the quadriatic formula

# Check if the number being square rooted is negative
neg = i_b**2 - 4 * i_a * i_c

if neg < 0:
    print("There are no solutions")
else:
    ans1 = ((i_b * -1) + math.sqrt(i_b**2 - 4 * i_a * i_c)) / (2 * i_a)
    ans2 = ((i_b * -1) - math.sqrt(i_b**2 - 4 * i_a * i_c)) / (2 * i_a)

    print( "The solutions are: {" + str(ans1) + ", " + str(ans2) + "}" )

# Find the AOS

AOS = -1 * (i_b / (2 * i_a) )

print( "AOS: " + str(AOS) )

# Find the vertex

vert = (i_a * AOS**2) + (i_b * AOS) + i_c

print( "Vertex: " + str(vert) )

print("done.")

time.sleep(100)