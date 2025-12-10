import random

lowerlimit = int(input("Enter the lower bound: "))
upperlimit = int(input("Enter the upper bound: "))

randomint = random.randint(lowerlimit, upperlimit)

print(randomint)