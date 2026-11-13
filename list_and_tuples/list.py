#LIST
# A built-in data type that stores set of values
# It can store elements of different types (integer, float, string, etc.)

list=[0, 1.2, 5, 7 , 8.6]

student = ["prince", 19, "bgp"]

print(type(list))
print(student)
print(student[2])  #index wala chij yaha v allowed h 
print(len(student))

#LIST SLICING
# list_name[ starting_idx : ending_idx ] #ending idx is not included
marks=[85, 75, 96, 50, 78 ]
print(marks[1:4])            #it will print 75,96,50 and 78 will not print bcuz ending index is not allowed 
print(marks[ : 4 ] )         # is same as marks[ 0 : 4]
print(marks[1:])              #is same as marks[ 1 : len(marks)]
print(marks[:])   #20 and 21 are both same , its just the way of writing in this case 
print(marks)
#NEGATIVE INDEXING IS ALSO HERE     
print(marks[-3:-1])

#LIST METHOD
list = [90, 78, 56 , 102]
print(list.append(4))    #it will return none in the output but it has added number 4 in the list 

list.append(8)     #adds one element at the end 
print(list)

list.sort()        #sort in ascending order 
print(list)

list.sort(reverse=True)     #sort in desending order 
print(list)

list.reverse()         #it reverse just the list 
print(list)

list=[5,8,2,78,90,65]
list.insert(4,25)     #insert element at particular index
print(list)

list=[2,1,3,1]
list.remove(1)       #remove first occurence of element
print(list)

list.pop(2)       #remove element from particular index 
print(list)





