# user_number= int(input("enter a number: "))
# # right = False
# def Fizz(number):
#     if user_number % 3 == 0:
#        return True
# def Buzz(number):
#     if user_number % 5 == 0:
#       return True

# if Fizz(user_number) and Buzz(user_number):
#     print("FizzBuzz")
# elif Fizz(user_number):
#     print("Fizz")
# elif Buzz(user_number):
#     print("Buzz")
# else:
#     print(user_number)
def fizzBuzz(n):
 answer = []
 temp = ''
 for i in range(1,n+1):
    if i % 3 == 0:
        temp = 'Fizz'
    if i % 5 == 0:
        temp = 'Buzz'
    if i % 3 == 0 and i % 5 == 0:
        temp = 'FizzBuzz'
    if i % 3 != 0 and i % 5 != 0:
        temp = f'{i}'
    answer. append(temp)
 return answer
num = int(input('enter number '))
print(fizzBuzz(num))
