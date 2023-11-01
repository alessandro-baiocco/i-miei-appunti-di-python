# 19 ereditarietà
# 1 - cose l'ereditarità
# 2 - creare una classe figlia
# 3 - il costruttore della classe figlia
# 4 - la funzione super
# 5 - proprietà esclusive della classe figlia
# 6 - i metodi e l'overriding

class Persona:
    def __init__(self , nome , cognome):
        self.nome = nome
        self.cognome = cognome 
    def saluta(self):
        print("ciao sono " + self.nome + " " + self.cognome)
        
        
class Insegnante(Persona): # in questo modo possiamo estendere una classe
    pass 


        
class Studente(Persona): 
    def __init__(self , nome , cognome , materia): #esempio di override
        super().__init__(nome , cognome) 
        self.materia = materia


insegnante1 = Insegnante("luca" , "rossi")

print(insegnante1.saluta())

studente1 = Studente("coso" , "rossi" , "matematica")

print(studente1.materia)