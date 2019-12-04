"""
Oppgave 1: Salgstatistikk
"""

def innlesning(filnavn):  # Lager en funksjon, innlesning, skal ta i mot en tekstfil.
    with open(filnavn, "r") as fil:  # Åpner filnavn og leser den, markert med "r".

# Leser hver linje i fil og splitter verdiene, som finnes i en liste med lengde 2.
# Indeks 0 inneholder nøklene, og indeks 1 inneholder verdiene jeg ønsker å ha i ordboka.
        stats = {"{}".format(line.split(" ")[0]): int(line.split(" ")[1]) for line in fil}
    return stats  # returner ordbok.

def maanedensSalgsperson(wb): # Lager en funksjon, maanedenssalgsperson, skal ta i mot en ordbok.
# Går gjennom verdiene til ordboka, gjør dem om til en list og finner maksimum i lista.
# Finner så indeksen til maksverdien.
    max_index = list(wb.values()).index(max(list(wb.values())))
# Gjør om nøklene i ordboka til en liste, og bruker maksindeksen for å finne hva nøkkelen er.
    man = list(wb.keys())[max_index]
# Skriver så ut en streng, med nøkkelen, som er den mest selgende, og salgstallet, som er verdien.
    print("Månedens ansatte er {} med {} salg.".format(man, wb[man]))

def totaltAntallSalg(wb):  # Lager en funksjon, totaltAntallSalg, skal ta i mot en ordbok.
    value = list(wb.values()) # Gjør om verdiene i ordboka til en liste.
    return sum(value)  # Bruker sum-funksjonen for å finne summen som skal bli returnert.

def gjennomsnittSalg(wb): # Lager en funksjon, gjennonsnittSalg, skal ta i mot en ordbok.

# Kaller på totaltAntallSalg(), og dividerer med lengden av lista som inneholder alle ansatte.
    return totaltAntallSalg(wb)/len(list(wb.keys()))  # Returnerer gjennomsnittet.

def hovedprogram():  # Lager funksjon, hovedprogram, som skal kalle på alle funksjonene overfor.
    statistikk = innlesning("salgstall.txt")  # Leser inn tesktfila, får en ordbok.
    maanedensSalgsperson(statistikk)  # Skriver ut månedens beste selger.
    # Skriver ut antall selgere.
    print("Aktive selgere denne måneden: ", len(list(statistikk.keys())))

    print("Totalt antall salg: ",totaltAntallSalg(statistikk))  # Skriver ut antall salg
    print("Gjennomsnittlig antall salg per selgsperson: ",\
gjennomsnittSalg(statistikk))  # Skriver ut gjennomsnittssalget

hovedprogram()  # Kaller på hovedprogram()


"""
Kjøreeksempel:
Månedens ansatte er Heidi med 133 salg.
Aktive selgere denne måneden:  8
Totalt antall salg:  668
Gjennomsnittlig antall salg per selgsperson:  83.5
"""