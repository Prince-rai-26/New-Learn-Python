# Loops are used to repeat instruction 

i=1
while i<=6:
    print("i will become a succesfull engineer " , i)
    i = i+1                                           # yaha pr i++ invalid syntax hota h 
print("loop ended")

#Q . Print the elements of the following list using a loop:
numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

i= 0 
while i<len(numbers):
    print(numbers[i])
    i=i+1

# Search for a number x in this tuple using loop:
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81,100 )

x= 36
i=0
while i<len(nums):
    if(x== nums[i]):
        print("x found at index",i)
    else:
        print("finding x ")
    i=i+1                        # ye i = i+1 else ke just niche hi likhna , kyunki khai aur likhne se pura output infinitely 
                                           # run krne lagta h  , as pyhthon depends on iteration 

# BREAK AND CONTINUE 

# Break : used to terminate the loop when encountered.

# Continue : it SKIP the specific thing , and it terminates execution in the current iteration & continues execution of the loop with the next iteration.

print()

#Break
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81,100 )

x= 36
i=0
while i<len(nums):
    if(x== nums[i]):
        print("x found at index",i)
        break
    else:
        print("finding x ")
    i=i+1 

#continue
i=1
while i<=10:
    if(i%2==0):
        i=i+1
        continue   #SKIP the even part and print only the odd number from 1 to 10 
    print(i)
    i=i+1
