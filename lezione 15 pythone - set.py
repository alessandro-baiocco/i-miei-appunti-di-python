# 15 set
# 1 - collezioni di dati non ordinate, non indicizzate , non modificabili e non permettono duplicati
# 2 - creare un set, normale e mischiata 
# 3 - vediamo len() , type() e tuple()

# 4 - accedere agli elementi con loop
# 5 - modificare elementi non è possibile , possiamo solo aggiungere e rimuovere
# 6 - aggiungere con add() e update()
# 7 - rimuovere elementi con remove(),discard() , pop() , clear() , del
# 8 - unire con union() e update, intersection_update(), intersection() , symmetric_defference_update() , symmetric_difference()


prima = {"milano" , "roma" , "napoli"}
seconda = {"pippo" , True , 45}
terza = {"franco" ,}
quarta = {"coso" , "cosa" , "matilde" , "sempronio" , "caio" , "roma"}

print("--------------------------------type-------------------------------")
print(type(terza))
print("--------------------------------len-------------------------------")
print(len(prima))
print("--------------------------------list-------------------------------")
print(list(prima))
print("--------------------------------accedere-------------------------------")

# print(prima[0]) questa sintassi da errore perchè i set non hanno indici
print(quarta) # ogni avvio del programma l'ordine è sempre diverso
print("------------------------------add e update--------------------------------------")
prima.add("boh")
print(prima)
prima.update(seconda)
print(prima)
print("--------------------------------remove-------------------------------------")

prima.discard(45) # discard rimuove un elemento dal set ma non da errore se l'elemento non esiste
try :
    prima.remove(45)#se si rimuove un elemento non esistente da errore
except : 
    print("errore")
    
print(prima)

prima.pop() # rimuove un elemento casuale visto che i set non hanno un'ordine
print(prima)


prima.clear() # per pulire il set
print(prima)

try :
    del prima #per eliminare completamente un set
    print(prima)
except : 
    print("errore")
    
print("-------------------------union--------------------------------------")

primo = seconda.union(quarta) #crea un nuovo set ma senza metter elementi duplicati
print(primo)

seconda.update(quarta) # unisce 2 set ma senza metter elementi duplicati
print(seconda)

print("------------------------interception e symmetric----------------------")

terzo = primo.intersection(quarta) #restituisce solo gli elementi che hanno in comune creando un nuovo set
print(terzo) 

primo.intersection_update(quarta) #restituisce solo gli elementi che hanno in comune modificando il set
print(primo)


terzo = primo.symmetric_difference(quarta) #restituisce solo gli elementi che non hanno in comune creando un nuovo set
print(terzo) 

primo.symmetric_difference_update(quarta) #restituisce solo gli elementi non che hanno in comune modificando il set
print(primo)


