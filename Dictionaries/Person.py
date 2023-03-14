meaza = {
    'First_Name': 'Meaza', 
    'Last_Name': 'Nigusse', 
    'city':'Dukem',
    'age':23,
    'Favorite_Place': ['Dukem','Gimma','Adama']
     }
    
# print(meaza.get('First_Name'))
# print(meaza.get('Last_Name'))
# print(meaza.get('age'))
# print(meaza.get('city'))
# print(meaza.get('sex'))
for key, value in meaza.items():
    print(f'{key} -- {value}')
mekides = {
    'First_name': 'Mekides',
    'Last_Name': 'Nigusse',
    'city':'Dukem',
    'age':25,
    'Favorite_Place': ['Adama', 'Debrezeyt', 'Asela']
    }
Yeabsira = {
    'First_Name':'Yeabsira',
    'Last_Name':'Nigusse',
    'city':'Dukem',
    'age':21,
    'Favorite_Place':['Shashemane','Addis Ababa','Dukem']
}
Bereket = {
    'First_Name': 'Bereket',
    'Last_Name':'Nigusse',
    'city': 'Dukem',
    'age':16,
    'Favorite_Place':['Dukem','Ardayita','Addis Ababa']
}
myFamily = [meaza,mekides,Yeabsira,Bereket]
for family in myFamily:
    print(family)