# Dictionaries are used to store data values in key:value pairs
# They are unordered , mutable(changeable) and dont allow duplicate keys 

dict = {
    "name" : "prince",
    "cgpa" : "8.3",
    "marks" : [98,78,80],                                #list
    "subject" : ("maths", "physics", "chemistry"),       #tuples
}
print(dict)
print(list[dict])       #to print dictionary thing in form of list , jis v form mein output nikalne chathe h wo aage likh do 
print(list(dict))       # agar list ya tuple ke baad () ye bracket ke andar dict likhoge , toh sirf key side print hoga , value print nhi hoga i.e print(tuple(dict))
print(tuple[dict])

dict["name"] = "priyanshi"    #to change the value of anything in the dictionary in between 
dict["enroll no "] = 138,     # to add ney key value pairs in the dictionary in between 

print(dict)
print(dict["cgpa"])       #to print specific thing from dictionary 
print(' ')

#NESTED DICTIONARY 
student = {
    "name" : "priyanshi",
    "marks": {
        "chem" : 48,
        "phy" : 57,
        "math" :78,
    }
}
print(student["marks"]["phy"])

#DICTIONARY METHODS 
print(student.keys())  #returns all keys , jo outer layer wala keys wo aayegi output mein , nested wale nhii chem,phy,math
print(list(student.keys()))    #ye list typecast mein print hoga 
print(len(student.keys()))

print(student.values())     #returns all values , isme nested wala ke andar ka v value print hoga 
print(list(student.values()))

print(student.items())     #returns all (key, value) pairs as tuples 
print(list(student.items()))

pairs= list(student.items())
print(pairs[0])

print(student["name"])
print(student.get("name"))

#  print(student["name2"])     #it will give error 
print(student.get("name2"))     #.get method isliye use kr rahe h kyunki , normally agar code galat hoga toh niche wala kuch v print nhi hoga , no matter wo sahi ho 
                                  #pr  .get se none return ho jayega agar galat rahega , aur niche wala v print hoga 

student.update({"city" : "bhagalpur"})    #insert the specified item to the dictionary 
print(student)

new_dict = {"city": "delhi" ,"age": 20}
student.update(new_dict)
print(student)

new_dict = {"name" : "prince"}       #dictionary ke andar duplicate keys allowed nhi hoti h , isliye name update hoke priyanshi se prince ho gaya 
student.update(new_dict)
print(student)
