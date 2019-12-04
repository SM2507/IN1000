"""
Oppgave 4: Billettpris
Mohammed Shartaz Mostafa
"""

def prosedyre(alder = int(input("Din alder: "))):  # Definerer funksjonen
    if alder <= 17:  # Kommentert i tidligere oppgaver
        billettpris = 30
    elif 17 < alder < 63 :
        billettpris = 50
    else:
        billettpris = 35
    print("Bruker er {:d} år gammel, billettprisen blir {:d} kr.".format(alder,\
billettpris))  # Strengformatering, printer streng, alder, og billettpris som streng.

for i in range(4):  # Bruker for løkke til å kalle på funksjon 4 ganger
    prosedyre()

"""
Kjøreeksempel:
Din alder: 21
Bruker er 21 år gammel, billettprisen blir 50 kr.
Bruker er 21 år gammel, billettprisen blir 50 kr.
Bruker er 21 år gammel, billettprisen blir 50 kr.
Bruker er 21 år gammel, billettprisen blir 50 kr.
"""

"""
Problemet er at brukeren bare skriver inn alderen én gang og 
alderen og billettprisen blir skrevet ut fire ganger.  
"""