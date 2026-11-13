word1 = "hello"
word2= "prince"
print(word1+" "+word2) # CONCATENATION (when word is being added )

str= "kya haal ho"
print(len(str)) #space v count hota h 

print(str[2]) # it will print "a" as index 2 has a
print(str[3]) # it will print a blank space
# we cannot manually change the value of any index means kisi word ke index ko change nhi kr sakte h ..
#  for e.g. str 2 ka value a h usko p nhi kr sakte manually 

#SLICING
print(str[1:4]) # it means it willprint from index 1 to index 3 i.e jo v last index likha hoga usse ek kam tk print karega 
print(str[4:]) # agar last index nhi likho ho toh automatically last index tk print ho hjayega mtlb len(str) se 1 km tk print ho jayega 
print(str[:len(str)]) # it will print from starting index to last index
print(str[:6])
#slicing with negative index 
print(str[-6:-1]) # isme -1 wala count similar;y nhi hoga means usse -2 tk print ho jayega 

#STRING FUNCTION 
str = "i am a coder"

print(str.endswith("er")) #returns true if string ends with substr

print(str.capitalize()) #capitalize only 1st char

print(str.replace("am","was"))
print(str.replace("a","h")) #replaces all occurrences of old with new

print(str.find("a")) #returns only 1st index of 1st occurrence
print(str.find("i"))
print(str.find("I"))
print(str.find("coder"))

print(str.count("a")) #counts the occurrence of substr in string
print(str.count("am"))