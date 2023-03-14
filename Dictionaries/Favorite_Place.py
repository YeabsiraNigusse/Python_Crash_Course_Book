Favorite_place = {
    'mekdes':{
        'first':'Adama,', 
        'second':'Debrezeyt,', 
        'third':'Asela'
    },
    'meaze':{
        'first':'Dukem,',
        'second':'Gimma,',
        'third':'Adama'
    },
    'yeabsira':{
        'first':'Shashemane,',
        'second':'Addis Ababa,',
        'third':'Dukem'
    },
    'bereket':{
        'first':'Dukem,',
        'second':'Ardayita,',
        'third':'Addis Ababa'
    }
}
for name , place in Favorite_place.items():
    print(f'favorite place of {name} is ')
    one  = f"{place['first']} {place['second']} {place['third']}"
    print(f'{one}\n')