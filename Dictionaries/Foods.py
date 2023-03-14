def foods(*types):
    print('you order the following foods')
    for food in types:
        print(f'-{food}')
foods('doro','shiro','beyayinet', 'atikilt')
print()
foods('alicha-shiro')