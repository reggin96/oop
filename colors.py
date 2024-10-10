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
class Rectangle:
    def __init__(self,name,width=0,height=0,color='green'):
        self.width=width
        self.height=height
        self.name=name
        self.color=color
rect1=Rectangle("rectangle",100,3141)
print(f"{rect1.name} {rect1.width}x{rect1.height} {rect1.color}")
rect2=Rectangle("sqwar3e")
print(f"{rect2.name} {rect2.width}x{rect2.height} {rect2.color}")
rectan=[]
for i in range(100):
    rectan.append(Rectangle(f"Name{i+1}"))
for rect in rectan:
    print(f"{rect.name} {rect.width}x{rect.height} {rect.color}")