# bilet satyp aluu
from my_exceptions import BilettinSanyJetishsiz

class BiletAluuSystem:
    # kinolor = []
    def __init__(self, bilettin_sany:int,tickets):
        self.bilets  = bilettin_sany
        self.tickets = tickets

    def bilet_aluu(self,number_bilets: int, kino):

        if self.tickets[kino] < number_bilets:
            raise BilettinSanyJetishsiz("Biletterdin sany jetishsiz")
        else:
            self.tickets[kino] = self.tickets[kino] - number_bilets
            self.bilets -= number_bilets
    
    def action(self):
        while self.bilets > 0:
            try:
                for i,key in enumerate(self.tickets):
                    print(i,key)
                kino = input("Kaisy kino?:")
                inp = int(input("Kancha bilet?:"))
                self.bilet_aluu(inp,kino)
            except ValueError as e:
                print(e)
            except BilettinSanyJetishsiz as b:
                print(b)
            else:
                print(f"bizde {self.bilets} kaldy")
                print(f"{inp} bilet satyldy")
        
        print("Biletter satylyp buttu")

def bilet_aluu() -> None:
    number_of_tickets = 10

    while number_of_tickets > 0:
        try:
            inp = int(input("Kancha bilet?:"))
        except ValueError as e:
            print(e)
        else:
            try:
                if number_of_tickets < inp:
                    raise BilettinSanyJetishsiz("Билеттин саны жетишсиз")
                else:
                    number_of_tickets = number_of_tickets - inp
                print(f"{number_of_tickets} бидет калды")
                print(f"{inp} билет сатылды")
            except BilettinSanyJetishsiz as b:
                print(b)


# bilet_aluu()
bb = BiletAluuSystem(20, {'Batman':5, 'Avatar': 10, 'Superman': 5})

bb.action()