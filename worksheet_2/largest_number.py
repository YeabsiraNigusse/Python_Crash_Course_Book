print("enter the first number")
number1 = int(input())
print("enter the second number")
number2 = int(input())
print("enter the third number")
number3 = int(input())
if number1 > number2 and number2 > number3:
    print(f"{number1} {number2} {number3}")
elif number1 > number2 and number3 > number2:
    print(f"{number1} {number3} {number2}")
elif number2 > number3 and number3 > number1:
    print(f"{number2} {number3} {number1}")
elif number2 > number3 and number1 > number3:
    print(f"{number2} {number1} {number3}")
elif number3 > number2 and number2 > number1:
    print(f"{number3} {number2} {number1}")
elif number3 > number2 and number1 > number2:
    print(f"{number2} {number3} {number1}")
