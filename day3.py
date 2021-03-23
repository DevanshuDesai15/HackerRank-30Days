# Objective
# In this challenge, we learn about conditional statements. Check out the Tutorial tab for learning materials and an instructional video.
#
# Task
# Given an integer, n, perform the following conditional actions:
#
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 10, print Weird
# If n is even and greater than 20, print Not Weird
# Complete the stub code provided in your editor to print whether or not  is weird.
#
# Input Format
#
# A single line containing a positive integer, .
#
# Constraints
# 1<=n<=100
# Output Format
# Print Weird if the number is weird; otherwise, print Not Weird.
#
# Sample Input 0
# 3
# Sample Output 0
# Weird
# Sample Input 1
# 24
# Sample Output 1
# Not Weird
#
# Explanation
# Sample Case 0: n=3
# n is odd and odd numbers are weird, so we print Weird.
#
# Sample Case 1:n=24
# n>20 and n is even, so it is not weird. Thus, we print Not Weird.

#Code

!/bin/python3

import math
import os
import random
import re
import sys
#Code by Devanshu Desai
#So here the use of if and if-else is used to get the desired Output
if __name__ == '__main__':
    N = int(input())
    if (N%2)!=0:
        print("Weird")
    elif N in range(2,5):
        print("Not Weird")
    elif N in range(6,21):
        print("Weird")
    else:
        print("Not Weird")
