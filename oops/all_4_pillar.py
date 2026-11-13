# OOPS -> ABSTRACTION , ENCAPSULATION , INHERITNACE, POLYMORPHISON

# ABSTRACTION - > Hiding the implementation details of a class and only showing the essential feature to the user (unnecessary detils to hide)

# ENCAPSULATION - > Wrapping data and function into a single unit (object)

class Car:
    def __init__(self):
        self.acc= False
        self.brk = False
        self.cluth=False

    def start(self):
        self.acc= True
        self.brk = True
        self.cluth=True
        print("car started..")

c1 = Car()
c1.start()

# Create Account class with 2 attributes - balance & account no.and Create methods for debit, credit & printing the balance

class account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.acc_no = acc

    def debit(self,amount):
        self.balance -=amount
        print("Rs",amount,"was debited")
        print("your balance is now",self.get_balance())

    def credit(self,amount):
        self.balance +=amount
        print("Rs",amount,"was credoted")
        print("your balance is now",self.get_balance())

    def get_balance(self):
        return self.balance

acc1= account(10002,5184)
print(acc1.balance)
print(acc1.acc_no)

acc1.debit(5000)
print()
acc1.credit(50002)

# INHERITANCE AND POLYMORPHISM 

# del keyword -> used to delete object properties or object itself .
#del s1.name
# del s1

class stu:
    def __init__(self,name):
        self.name=name

s1 = stu("priyanshi")
print(s1.name)
del s1.name    
# print(s1.name)   # it will give the error as it is now deleted 

# PRIVATE(like) attributes and methods --> __ ye lagana h toh wo chij private bn jayegi class ke andar 

# private attributes and methods are meant to be used only within the class and are not accesible from outside the class 

class account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print( self.__acc_pass)

acc1 = account(12345,"piyu")
print(acc1.acc_no)
# print(acc1.__acc_pass)   #now it is priate after putting __ after dot (acc1.)

print(acc1.reset_pass()) 

class person:
    __name ="anoynomous"

    def __hello(self):
        print("hello person")

    def welcome(self):
        print(self.__hello())

p1= person()
print(p1.welcome())






