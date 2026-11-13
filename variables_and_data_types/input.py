# we take input normally in python in string .
# then we use type casting to convert from one keyboard to another keyboard
# just before taking input we write the data types in which we want to take input 
# string input ke case mein we dont write str before input kyunki wo automatically python mein input string mein hi leta h 

name = input("enter your name - ")
age = int(input("enter your age"))
price = float(input("enter your price"))

print(type(name), name)
print(type(age),age)
print(type(price),price,)

print(type(age+price), age+price)

a= input()
b= input()

print (a+b)