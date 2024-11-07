class Olimp:
    def __init__(self, vards, uzvards, klase, skola,):
        self.vards=vards
        self.uzvards=uzvards
        self.klase=klase
        self.skola=skola
    def laiks(self):
         sāklaiks=int(input("ievadiet stundu:"))
         sāklaiks1=int(input("ievadiet min:"))
         pametlaiks=int(input("ievadiet stundu:"))
         pametlaiks1=int(input("ievadiet minūti:"))
         aprē=pametlaiks-sāklaiks
         aprē1=pametlaiks1-sāklaiks1
         print(f"{self.vards}pildija uzdevumus {aprē} stundu {aprē1} minūtes")
    def point(self):
        punkti1=int(input("ievadiet 1. uzd rezultātu max 20:"))
        punkti2=int(input("ievadiet 2. uzd rezultātu max 20:"))
        punkti3=int(input("ievadiet 3. uzd rezultātu max 20:"))
        punkti4=int(input("ievadiet 4. uzd rezultātu max 20:"))
        punkti5=int(input("ievadiet 5. uzd rezultātu max 20:"))
        punkti=punkti1+punkti2+punkti3+punkti4+punkti5
        prem=float(0.1*punkti)
        print(f"{self.vards} {self.uzvards} ieguva:{punkti}")
        if punkti>=70 and punkti<80:
            
            print(f"{self.vards} {self.uzvards} ieguva:{punkti} punktus un ieguva 3. pakāpes diplomu un saņem {prem}")
        elif punkti>=80 and punkti<90:
            print(f"{self.vards} {self.uzvards} ieguva:{punkti} punktus un ieguva 2. pakāpes diplomu un saņem {prem}")
        elif punkti>=90:
            print(f"{self.vards} {self.uzvards} ieguva:{punkti} punktus un ieguva 1. pakāpes diplomu un saņem {prem}")
        else:
            print(f"{self.vards} {self.uzvards} ieguva:{punkti} punktus,bet diplomu neieguva")
    
    def print_info(self):
        print(f"{self.vards} {self.uzvards} {self.klase}. klase {self.skola}. ")
    
dal_1=Olimp("Marks", "Tučs", "11", "Maltas Vidusskola")
dal_2=Olimp("Adriāns", "Taškāns", "11", "Liepu Vidusskola")
dal_3=Olimp("Anna", "Itkače", "11", "Vīnes Vidusskola")
dal_4=Olimp("Viktorija", "Loģinovas", "11", "Poļu Vidusskola")
dal_5=Olimp("Daniils", "Prančs", "11", "Kristietīgā Vidusskola")
dal_1.print_info()
dal_2.print_info()
dal_3.print_info()
dal_4.print_info()
dal_5.print_info()
dal_1.point()
dal_2.point()
dal_3.point()
dal_4.point()
dal_5.point()
dal_1.laiks()
dal_2.laiks()
dal_3.laiks()
dal_4.laiks()
dal_5.laiks()