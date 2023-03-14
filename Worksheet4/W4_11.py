number1 = float(input("enter the first number"))
oprater = input("enter oprater")
number2 = float(input("enter the second number"))

def sum():
    print("the sum of your numbers is ", number1 + number2)

def diffrence():
    print("the diffrence of your numbers is ", number1-number2)

def product():
    print("the product of your number is ", number2*number1)

def quotient():
    if number2 == 0:
        print("cant be computed, denominater = 0")
    else:
        print("the quotient of your number is ", number1/number2)
if oprater == "+":
    sum()
elif oprater == "/":
    quotient()
elif oprater == "*":
    product()
elif oprater == "-":
    diffrence()