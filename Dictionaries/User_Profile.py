def user_profile(first,last,**user_info):
    user_info['first_Name'] = first
    user_info['last_name'] = last
    return user_info

print(user_profile('Yeabsira', 'Nigusse',age = 21, nationality = 'Ethiopian',lives_in = 'Dukem'))