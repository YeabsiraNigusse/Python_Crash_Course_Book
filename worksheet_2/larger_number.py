print("enter the frst number ")
number_one = int(input())
print("enter the second number")
number_two = int(input())
if number_one > number_two:
    print(f"{number_one} is greater than {number_two}")
elif number_one < number_two:
    print(f"{number_two} is greater than {number_one}")
else:
    print("the numbers you enter are equal")