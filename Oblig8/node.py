

class Node(object):
    ## Oppretter en node med gitt minne-storrelse og antall prosessorer
    def __init__(self, minne, antPros):
        self._minne = minne  # @param minne GB minne i den nye noden
        self._antPros = antPros  # @param antPros antall prosessorer i den nye noden

	## Henter antall prosessorer i noden
    def antProsessorer(self):
        return self._antPros  # @return antall prosessorer i noden

    ## Sjekker om noden har tilstrekkelig minne for et program
    def nokMinne(self, paakrevdMinne):  
        if self._minne >= paakrevdMinne:  # @param paakrevdMinne GB minne som kreves for programmet
            return True #  @return True hvis noden har minst saa mye minne
        else:
            return False

if __name__ == "__main__":
    node = Node(8,4)
    print(node.antProsessorer())
    print(node.nokMinne(16))
    print(node.nokMinne(8))