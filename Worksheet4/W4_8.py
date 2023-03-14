user_number = int(input("enter a posetive number"))
def factorial(number):
    if number == 1:
        return number
    else:
        return number*(number - 1)
given_number = True


def Euler(number):
    sum = 0.0
    for number in range(1,number+1):
     sum += (1 + (1/factorial(number)))
    return sum


while (given_number):
  if user_number <= 0:
    print("invalid number, enter again")
    user_number = int(input("enter a posetive number"))
  else:
    print(Euler(user_number))
    given_number = False
