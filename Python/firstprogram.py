# This program says hello and asks for my name.
print('Hello world!.')
print('What is your name?')# ask for their name
myName = input() 
print('It is good to meet you, ' +myName) 
print('The length of your name is:')
print(len(myName))

from datetime import datetime

datetime.now()
print('What is you birthday in numbers?')
myBirthday = input()

difference = (myBirthday - datetime)

print(str(difference) + " days until your birthday")
print(str(difference.total_seconds()/60) + " minutes until your birthday")
print(str(difference.total_seconds()) + " seconds until your birthday")

print('Which country do you live in?') #ask for which country they live in
myCountry = input()
print(myCountry+' is a beautiful country')
print('Which city do you live in?') #ask which country they live 
myCity = input()
print(myCity+ ' is a nice city')
