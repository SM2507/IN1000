
class Celle(object):  #  Lager klassen Celle
    def __init__(self):  # Konstruktøren setter instansvariabler 
        self.status = "doed"
        self.nabo = []  # Ikke beskrevet i oppgaven, men nødvendig for min tolkning av metoden finnNabo

    def settDoed(self):  # Metode setter cellen død
        self.status = "doed"

    def settLevende(self):  # Setter cellen levende
        self.status = "levende"

    def erLevende(self):  # Returnerer True hvis cellen har status levende
        if self.status == "levende":
            return True
        else:
            return False

    def tegn(self):  # Returnerer tegn for levende og døde celler
        if self.erLevende() == True:
            return "O"
        else:
            return "."
    
    

