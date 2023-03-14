Favorite_number = {
    'Nigusse': 7,
    'Tsehay': 10,
    'Mekides': 1,
    'Meaza': 3,
    'Yeabsira':5,
    'Bereket':2 }
# print(Favorite_number.get('Nigusse'))
# print(Favorite_number.get('Tsehay'))
# print(Favorite_number.get('Mekides'))
# print(Favorite_number.get('Meaza'))
# print(Favorite_number.get('Yeabsira'))
# print(Favorite_number.get('Bereket'))
for name , number in Favorite_number.items():
    print(f'favorite number of {name} is {number}')