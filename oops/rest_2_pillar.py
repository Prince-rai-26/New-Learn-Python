# INHERITANCE AND POLYMORPHISM 

# INHERITANCE -> when one class(child/derived) derives the properties and method of another class (parent/base).
# class car:
# ....
# class toyotacar(car):
# .... 

class car:
    color="black"
    def start():
        print("car started")

    def stop():
        print("car stoped")

class toyotacar(car):
    def __init__(self,name):
        self.name= name

c1=toyotacar("fortunor")
c2=toyotacar("prius")

print(c1.color)