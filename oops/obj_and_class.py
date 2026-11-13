# To map with real world scenarios, we started using objects in code.
# This is called object oriented programing

# CLASS IS A BLUEPRINT OF CREATING OBJECT 

class Student:                     #generally class variable ke naam capital letter se hi suru krte h 
    name = "prince"
    gender = "male"

s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)

s3 = Student()
print(s3.gender)

# __init__  Function 
# constructor -> All classes have a function called __init__(), which is always executed when the object is being initiated

# creating class 
# class Student:
# def __init__( self, fullname ):           #self rakhna jaruri h 
# self.name = fullname

# *The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

class student:
    college_name = "usar"
    name = "bjbffbhjf"          # class attributes

    #default constructor 
    def __init__(self):
        pass

    #parametrized construcotr
    def __init__(self,fullname,marks):
        print("adding new student in the database")
        self.name= fullname                          # obj attribute > class attribute
        self.marks=marks

s1 = student("karan",89)
print(s1.name)            
print(s1.marks)

s2 = student("rahul",95)
print(s2.name , s2.marks)
print(s2.marks)

print(student.college_name) # or print(s2.college_name) or s1

# METHODS -> Methods are functions that belong to objects.

class bachhe:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("welcome",self.name,)

    def your_marks(self):
        return self.marks      #or , # print("your marks is",self.marks)

s1=bachhe("priyanshi",98)
s1.welcome()
print(s1.your_marks())

# Q. Create student class that takes name & marks of 3 subjects as arguments in constructor Then create a method to print the average

class students():

    def __init__(self,name,marks):
        self.name= name
        self.marks=marks

    def sum(self):
        sum=0
        for val in self.marks:
            sum = sum+val
        return sum 

    def avg(self):
        avg = self.sum()/len(self.marks)
        print(avg)

s1= students("shreya",[88,69,80])
print(s1.name)
print(s1.marks)
print(s1.sum())
s1.avg()

# mam code 

#     def get_avg(self):
#     sum = 0
#     for val in self.mrrks:
#         sum +=val
#     print("hi",self.name,"your avg marks is ",sum/3)
# 
# s1= students("shreya",[88,69,80])
# s1.get_avg()

# Static Methods -> Methods that don’t use the self parameter (work at class level)

class bachhe:

    def __init__(self,name,marks):
                self.name= name
                self.marks=marks

   
    def hello():
        print("hello")
    

s1 = bachhe("prince",88)
s1.hello()

