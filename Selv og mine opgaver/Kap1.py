name = 'Lillemor'
password = 'Tøsen'
print('Hvad er dit navn?')
myName = input()
if name == 'Lillemor':
    print('Hej Anne')
    myPassword = input()
    print('Hvilken er din adgangskode?')
    if password == 'Tøsen':
        print ('forkert.')
    else:
        print ('forkert adgangskode')