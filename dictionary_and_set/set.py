# SET is the collection of unordered item .
# each element in the set must be unique and immutable 
# there is no fixed order in out put , mtlb agar input jis sequence mein likhe ho , zarrori nhi h ussi sequence mein output
                                  #  print hoga 
# set - mutable hota h 
# set ke andar ka elemnt immutable hota h , mtlb wo chij ko change nhi kr sakte 

collection ={1,2,5,2,"heelo",54,"world"}  #agar same chij rahega toh error nhi hoga , bas wo ek hi baar print hoga 
print(collection)
print(len(collection))  #length of unique collection in the set 
print(type(collection))

#creating empty set 
collection = set()     #empty set , syntax
#NOTE - collection = {}   ye empty dictionary hota h 

#SET method 
collection = set()

collection.add(1)    #add an element 
collection.add(2)
collection.add(2)
collection.add(54)
collection.add("apna college ")
collection.add((1,2,3))  #ye tuple ko add kr sakte h , list aur dictionary ko nhi 
#collection.add[1,2,3]

collection.remove(1)    #remove an element from the set 
#collection.remove(7)   #it will give error 

print(collection.pop())    #print any RANDOM value from the set 

print(collection)  
print(len(collection))

#NOTE - unhashbale - list , dictionary , set 

collection.clear()      #empties the set 
print(collection)
print(len(collection)) 

set1 = {1,2,3}
set2= {2,3,4}

print(set1.union(set2))  #this is just a new set , in which union of both store and printed 
print(set1)
print(set2)

print(set1.intersection(set2)) #this is the intersection of both set 

print(set2.union(set1))  # kisi ko pehle ya baad mein likho , baat barabar h 
print(set2.intersection(set1))