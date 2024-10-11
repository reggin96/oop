import math
class Ball:

    def __init__(self,diameter):
      self.diameter=diameter
      self.health=120
    def volume(self):
       return(math.pi*self.diameter**3)/6
    def meeting(self, energy):
       energy.health-=20 


class Cube:
    def __init__(self,hwd):
      self.hwd=hwd
      self.health=120
    def volume(self):
       return(self.hwd**3)
    def meeting(self, energy):
       energy.health-=20 
hero1=Ball(5)
print(hero1.volume()) 
hero2=Cube(5)
print(hero2.volume())
print(hero1.health)
hero1.meeting(hero2)
print(hero2.health)