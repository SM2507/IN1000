from node import Node

class Rack(object):
    ## oppretter et rack der det senere kan plasseres noder
    def __init__(self):
        self._rack = []

    ## Plasserer en ny node inn i racket
    #  @param node noden som skal plasseres inn
    def settInn(self, node):
        self._rack.append(node)

    ## Henter antall noder i racket
    # @return antall noder
    def getAntNoder(self):
        antall = 0
        for i in self._rack:
            if isinstance(i,Node):
                antall += 1
        return antall

    ## Beregner sammenlagt antall prosessorer i nodene i et rack
    def antProsessorer(self):
        antall = 0
        for i in self._rack:
            antall += i.antProsessorer()
        return antall  # @return antall prosessorer

    ## Beregner antall noder i racket med minne over gitt grense
    def noderMedNokMinne(self, paakrevdMinne):
        antall = 0
        for i in self._rack:
            if i.nokMinne(paakrevdMinne):  # @param paakrevdMinne antall GB minne som kreves
                antall += 1
        return antall  # @return antall noder med tilstrekkelig minne

if __name__ == "__main__":
    quack = Rack()
    print(quack.getAntNoder())
    quack.settInn(Node(8,8))
    quack.settInn(Node(6,8))
    print(quack.getAntNoder())
    print(quack.antProsessorer())
    print(quack.noderMedNokMinne(7))