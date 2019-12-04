"""
Oppgave 6: Egen oppgave
Lag en klasse, Bankkonto, som tar inn nødvendig informasjon som navn, fødselsdato, adresse,
telefonnummer, og mer om ønsket, vha. en konstruktør, enten __call__ eller __init__. Sørg
for at kontobalansen er lik 0 ved oprettelse. Bruk inkapsling til dette, ettersom bruker
ikke skal kunne endre balansen utenfor metodene.
Deretter lag metoder som lar bruker kunne gjøre innskud og uttak, og som viser kontobalanse eter 
utførte operasjoner. Til slutt lager du en metode som kun viser kontobalansen.
"""

class Bankkonto(object):
    def __init__(self, navn, fødsel, adresse, nummer):  # Konstruktør
        self.navn = navn  
        self.fødsel = fødsel
        self.adresse = adresse
        self.nummer = nummer
        self.__balanse = 0  # Privat variabel, kan ikke benyttes utenfor klassen.

    def innskudd(self, beløp):  # Metode
        if beløp <= 0:
            print("Ugyldig intasting, vennligst tast inn et positivt beløp")
        else:
            self.__balanse += beløp
            print("Kontobalanse: ", self.__balanse)

    def uttak(self, beløp):  # Metode
        if beløp > self.__balanse:
            print("Du har ikke tilstrekkelige midler på denne kontoen")
        else:
            self.__balanse -= beløp
            print("Kontobalanse: ", self.__balanse)
    
    def kontobalanse(self):  # Metode
        print("Kontobalanse:", self.__balanse)



 
my_acc = Bankkonto("Mohammed Mostafa", 10101991, "Nordbyveien 3", 47777799)  # Instans av klassen
my_acc.innskudd(1000)  # Gjør et innskudd. kaller på innskudd-metoden
my_acc.kontobalanse() # Sjekker kontobalansen

