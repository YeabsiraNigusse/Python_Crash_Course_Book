user_number = int(input("enter a number: "))
def factorial(number):
    if user_number == 1 or 0:
        return 1
    return (number) * (number - 1)     
print("the factorial of the number is ", factorial(user_number))
