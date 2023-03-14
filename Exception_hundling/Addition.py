try:
    number1 = int(input('enter a number'))
    number2 = int(input('enter number'))
except ValueError:
    print('invlaid input')
else:
    print(number1+number2)
