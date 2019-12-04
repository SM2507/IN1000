
from spillebrett import Spillebrett  # Importerer Spillebrett

def main():
    m = int(input("Skriv inn antall rader: "))  # Rader
    n = int(input("Skriv inn antall kolonner: "))  # Kolonner
    spill = Spillebrett(m,n)  # Lager et objekt av Spillebret
    spill.tegnBrett()  # Skriver ut brett til den 0. generasjonen

    k = True  # Boolsk variabel
    while k:  # Løkke
        g = input("Trykk Enter for neste generasjon \nSkriv q for å avslutte: \n")
        if g == "q":
            k = False
        else:
            spill.oppdatering()  # Hvis ikke bruker avslutter, skal brettet oppdatere seg
            spill.tegnBrett()  # Og skrives ut for neste generasjon

main()