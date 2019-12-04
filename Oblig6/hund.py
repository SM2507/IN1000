"""
Oppgave 4: Hund
"""

class Hund(object):  # Lager klassen Hund
    def __init__(self, alder, vekt):  # Konstruktøren tar i mot to argumenter, alder og vekt, når instansen lages.
        self.alder = alder  # Definerer instansvariablene
        self.vekt = vekt
        self.metthet = 10  # Denne variablen settes alltid til 10 hver gang en instans av Hund opprettes.
    
    def hentvekt(self):  # Definerer en instansmetode som ikke tar argumenter
        return self.vekt  # reutrnerer alder og vekt til hunden

    def hentalder(self):
        return self.alder
    
    def spring(self):   # instansmetode som ikke tar argumenter
        self.metthet -= 1  # verdien til metthetvariablen innen klassen reduseres med 1
        if self.metthet <5:  # dersom verien er mindre enn 5, reduser vekt
            self.vekt -= 1

    def spis(self,heltall):  # instansmetode som tar ett argument
        self.metthet += heltall  # Økt metthet
        if self.metthet > 7:  # Dersom metthet er større enn 7, øk vekt. 
            self.vekt +=1

