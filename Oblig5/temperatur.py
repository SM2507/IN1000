"""
Oppgave 2: Temperatur
"""

with open("temperatur.txt","r") as tem:  # Åpne temperatur.txt og les den "r"
    temperaturer = [int(line) for line in tem]  # legg til det som står linje for linje som heltall

def gjennomsnitt(liste):  # definerer en funksjon med en parameter
    s = 0  # dummy variabel
    for i in liste:  # For element i liste...
        s+=i  # summer summen av de forrige elementene pluss det neste
    return s/len(liste)  # Returner summen delt på gjennomsnittet.

print("Gjennomsnittet av temperaturene over 12 mnder er {}".format\
(gjennomsnitt(temperaturer)))  # Skriver ut streng og gj.snittstemp. formatert.
    
