

from celle import Celle  # Importerer Celle-klassen fra celle.py
from random import randint  # Importerer randint  
import os  # Importerer os

class Spillebrett(object):  # Lager klasse
    def __init__(self,m,n):  # Konstruktør tar inn rader og kolonne, setter instansvariabler
        self._rader = m  # Bruker innkapsling
        self._kolonner = n
        # List comprehension for å lage rutenettet
        self.rutenett = [[0 for i in range(self._kolonner)]for i in range(self._rader)]
        self.generasjon = 0  # Generasjonsnummer
        self.generer(self.rutenett)  # Kaller på generer metoden inni klassen


    def generer(self,ruter):  # Metode generer
        for i in range(len(ruter)):
            for j in range(len(ruter[i])):
                x = Celle()  # Lager et objekt av klassen Celle
                if randint(0,2) == 1:  # En viss sannsynlighet for at cellen er levende
                    x.settLevende()
                    ruter[i][j] = x  # Objektet blir lagt til på sin plass
                else:
                    ruter[i][j] = x

    def tegnBrett(self):  # Tegner brettet
        os.system("cls")  # Klarerer kommandovinduet
        for i in range(len(self.rutenett)):
            print("")
            for j in self.rutenett[i]:
                print(j.tegn(), end = " ")
        print("\n Antall levende celler: {:d}".format(self.finnAntallLevende()))  # Strengformatering
        print("Generasjon: {:d} ".format(self.generasjon))  # Kaller på metodene inni klasen

        

    def finnNabo(self, m,n):  # Metode min nabo
        self.rutenett[m][n].nabo.clear()  # For hver iterasjon skal lista tømmes ettersom naboer dør og gjenopplives
        # Planen var å ta i mot hele rutenettet og finne naboene til hvert listeelement. 
        i_max = len(self.rutenett)-1
        for i in range(0,len(self.rutenett)):
            j_max = len(self.rutenett[i])-1
            for j in range(0,len(self.rutenett[i])):
                if 0 <i <i_max:  # Alle de indre radene
                    self.rutenett[i][j].nabo.append(self.rutenett[i-1][j])
                    self.rutenett[i][j].nabo.append(self.rutenett[i+1][j])
                    if j > 0:  # Alle naboene til venstre for nåværende objekt
                        self.rutenett[i][j].nabo.append(self.rutenett[i-1][j-1])#opp
                        self.rutenett[i][j].nabo.append(self.rutenett[i][j-1])#current
                        self.rutenett[i][j].nabo.append(self.rutenett[i+1][j-1])#ned
                    if j < j_max:  # Til høyre
                        self.rutenett[i][j].nabo.append(self.rutenett[i-1][j+1])
                        self.rutenett[i][j].nabo.append(self.rutenett[i][j+1])
                        self.rutenett[i][j].nabo.append(self.rutenett[i+1][j+1])
                elif i == 0 :  # Øverste rad
                    self.rutenett[i][j].nabo.append(self.rutenett[i+1][j])
                    if j > 0:
                        self.rutenett[i][j].nabo.append(self.rutenett[i][j-1])
                        self.rutenett[i][j].nabo.append(self.rutenett[i+1][j-1])
                    if j < j_max:
                        self.rutenett[i][j].nabo.append(self.rutenett[i][j+1])
                        self.rutenett[i][j].nabo.append(self.rutenett[i+1][j+1])

                elif i == i_max:  # Nederste rad
                    self.rutenett[i][j].nabo.append(self.rutenett[i-1][j])
                    if j > 0:
                        self.rutenett[i][j].nabo.append(self.rutenett[i][j-1])
                        self.rutenett[i][j].nabo.append(self.rutenett[i-1][j-1])
                    if j < j_max:
                        self.rutenett[i][j].nabo.append(self.rutenett[i][j+1])
                        self.rutenett[i][j].nabo.append(self.rutenett[i-1][j+1])  
# Uheldigvis skulle naboene til objektene bli funnet vha. koordinater, dermed ble koden ineffektiv.   
# I stedet for å returnere alle listene, måtte samme kalkulasjoner gjentaes, og kun en liste ble returnert.                   
        return self.rutenett[m][n].nabo  

    def oppdatering(self):
        ded2lev = []  # Tomme lister
        lev2ded = []
        self.generasjon += 1  # Øker gen.#

        for i in range(len(self.rutenett)):
            for j in range(len(self.rutenett[i])):  # Går inn på hvert objekt
                naboer = self.finnNabo(i,j)  # Kaller på finnNabo som gir en liste
                teller = 0  # Setter teller lik 0
                for cell in naboer:
                    if cell.erLevende():
                        teller += 1  # Øker teller proporsjonalt med antall levende naboer

                if self.rutenett[i][j].erLevende():
                    if teller < 2 or teller > 3:  # Dersom det er færre enn 2 eller flere enn 3 naboer
                        lev2ded.append(self.rutenett[i][j])  # Legg til disse i lista der cellene skal dø
                else:
                    if teller == 3:  # Dersom en død celle har akkurat 3 celler
                        ded2lev.append(self.rutenett[i][j])  # Gjenoppliv den cella

        # Oppdaterer hvilke celler som er døde og levenende for neste gen.
        for cell in ded2lev:
            Celle.settLevende(cell)
        for cell in lev2ded:
            Celle.settDoed(cell)

    def finnAntallLevende(self):
        teller = 0
        for i in range(len(self.rutenett)):
            for j in range(len(self.rutenett[i])):
                if self.rutenett[i][j].erLevende():
                    teller += 1  # Øker teller proporsjonalt med antall levende på hele brettet

        return teller

if __name__ == "__main__":  # Kjøres kun dersom spillebrett kjøres som main
    test = Spillebrett(10,10)  # Testkode
    test.oppdatering()
    test.tegnBrett()