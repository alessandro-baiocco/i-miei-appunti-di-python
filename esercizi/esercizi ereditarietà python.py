import math

# 🍰 Esercizio 1
# Scrivere una classe Veicolo che abbia le seguenti proprietà: marca, modello e anno. 
# Aggiungi poi i metodi accellera e frena. 
# Creare poi una classe Auto che eredita da Veicolo ma aggiunge la proprietà colore ed il metodo cambia_colore().
class Veicolo:
    def __init__(self ,marca , modello , anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.velocità = 0
    def accelera(self , n):
        if(self.velocità + n < 100):
            self.velocità += n 
            print("sto accelerando di " , n)
        else:
            print("non posso andare più veloce di così")
    def rallenta(self , n):
        if(self.velocità - n <= 0):
            print("sono fermo")
        else:
            self.velocità - n
            print("sto rallentando di " , n)
    def __str__(self):
        print("marca : " + self.marca + ", modello : " + self.modello + ", anno : " , self.anno)
            
class Macchina(Veicolo):
    def __init__(self , marca , modello , anno , colore):
        super().__init__(marca , modello , anno)
        self.colore = colore
    def cambia_colore(self, str):
        self.colore = str
        print("ho cambiato colore in " + str)

            

macchina1 = Macchina("audi" , "boh" , 1990 , "rossa")   
macchina1.accelera(40)  
print(macchina1.velocità)
macchina1.rallenta(20) 
print(macchina1.velocità)
macchina1.cambia_colore("blu") 
print(macchina1.colore)

        



print("-------------------------------------------------------------------")
# 🍰 Esercizio 2
# Modifica la classe Auto in modo che erediti anche il metodo __str__() 
# dalla classe Veicolo, in modo da stampare le informazioni sull’auto in questo formato: 
# “Marca: Ferrari, Modello: Enzo, Anno: 2004, Colore: Rosso”.
class Macchina2(Veicolo):
    def __init__(self , marca , modello , anno , colore):
        super().__init__(marca , modello , anno)
        self.colore = colore
    def cambia_colore(self, str):
        self.colore = str
        print("ho cambiato colore in " + str)
    def __str__(self):
        print("marca : " + self.marca + ", modello : " + self.modello + ", anno : " , self.anno , ", colore : " + self.colore )
        
macchina2 = Macchina2("audi" , "boh" , 1990 , "rossa")

macchina2.__str__()



print("-------------------------------------------------------------------")
# 🍰 Esercizio 3
# Scrivi una classe Forma che abbia un metodo area() che calcoli l’area della forma. 
# Poi crea le classi Quadrato e Cerchio che ereditino dalla classe Forma e che implementino il metodo area() 
# in modo appropriato per ogni forma. 
# Utilizza le classi create per creare un quadrato e un cerchio, quindi stampa l’area di ognuno di essi.



pGreco = math.pi
print(pGreco)
class Forma:
    def __init__(self , lunghezza , altezza):
        self.lunghezza = lunghezza
        self.altezza = altezza
    def area(self):
        print("l'area è : " , self.lunghezza * self.altezza / 2)
        



class Cerchio(Forma):
    def __init__(self , raggio):
        self.raggio = raggio
    def area(self):
        print("l'area è " , math.pow(self.raggio , 2) * pGreco)
        
cerchio1 = Cerchio(30)
cerchio1.area()

class Quadrato(Forma):
    def __init__(self , lunghezza , altezza):
        super().__init__(lunghezza , altezza)
    def area(self):
        print("l'area è : " , self.lunghezza * self.altezza)
        
quadrato = Quadrato(20 , 20)

quadrato.area()
        




