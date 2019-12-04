"""
Oppgave 5: Å telle bokstaver og ord
"""

# Definerer en funksjon som teller antall symboler/karakterer i en streng
def antallbokstaver(streng):
    return len(streng)

# Definerer funksjonen som returnerer en ordbok som inneholder ord som nøkler og 
# forekomst av ordene som verdier
def bokstavteller(streng):
    streng = streng.split(" ")  # Splitter strengen der det finnes ett mellomrom, og legger dem
    # som element i en liste, streng

    # for-løkke i en "tom" ordbok som brukes til å fylle inn nøkler og verdier
    wordbook = {streng[i]: streng.count(streng[i]) for i in range(len(streng))}
    return wordbook  # Returner ordbok

setning = input("Skriv inn setning:\n")  # Bruker skriver inn en setning.
a = bokstavteller(setning)  # kaller på funksjon bokstavteller med setning som argument

print("Det er {} ord i setningen din.".format(len(setning.split(" "))))  # Printer antall ord
for i in range(len(bokstavteller(setning))):  # Printer hvilke ord som finnes og deres forekomst
    print("Ordet {} forekommer {} gang(er) i setningen din, og har {} bokstaver".format\
(setning.split(" ")[i], a[setning.split(" ")[i]], antallbokstaver(setning.split(" ")[i])))

"""
Skriv inn setning:
Amalie har fire katter !
Det er 5 ord i setningen din.
Ordet Amalie forekommer 1 gang(er) i setningen din, og har 6 bokstaver
Ordet har forekommer 1 gang(er) i setningen din, og har 3 bokstaver
Ordet fire forekommer 1 gang(er) i setningen din, og har 4 bokstaver
Ordet katter forekommer 1 gang(er) i setningen din, og har 6 bokstaver
Ordet ! forekommer 1 gang(er) i setningen din, og har 1 bokstaver
"""


