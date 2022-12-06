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

