"""
Bruk en liste eller en ordbok til å lagre verdier for summer av to terningkast.
Gjør dette tilstrekkelig mange ganger, N ganger, og finn sannsynlighetene.
Skriv ut sannsynlighetene til de forskjellige summene.
"""

from random import randint  # Importerer randint
N = 10000  # Terningene skal slås N ganger
# Lager en ordbok med summene som nøkler og respektive startverier lik 0
sumdice = {i:0 for i in range(2,13)}  

for i in range(N):  # løkke
    a = randint(1,6)  # Gir et heltall fra 1 til 6
    b = randint(1,6)
    sumdice[a+b] += 1  # Bruker summen som nøkkel, og øker korrespondende verdi med 1.

for i in range(2,13):  # Skriver ut summene og sannsynlighetene
    print("Sum = {:d}: {:.3f}".format(i, sumdice[i]/N))  # Strengformatering

"""
Kjøreeksempel
Sum = 2: 0.027
Sum = 3: 0.055
Sum = 4: 0.077
Sum = 5: 0.112
Sum = 6: 0.148
Sum = 7: 0.165
Sum = 8: 0.137
Sum = 9: 0.110
Sum = 10: 0.085
Sum = 11: 0.055
Sum = 12: 0.030
"""


