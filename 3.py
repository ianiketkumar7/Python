class Person:
    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name
p1=Person()
p2=Person()
p1.setname("op")
p2.setname("jheri")
a=p1.getname()
b=p2.getname()
print(a)
print(b)