"""
Oppgave 2: Konvertering
"""

F = float(input("Velg temperatur i farenheit: "))  # Temperatur i farenheit
print("temperatur i farenheit: {:.1f}".format(F))  # Printer input

C = (F-32)*5/9  # Variabelen som konverterer fra farenheit til celsius
print("temperatur i celsius: {:.1f}".format(C))  # Printer konvertert temperatur

"""
Kjøreeksempel:
Velg temperatur i farenheit: 100
temperatur i farenheit: 100.0
temperatur i celsius: 37.8
"""
