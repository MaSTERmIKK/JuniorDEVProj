# Incapsulamento in Python
# class NuovaCasa:
    
#     def __init__(self):
#         self.__colore = "verde"

#     def colora(self):
#         print("La Nuova Casa è di colore {}".format(self.__colore))

#     def impostaColore(self, variante):      
#         self.__colore = variante

# # istanza di classe
# x = NuovaCasa()
# x.colora()

# # modifica del colore
# x.__colore = "rosso"
# x.colora()

# # funzione setter
# x.impostaColore("rosso")
# x.colora()




#---------------------------------------------------

class MasterD:
    def __init__(self, age = 0):
         self.__age = age
      
    # getter method
    def get_age(self):
        return self.__age
      
    # setter method
    def set_age(self, x):
        self.__age = x
  
raj = MasterD()
  
# setting the age using setter
raj.set_age(21)
  
# retrieving age using getter
print(raj.get_age())
  
raj.set_age(29)

print(raj.get_age())
  