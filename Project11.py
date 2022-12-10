# Here I have imported two library called as Random
import random

while True:
    a = int(input("a: "))
    b = int(input("b: "))

    c = random.randint(a, b)

    # Here we are checking that the number is Even or Odd
    if c % 2 == 0:
        print("{} is an Even Number".format(c))
    else:
        print("{} is an Odd Number".format(c))

    # Here we are checking if the number is Positive or Negative
    if c > 0:
        print("{} is a Positive Number".format(c))
    else:
        print("{} is a Negative Number".format(c))

    # Here we are checking if the Number Prime Number or Composite Number
    if c > 1:
        for i in range(2, c):
            if (c % i) == 0:
                print("{} is a Composite Number". format(c))
                break
        else:
            print("{} is a Prime Number".format(c))

