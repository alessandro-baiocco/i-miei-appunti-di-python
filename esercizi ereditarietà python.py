# 🍰 Esercizio 1
# Scrivere una classe Veicolo che abbia le seguenti proprietà: marca, modello e anno. 
# Aggiungi poi i metodi accellera e frena. 
# Creare poi una classe Auto che eredita da Veicolo ma aggiunge la proprietà colore ed il metodo cambia_colore().
class Veicolo:
    def __init__(marca , modello , anno):
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
            
    
        
        



print("-------------------------------------------------------------------")
# 🍰 Esercizio 2
# Modifica la classe Auto in modo che erediti anche il metodo __str__() dalla classe Veicolo, in modo da stampare le informazioni sull’auto in questo formato: “Marca: Ferrari, Modello: Enzo, Anno: 2004, Colore: Rosso”.
print("-------------------------------------------------------------------")
# 🍰 Esercizio 3
# Scrivi una classe Forma che abbia un metodo area() che calcoli l’area della forma. Poi crea le classi Quadrato e Cerchio che ereditino dalla classe Forma e che implementino il metodo area() in modo appropriato per ogni forma. Utilizza le classi create per creare un quadrato e un cerchio, quindi stampa l’area di ognuno di essi.
