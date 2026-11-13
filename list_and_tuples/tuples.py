#TUPLES -> a built in data types that lets us to create a IMMUTABLE SEQUENCE of values .

# tuples mein list ke square bracket ke jagah () bracket use kro 

tup = (87,64,58,96,25)

#tup[0]=43   not allowed in tuples

tup1=() #it is non empty tuples
tup2=(5,)  # comma lagana jaruri hai jb 1 integer ya string ho kyunki warna compiler usse tuples ke tarah nhi lega , 
                                                #usko ya toh single integer ya single string ke taha lene lagega 

tup3= (1,2,3,1)

print(tup3.index(2)) #return index of first occurence

print(tup3.count(1)) #count total occurence of the search number 

# Q-> WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)

list = [1,2,3,2,5]

copy_list = list.copy()
print(list)

copy_list.reverse()
print(copy_list)

if(list==copy_list):
    print("PALINDROME")
else:
    print("NOT PALINDROME")