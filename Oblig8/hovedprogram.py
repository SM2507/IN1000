from node import Node  # Importer
from rack import Rack
from regneklynge import Regneklynge

abel = Regneklynge(12)  # Oppretter en instans, med maks noder/rack = 12
for i in range(650):  # Setter inn 650 noder
    abel.settInnNode(Node(64,1))

for i in range(16):  # Setter inn 16 noder
    abel.settInnNode(Node(1024,2))
# Print
print("Noder med minst 32 GB:", abel.noderMedNokMinne(32))
print("Noder med minst 64 GB:", abel.noderMedNokMinne(64))
print("Noder med minst 128 GB:", abel.noderMedNokMinne(128))
print("Antall prosessorer:", abel.antProsessorer())
print("Antall rack:", abel.antRacks())