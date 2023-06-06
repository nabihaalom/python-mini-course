# Functions - function, modularity, helper function, scope

# create a function

# call the function

# scope

DIMENSIONS = 2
## constants are UPPERCASE


def computeSquareArea(side):
    return side ** 2


def main():
    x = int(input("Enter the length of a square: "))
    print("The square has Area: ", computeSquareArea(x), "square units")

main()
