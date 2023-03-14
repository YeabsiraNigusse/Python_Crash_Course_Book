guests = ['mekides', 'meaza', 'bereket']
for guest in guests:
    print(f'{guest} could you came to my dinner party')

print(guests[0],"couldn't make it")
del guests[0]
guests.insert(0, 'yeab')
for guest in guests:
    print(f'{guest} could you came to my dinner party')
print('I got additional dinner table')
guests.insert(0, 'Nigusse')
mid = len(guests)//2
guests.insert(mid,'tsehay')
guests.append('ababa')
print()
for guest in guests:
    print(f'{guest.title()} could you came to my dinner party')
print()
for guest in guests:
    if len(guests) > 2:
        current_guest = guests.pop()
        print(f"sorry {current_guest}, i can't invite you to my dinner")
    else:
        print(f'{guest}, you still come to my dinner')
print(guests)
number = [1,3,5,6,8,9,0]
print(number[:-3])