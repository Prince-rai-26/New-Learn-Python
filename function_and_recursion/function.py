# function -> block of statement that performs a specified task 

#function definition 
def calc_sum(a,b):   #parameters
    return a+b

sum = calc_sum(4,6)    #function call ,  (argument)
print(sum)

def print_hello():
    print("hello")

print_hello()
print_hello()
print_hello()
#or
output=print_hello()
print(output)            #none , kyunki function kuch v return nhi kr rahi h , but hello will print one more time 

#avg of 3 number 
def calc_avg(a,b,c):
    sum = a+b+c
    ans = sum/3
    print(ans)
    return ans 

calc_avg(5,15,12)

# function is of two types 
# 1. BUILT IN FUNCTION -> e.g. print() , type(), len(), range()
# 2 . USER DEFINED FUNCTION -> jisko hm define krte h code likhthe time 

# DEFAULT PARAMETER -> assigning a default value to parameter , which is used when no argument is passed 
#i.e , def calc_sum(a=5,b=10):   #parameters
   # return a+b

# Let‘s Practice
# WAF to print the length of a list. ( list is the parameter)
# WAF to print the elements of a list in a single line. ( list is the parameter)
# WAF to find the factorial of n. (n is the parameter)
# WAF to convert USD to IN

nums = [83,48,38,29,94,843,84]

def display_list(list):
    print(len(list))

display_list(nums)

def print_len(list):
    for item in list:
        print(item , end=" ")
    
    
print_len(nums)

print()



def calcfact(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    print(fact)
        
n= int(input("enter the number"))
calcfact(5)

def calfac(n):
    i = 1
    fact = 1
    while i<=n:
        fact = fact * i
        i = i+1
    print(fact)
    
n= int(input("enter the no"))
    
calfac(5)

def convert(n):
    usd = 97 
    inr = usd * n
    print(inr)

n = int(input("enter the rs in usd "))
convert(n)