#1st
def num(n):
    if n != 0:
        return n + num(n-1)
    else:
        return 0
add = num(10)
print("Additon of first 10 natural number is", add)
additon = num
print("New function value is: ", additon(10))
#2nd
def maximum(a):
    largest = 0
    for i in range(len(a)):
        if largest>a[i]:
            largest = largest
        else:
            largest = a[i]
    return largest
nu = [1,2,3,4,5,6,12,8,9,10]
print("Largest number in given list is: ",maximum(nu))
#3rd
def fun(*arg):
    for i in arg:
        print(i)
fun(10,20,30,'Himanshu','Jadon','Jayden')
#4th
def addsub(x,y):
    additon = x + y
    substraction = x - y
    return additon, substraction
print("Additon and substraction of 10 and 5 are: ",addsub(10,5))