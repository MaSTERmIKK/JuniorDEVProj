DIZIO = {
  "Marca": "Nike",
  "Modello": "air jordan",
  "Anno": 1999
}

print(DIZIO)
print(DIZIO["Marca"])
print(len(DIZIO))    # andiamo a vedere la lunghezza del dizionario



dizzion ={
"nOME" : "Mirko",
"ETà"  :  123,
12  : DIZIO,
"colors": ["red", "white", "blue"]
}

#DIZIO.clear()

DIZIO.keys()    # STAMPIAMO TUTTE LE CHIAVI ELEMENTO SULLA SINISTRA

DIZIO.values()  # STAMPIAMO TUTTI I VALORI ELMENTI SULLA DESTRA

dizzion(DIZIO["Marca"])

dizzion["ETà"] = "21"   # adding

dizzion.update({"color": "21"})  # umpate o aggiunta ggiornata

dizzion.pop("model")   # rimozione mirata


# Incapsulamento in Python
class Facciata:
    def __init__(self):
        self.__colore = "verde"

    def colora(self):
        print("La facciata è di colore {}".format(self.__colore))

    def impostaColore(self, variante):
        self.__colore = variante

    def dimm (self):
       if( i == False ):
        i = 10 
       else:
        i - 1


# istanza di classe
x = Facciata()
x.colora()

# modifica del colore
x.__colore = "rosso"
x.colora()

# funzione setter
x.impostaColore("rosso")
x.colora()


# Polimorfismo in Python
class Persiano:

    def miagola(self):
        print("Il mio persiano miagola")
    
    def graffia(self):
        print("Il mio persiano non graffia")

    lista = []
    mirko = 1

    def unico ():
        i = "mirko"
        print(i)

class Siamese:

    def miagola(self):
        print("Il mio siamese non miagola")
    
    def graffia(self):
        print("Il mio siamese graffia")

# Metodo comune
def evento(self):
    self.miagola()

# istanza oggetto
tyson = Persiano()
foreman = Siamese()

# passaggio oggetto all'metodo comune
evento(tyson)
evento(foreman)

Persiano.unico()
Persiano.lista.append(Persiano.unico())