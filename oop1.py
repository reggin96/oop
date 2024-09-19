class Person:
    def set(self,name,age):
        self.name = name
        self.age = age
    def output(self):
         print("persona:",self.name,"kuram ir",self.age,"gadi")

p=Person()
p.set('Vasja',200)
p.output()
k=Person()
k.set("Marks",17)
k.output()