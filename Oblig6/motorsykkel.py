"""
Oppgave 2: Motorsykkel
"""
class Motorsykkel(object):  # Lager en klasse, Motorsykkel, som arver fra object-klassen.
# Lager så en konstruktør som tar i mot verdier når en skal lage en instans av klassen.
    def __init__(self, merke, registreringsnummer, kilometerstand):
        self.merke = merke  # Definerer så instansvariablene
        self.registreringsnummer = registreringsnummer
        self.kilometerstand = kilometerstand
    
    def kjor(self, km):  # Definerer en metode innen klassen
        self.kilometerstand += km  # Øker kilometerstanden
    
    def hentKilometer(self):  # Ny metode
        return self.kilometerstand  # returner kilometerstanden

    def skrivUt(self):  # Metode som skriver ut merke, reg. #, og kilometerstand
        print("Merke: ", self.merke)
        print("Reg. Nummer: ", self.registreringsnummer)
        print("Kilometerstand: ", self.kilometerstand,"\n")
