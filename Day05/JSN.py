import json


file = open('Jayden.txt','w+')
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
dict = {'name': name, 'age': age, 'city': city}
json.dump(dict,file)
file.seek(0)
print(file.read())