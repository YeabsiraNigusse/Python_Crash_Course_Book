user_number = int(input("enter a posetive number"))
def fib(number):
    if number == 1 or number == 0:
        return 1
    else:
        return (number - 2)*(number - 1)
given_number = True
while (given_number):
  if user_number <= 0:
    print("invalid number, enter again")
    user_number = int(input("enter a posetive number"))
  else:
    print(fib(user_number))
    given_number = False
