from node import Node
from rack import Rack

class Regneklynge(object):
	## Oppretter tom regneklynge for racks med oppgitt maxtall noder/ rack
    def __init__(self, noderPerRack): 
        self._rk = [Rack()]
        self.npr = noderPerRack   # @param noderPerRack max antall noder som kan plasseres i et rack
        

	## Alternativ konstruktor for de som loser oppgave d). Kan ellers ignoreres
	## Leser data om regneklynge fra fil, bygger datastrukturen.
	# @param filnavn filene der dataene for regneklyngen ligger
    #def __init__(self, filnavn):
    #    pass

	## Plasserer en node inn i et rack med ledig plass, eller i et nytt
	# @param node referanse til noden som skal settes inn i datastrukturen
    def settInnNode(self, node):
        for j in range(len(self._rk)):
            if self._rk[j].getAntNoder() < self.npr:
                self._rk[j].settInn(node)
                break
            elif j == len(self._rk)-1 and self._rk[j].getAntNoder() >= self.npr:
                self._rk.append(Rack())
                self._rk[-1].settInn(node)


	## Beregner totalt antall prosessorer i hele regneklyngen
	# @return totalt antall prosessorer
    def antProsessorer(self):
        antall = 0
        for i in range(len(self._rk)): 
            antall += self._rk[i].antProsessorer()
        return antall

	## Beregner antall noder i regneklyngen med minne over angitt grense
	# @param paakrevdMinne hvor mye minne skal noder som telles med ha
	# @return antall noder med tilstrekkelig minne
    def noderMedNokMinne(self, paakrevdMinne):
        antall = 0
        for i in range(len(self._rk)):
            antall += self._rk[i].noderMedNokMinne(paakrevdMinne)
        return antall

	## Henter antall racks i regneklyngen
    def antRacks(self):
        return len(self._rk) # @return antall racks

if __name__ == "__main__":
    rk = Regneklynge(4)
    for i in range(5):
        rk.settInnNode(Node(8+i,4))
    print(rk.antProsessorer())
    print(rk.antRacks())
    print(rk.noderMedNokMinne(10))