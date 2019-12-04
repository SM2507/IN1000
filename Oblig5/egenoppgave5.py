"""
Oppgave 5: Egen oppgave
Les ut informasjon fra en txt-fil på samme format som den vedlagte fila,
og lagre den i en ordbok med passende nøkler og verdier.
Du skal ha en ordbok som inneholder navnet på målet og selve målet. Lag så en funksjon som
skriver alle nøkler og verdier til kommandolinja på en oversiktlig måte. 
"""

with open("maal.txt","r") as m:  # Åpner tekstfilen som m, "r" betyr at den leses.
# Leser hver linje i fil og splitter verdiene, som finnes i en liste med lengde 2.
# Indeks 0 inneholder nøklene, og indeks 1 inneholder verdiene jeg ønsker å ha i ordboka.
    mål = {"{}".format(line.split(":")[0]): float(line.split(":")[1]) for line in m}

def utskrift(D):  # Definerer en funksjon som tar i mot en ordbok.
# Kjører en for-løkke så mange ganger som lista med nøkkelverdier er lang 
    for i in range(len(list(D.keys()))):
# Printer så ut nøklene og verdiene linje etter linje. 
        print(list(D.keys())[i],"-",D[list(D.keys())[i]])

utskrift(mål)
    
"""
Kjøreeksempel:
Skulderbredde - 48.1
Halsvidde - 17.6
Livvidde - 35.8
"""