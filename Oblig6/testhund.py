"""
Oppgave 4: Hund
"""

from hund import Hund  # importerer Hund-klassen fra hund fila

def hovedprogram():
    bisk = Hund(5, 12)  # Lager en instans av hund med alder = 5, vekt = 12

    bisk.spring()  # Kaller på instansmetoden spring
    print("Hundens vekt:", bisk.hentvekt()) # Printer vekt ved å kalle på instansmetode hentinfo.
    bisk.spring()
    print("Hundens vekt:", bisk.hentvekt())
    bisk.spis(1)  # Kaller på instansmetoden spis
    print("Hundens vekt:", bisk.hentvekt())
    bisk.spis(1)
    print("Hundens vekt:", bisk.hentvekt())

hovedprogram()



