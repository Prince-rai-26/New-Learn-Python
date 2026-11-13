"""
if(condition):
    print()   #we have to leave 4 tab spaces -  isko IDENTATION Bolte h 
elif(condition):
    print() #we have to again leave 4 tab space
else:
    print() 

    #in this , koi agar ek condition true hogi toh baki statement execute nhi hoga ... ,

# agar if ke saath if hi ho , elif na ho toh multiple statement true hone pr dono statement execute hoga 
    """
num = 5
if(num>2):
   print("number greater then 2")
if(num>3):
   print("number greater than 3")
else:
   print("number bada h 5 se ")

print(" ")

numb=5
if(num>2):  #isme jaise hi koi ek condition true hoga , bas wahi statement execute hoga 
   print("number greater then 2")
elif(num>3):
   print("number greater than 3")
else:
   print("number bada h 5 se ")

#Grade students based on marks
marks = 85
if(marks>=90):
   grade="a"
elif(marks>=80 and marks<90):
   grade = "b"
elif(marks>=70 and marks<80):
   grade="c"
else:
   garde="d"
print("grade of the student is :-",grade)

#NESTING
age = 80
if(age>18):
   if(age>=80):
      print("cannot drive")
   else:
       print("can drive")
else:
   print("cannot drive")




