file = open('Jayden.txt','r+')
n = input("What is your name?: ")
c = input("What is your current CGPA?: ")
b = input("What is your branch?: ")
u = input("What is your college name: ")
file.write("My name is ")
file.write(n)
file.write("\n My current CGPA is ")
file.write(c)
file.write("\n My branch is ")
file.write(b)
file.write("\n My college name is ")
file.write(u)
file.seek(0)
print(file.read())