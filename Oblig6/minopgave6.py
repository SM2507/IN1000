"""
Skriv en klasse Person med en konstruktør som tar imot navn og alder. I tillegg skal
konstruktøren ha en tom liste hobbyer. Skriv en metode leggTilHobby som tar imot
en tekststreng og legger den til i hobbyer-listen. Skriv også en metode skrivHobbyer.
Denne metoden skal skrive alle hobbyene etter hverandre på en linje. Gi deretter
Person-klassen en metode skrivUt som i tillegg til å skrive ut navn og alder kaller på
metoden skrivHobbyer. La brukeren skrive inn navn og alder, og lag et Person-objekt
med informasjonen du får. Deretter skal brukeren ved hjelp av en løkke få legge til så
mange hobbyer de vil. Når brukeren ikke lenger ønsker å oppgi hobbyer skal
statistikk om brukeren skrives ut.
"""

class Person(object):
    def __init__(self, navn, alder):
        self.navn = navn
        self.alder = alder
        self.hobbyer = []

    def leggTilHobby(self, streng):
        self.hobbyer.append(streng)

    def skrivHobbyer(self):
        for i in self.hobbyer:
            print(i)

    def skrivUt(self):
        print(self.navn, self.alder)
        self.skrivHobbyer()

mittobjekt = Person(input("Navn: "), int(input("Alder: ")))

mittobjekt.leggTilHobby(input("Legg til hobby: "))
    