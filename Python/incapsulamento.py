x = 1

def Pippo():
    y = 11   # local scope  \  ambito locale
    #print(y)
    global x # non può essere valorizato sulla stessa riga 
    x = "erorre"
    print(x)
 

def Pippo2():   # non setta il valore globale 
    _y = 11      # ambito protected 
    #print(y)
    global x
    x = "login avvenuto"
    print(x)
    

print(x)  
Pippo()
print(x)
Pippo2()
print(x)




# andare a creare un if che faccia scegliere tra due opzioni di metodo che cambiano un valore globale che poi influenzi un menu


class MasterD:
    _nomescuola = "MasterD"    #il nsotro atributo e protetto 

    
    def __init__( self, name ):
        self._name = name
        
    @property    
    def name(self):
        return self._name
    
    @name.setter 
    def name(self,newname):
         self._name = newname
         
x = MasterD("mirko")

print( x.name )

print(x._name)

print(x._name)



class NuovaScuola:
    __NomeScuola = "master D"
    
    def __init__( self, name, age ):
        self.__name = name
        self.__age = age
        
    def __scrivi(self):
        print("ciao")


y = NuovaScuola("MKIRKO" , 31)

y._NuovaScuola__scrivi()

