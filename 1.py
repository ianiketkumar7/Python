class sum1:
    a=10
    b=20
    def __init__(self,firstname,lastname):
        self.Fname=firstname 
        self.Lname=lastname
obj1=sum1("a","b")
print(obj1.a+obj1.b)
obj2=sum1("Nike","gamerz")
print(obj2.Fname)
class cars:
    def method1(self,model,regno):
        self.model=model
        self.gegno=regno
    def method2(self):
        return self.model
    def method3(self):
        return self.regno
car1=cars()
car2=cars()

car1.method1("lamborgini sain","lamborgini terzo")
print(car1.method2())
print(car1.method3())


class cars:
    def setname(self,carname):
        self.carname = carname

    def getname(self):
        return(self.carname)

name=input("enter car name : ")
car1=cars()
car1.setname(name)
n=car1.getname()
print("Entered car Name is: ",n)