

class Persona :
   
    tipo = "umano"                     # attributi 
    
    # Metodi
    
    def __init__(self, Nome, Eta):     # costruttore 
        self.Nome = Nome
        self.Eta = Eta
    
    def MasterD(self):                 # Metodo della classe
        print( " ciao sono " + self.Nome + " " + self.tipo)
        
X = Persona("Mirko", 99)
X.MasterD()

class Alievo(Persona):
    
    def __init__(self, Nome, Eta, grado):
        super().__init__(Nome, Eta)
        self.grado = grado
    
    tipo = "gatto"
    
    def MasterD(self):                 # Metodo della classe
        print( " ciao sono " + self.Nome + " " + self.tipo + " " + self.grado)

Y = Alievo("Marius", 23, "TERZO DAN")
Y.MasterD()


# creare una discendenza. Create un padre chimato Uno, che di figlio in figlio fino al 10# aggiunga un valore, un attributo
# l'ultimo dovrà stamparli tutti tramite un metodo fatto nel padre e derivato 

class Uno():
    
    Numero = 1
    
    def Scrivicose(self) :
        print(self.Numero)    


class Due(Uno) :
    Numero2 = 2
    Numero = 2
    
    def Scrivicose(self):
        print(self.Numero2)
        return super().Scrivicose()
    
    
    
#### INNER CLASS

class iNNERPROVA():
 
    # constructore 
 
    def __init__(self):
 
        # object attributi
        self.course = "Campus Master D"
        self.duration = "quanto vuoi"
        
        #crrea la classe interna
        self.inner = self.corsoavanzato()
 
 
    def show(self):
 
        print("Corso:", self.course)
        print("Durata:", self.duration)
    
    
    class corsoavanzato: 
        
       def __init__(self) -> None:
           print("ciao")
           
       def MasterdAvanzato():
           print ("avanzato")
           
           
    class   corsofinale:
        
        finirò = True
        
        def __init__():
            print("ciao finale")
        
        def finito(self):
            if( self.finirò != True  ):
                print ("hai finito")
                
        class attestato:
             print("ti sei classificato 3")
             
             def esci ():
                 print("addio e buon lavoro")                
                

padreinterno = iNNERPROVA()

figliointerno = padreinterno.corsoavanzato

figliointerno.MasterdAvanzato()

figliodueinterno = padreinterno.corsofinale

figliodueinterno.finito()

figliotre = figliodueinterno.attestato()

figliotre.esci()
