from datetime import*

class Dog:
    list_name=[]
    list_cena=[]

    def __init__(self, name=str,age=int, breed='unknown',weight=float, gender=str,cena=float, color='melns'):
        self.name=name
        self.age=age
        self.breed=breed
        self.weight=weight
        self.gender=gender
        self.cena=cena
        self.color=color
        Dog.list_name.append(
self.name
)
        Dog.list_cena.append(self.cena)

    def info(self):
        print(f'Suņa vārds {
self.name
} viņam ir {self.age} gadi un suņa cena ir {self.cena} suņa krāsa {self.color} sver{self.weight}')

    def registration(self):
        now = 
datetime.now
()
        dt_string= now.strftime('%d/%m/%Y %H:%M:%S')
        print(f'Suns {
self.name
} ir reģistrēts {dt_string}')

    def sacensibas(self,vieta,pilseta):
        self.vieta=vieta
        self.pilseta=pilseta
        print(f'Suns {
self.name
} piedalījās sacensībās {self.pilseta} un ieguva {self.vieta} vietu')

    def svars(self,svars1):
        self.svars1=svars1
        a=input('Vai svars palielinājās? (samazinājās, palielinājās, nemainījās)')
        if a=='samazinājās':
           self.weight-=self.svars1
        if a=='palielinājās':
            self.weight+=self.svars1
        if a=='nemainījās':
            print(f'Svars palika nemainīgs {self.weight} kg')

    def vitamini(self,doze):
        self.doze=doze
        daudzums=self.weight/doze
        print( f'suņa deva ir {round(daudzums,0)}')
       
suns1=Dog('Toms', 12, 'Dog', 32, 'v', 250.00)
suns1.info
()
suns2=Dog('Lords', 9, 'Dog', 28, 'v', 200.00,'balts')
suns2.info
()
suns3=Dog('Simba', 7, 'Dog', 22, 's', 150.00)
suns3.info
()
suns1.registration()
suns1.sacensibas(1,'Rīgā')
suns1.svars(5)
suns1.info
()
suns1.vitamini(10) 