nums = [1,2,3,4,5,6]

for val in nums:
    print(val)

veggies = ["potato" , "ladyfinger" , "onion" , "cauliflower",]
for ingrediets in veggies:
    print(ingrediets)

stri = "apnacollege"
for char in stri:
    print(char)

for char in stri:
    if(char == "o"):
        print("o found ")
        break 
    print(char)
else:                       # else used as it doesnt execute when break is used    
    print("end'")

# RANGE()  -> range function returns a sequence of numbers , starting from 0 by default , and increment by 1 (by default), and 
            # stop before a specified number .

# range(start , stop , step)

for el in range(5):              # range(stop)   print ye ending number se pehle tk krta h 
    print(el)

for el in range(2,10):           # range(start , stop)
   print(el)

for el in range(2,10,2):           # range(start , stop, increment)
   print(el)

# Q. print the multiplication table of number n , lets take input n = 5
n=5
for i in range(1,11):
    print(n*i)

# PASS -> pass is a null statement that does nothing . it is used as placeholder for future code .
for el in range(5):
    pass

print("heheehehe")

# WAP to find the sum of first n numbers. (using while and for) , lets take n =5
n= 5
sum = 0
i=1
while i<=n:
    sum = sum +i
    i=i+1
print(sum)

n= 5
sum = 0
i=1
for i in range(1,n+1):
    sum = sum+i
    i=i+1         #isko nhi v likhega toh automatically for loop me increment ho jata h by +1
print(sum)