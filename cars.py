class Autom:
    def __init__(self, marka, modelis, gads):
        self.marka=marka
        self.modelis=modelis
        self.gads=gads
    def rez(self,):
        self.dienas=int(input("ievadiet dienu skaitu"))
        if self.gads>2020:
            self.cena_par_dienu=50
            self.cena=self.dienas*self.cena_par_dienu
        else:
            self.cena_par_dienu=30
            self.cena=self.dienas*self.cena_par_dienu
    def output(self):
        print(f"{self.marka} {self.modelis} {self.gads},maksājiet {self.cena}")



auto1=Autom("Audi", "A6", 2018)
auto2=Autom("BMW","X5",2021)
auto1.rez()
auto2.rez()
auto1.output()
auto2.output()
 