"""
Oppgave 2: Ordbok
Mohammed Shartaz Mostafa
"""
# Lager en dictionary med keys og values
varer = {"melk":14.90, "brød":24.90, "yoghurt":12.90, "pizza":39.90}
print(varer)  # print dictionary

for i in range(2):  # D.R.Y
    vare = input("Sett inn vare: ")  # Lager nøkkelen til prisen 
    varer[vare] = float(input("Tast inn pris: "))  # legger til valuen til keyen
print(varer)
"""
Kjøreeksempel:
{'melk': 14.9, 'brød': 24.9, 'yoghurt': 12.9, 'pizza': 39.9}
Sett inn vare: peanøtter
Tast inn pris: 30
Sett inn vare: rislunsj
Tast inn pris: 12
{'melk': 14.9, 'brød': 24.9, 'yoghurt': 12.9, 'pizza': 39.9, 'peanøtter': 30.0, 'rislunsj': 12.0}
"""