"""
Oppgave 2: Motorsykkel
"""
from motorsykkel import Motorsykkel  # Importerer Motorsykkelklassen fra motorsykkelfila

def hovedprogram():   #Definerer et hovedprogram
    motorsykkel1 = Motorsykkel("Ducati", "IT25392", 50)  # Lager en instans av MOtorsykkel-klassen
    motorsykkel2 = Motorsykkel("Honda", "JP89132", 432)  # ny instans med nye instansvariabler
    motorsykkel3 = Motorsykkel("BMW", "DE74201", 100)  # ny instans
    motorsykkel1.skrivUt()  # Skriver ut instansvariablene ved å kalle på skrivUt-metoden...
    motorsykkel2.skrivUt()
    motorsykkel3.skrivUt()  # ... tilsvarende 
    motorsykkel3.kjor(10)  # kaller på kjor-metoden innen Motorsykkelklassen vha. instansen
    motorsykkel3.skrivUt()  # Skriver ut de endrede instansvariablene ved å kalle på skrivUt-metoden

hovedprogram() # Kaller på hovedprogram()



