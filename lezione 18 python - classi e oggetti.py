# 18 classi e oggetti
# 1 - introduzione alla programmazione ad oggetti
# 2 - creare una classe
# 3 - creare un oggetto, cos'e un'istanza (instance)
# 4 - il costruttore
# 5 - i metodi
# 6 - il parametro self
# 7 - modificare , eliminare proprietà di un oggetto 
# 8 - eliminare oggetto


print("---------------------classe----------------------")
class Luca:
    nome = "luca"
    cognome = "rossi"
    
personaPrima = Luca()
personaSeconda = Luca()
print(personaPrima.nome, personaSeconda.cognome)


print("----------------------costruttore----------------")

class Persona:
    def __init__(self , nome , cognome):
        self.nome = nome
        self.cognome = cognome
        
        
PersonaTerza = Persona("carlo" , "magno")
PersonaQuarta = Persona("marco" , "verdi")
print(PersonaTerza.nome, PersonaQuarta.cognome)


print("---------------------------metodi-------------------------------")


class Persona2:
    def __init__(self , nome , cognome):
        self.nome = nome
        self.cognome = cognome
    def saluta(self):
        print("ciao sono " + self.nome + " " + self.cognome)
    def somma(self , num1 , num2):
        print(num1 + num2)
    
        
personaQuinta = Persona2("coso" , "rossi")

personaQuinta.saluta()
personaQuinta.somma(3,8)

print("---------------------------------elimina----------------------------")

personaPrima.nome = "carolina"
print(personaPrima.nome) 
  
del PersonaTerza.nome

try:
    print(PersonaTerza.nome)
except:
    print("personaTerza.nome non esiste più")
    
    
del personaPrima

try:
    print(PersonaPrima)
except:
    print("personaPrima non esiste più")







