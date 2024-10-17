'''class Color:
    red = 0
    green = 0
    blue = 0

    def __init__(self, r,g,b):
        self.red=r
        self.green=g
        self.blue=b


    def tprint(self,r,g,b):
        print(f'Red{r} green{g} blue{b}')
    
    def toHex(self):
        return '#%02x%02x%02x' % (self.red, self.green, self.blue)
    def redColor(self):
        self.red=255
        for i in range(20):
            print(self.red-i, self.green, self.blue)
gray = Color(0,128,0) 
gray.tprint(0,128,0)       
print(gray.toHex()) 
print(gray.redColor()) '''
from random import*
class Rectangle:
    count=0
    def __init__(self,name,width=0,height=0,color='green'):
        self.width=width
        self.height=height
        self.name=name
        self.color=color
        Rectangle.count+=1
    def inform_count():
        print(f"Īnstance created:{Rectangle.count}")
    def itroduce(self):
            print(f"{self.name} {self.color} {self.width}x{self.height}")
    def calculate_area(self):
          print(f"the area is {self.width*self.height}")
rect1=Rectangle("rectangle",100,3141)
rect1.itroduce()
rect1.calculate_area()
print(f"{rect1.name} {rect1.width}x{rect1.height} {rect1.color}")
rect2=Rectangle("sqwar3e")
rect2.itroduce()
rect2.calculate_area()
print(f"{rect2.name} {rect2.width}x{rect2.height} {rect2.color}")
rectan=[]
colors=['red','green','blue','yellow','purple','orange']
for i in range(100):
        rectan.append(Rectangle(f"Name{i+1}",randint(1,500), randint(1,500), choice(colors)))
for rect in rectan:
    print(f"{rect.name} {rect.width}x{rect.height} {rect.color}")
Rectangle.inform_count()