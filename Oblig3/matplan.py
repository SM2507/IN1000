"""
Oppgave 5: Matplan
Mohammed Shartaz Mostafa
"""
# Lager ordboken med nøkler og verdier
matplan = {"Olav Haakonsen": ["eggerøre","eggs benedict","kylling fritata"],\
"Marius Klonk": ["sitronterte","ramen","linguini"],\  
"Brynhild Mikkelsen": ["banansmoothie","rundstykker","kyllingfilet og laks"]}

def matplanutskrift(navn = input("Tast inn navn: ")):  # Definerer funksjon
    if navn not in matplan:  # Hvis navnet ikke finnes i ordbok...
        print("Beboer ikke registrert")
    else:  # Ellers...Bruker strengformatering til å skrive ut navn og matplan 
        print("matplanen til {}: \n{}".format(navn,matplan[navn]))

matplanutskrift()  # Kaller på funksjonen
"""
Kjøreeksempel:
Tast inn navn: Marius Klonk
matplanen til Marius Klonk:
['sitronterte', 'ramen', 'linguini']
"""