name = 'Lillemor'
password = 'Tøsen'
print('Hvad er dit navn?')
myName = input()
if name == 'Lillemor':
    print('Hej Anne')
else: 
    print('Husk denne computer tilhøre Anne, som er lille og passer på alle som en mor.')
    myPassword = input()
    print('Hvilken er din adgangskode?')
    if password == 'Tøsen':
        print ('forkert.')
    else:
        print ('forkert adgangskode')