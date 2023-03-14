Favorite_numbers = {
    'Nigusse': ['7','9','13'],
    'Tsehay': ['10'],
    'Mekides': ['1','3','5'],
    'Meaza': ['3','5','7'],
    'Yeabsira':['5','7','9'],
    'Bereket':['2','4','6']
    }
for name, numbers in Favorite_numbers.items():
    if len(numbers) > 1:
        print(f'favorite numbers of {name} are ')
        for number in numbers:
            print(number, end = " ")
        print()
    else:
        print(f'favorite number of {name} is {numbers}')