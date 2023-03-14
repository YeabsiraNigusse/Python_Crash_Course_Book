print('enter 10 intger number')
numbers = []
for i in range(10):
    num = int(input('enter number'))
    numbers.append(num)
print(numbers)

max = 0
min = 0
for i in range(10):
    for j in range(10):
        if numbers[i] > numbers[j]:
            temp = numbers[j]
            numbers[j] = numbers[i]
            numbers[i] = temp
             
print(numbers)
print('max number is ', numbers[0])
print('minimum number is ', numbers[9])