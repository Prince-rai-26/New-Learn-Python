# RECURSION -> when a function call itself repeatedly . 
# jo kaam recusion se ho sakta h wo loop se v ho sakta h and vice versa . 

# print number from n to 0 
def show(n):
    if(n==0):                    # BASE CASE 
        return
    print(n, end=" ")
    show(n-1)                   # SELF CALLING FUNCTION that is what recursion is .

#n = int(input("enter the number "))
show(5)
print()
# factorial of number n using recursion 
def fact(n):
    if(n==0) or (n==1):
        return 1
    else:
        return (fact(n-1) * n)

print(fact(5))
Hello = "Hello"
print(Hello, end=" ")
print("world!")

# write a recursive function to calculate the sum of first n natural numbers.
# write a recursive function to print all elements in a list.(Hint : use list & index as paramet)

def calc_sum(n):
    if(n==0):         # In recursion -> base case is very important , otherwise it will run infinite times and code will burst 
        return 0
    sum = calc_sum(n-1)+n
    return sum 
    calc_sum(n-1)

print(calc_sum(5))

city = ["bhagalpur", "delhi", "dwarka", "gurugram", "mirzachowki", "narkatia"]

def print_list(lis, idx=0):
    if(idx==len(lis)):
        return 
    print(lis[idx], end= " ")
    print_list(lis,idx+1)

print_list(city)
