import math
#||------------------------------------------------------------------------------------||
#||------------------------------------------------------------------------------------||
#|| documentazione presa da qui --> https://codegrind.it/esercizi/python/tuple         ||
#||------------------------------------------------------------------------------------||
#||------------------------------------------------------------------------------------||


# 🍰 Esercizio 1
# Creare una tupla vuota e assegnarla a una variabile.

emptyTupla = ()
print(emptyTupla)

print("--------------------------------------------------------------")
# 🍰 Esercizio 2
# Creare una tupla con i seguenti elementi: "mela", "banana", "kiwi".

customTupla = ("mela" , "banana" , "kiwi")
print(customTupla)

print("--------------------------------------------------------------")
# 🍰 Esercizio 3
# Accedere all'elemento "banana" della tupla precedente.
print(customTupla[1])

print("--------------------------------------------------------------")
# 🍰 Esercizio 4
# Creare una nuova tupla che contenga solo i primi due elementi della tupla precedente.
customTupla2 = customTupla[0:2]

print(customTupla2)


print("--------------------------------------------------------------")
# 🍰 Esercizio 5
# Verificare se l'elemento "ananas" è presente nella tupla precedente.
if "ananas" in customTupla:
    print("ananas è presente")
else:
    print("non c'e nessun ananas")


print("--------------------------------------------------------------")
# 🍰 Esercizio 6
# Creare una nuova tupla concatenando la tupla precedente con la tupla ("pesca", "arancia").
customTupla3 = ("pesca", "arancia")
emptyTupla = customTupla + customTupla3
print(emptyTupla)


print("--------------------------------------------------------------")
# 🍰 Esercizio 7
# Verificare la lunghezza della tupla precedente.

print("emptyTupla è lunga",len(emptyTupla), "elementi")

print("--------------------------------------------------------------")
# 🍰 Esercizio 8
# Creare una tupla contenente i numeri interi da 1 a 5.
numberTupla = (1 , 2 , 3 , 4 , 5)
print(numberTupla)
print("--------------------------------------------------------------")
# 🍰 Esercizio 9 (difficile)
# Creare una tupla contenente il quadrato dei numeri interi da 1 a 5.

powTupla = (math.pow(1, 2) , math.pow(2, 2) ,math.pow(3, 2) ,math.pow(4, 2) ,math.pow(5, 2))
print(powTupla)

print("--------------------------------------------------------------")
# 🍰 Esercizio 10
# Contare il numero di occorrenze dell'elemento "mela" nella tupla precedente.

count = 0
for str in emptyTupla:
    if str == "mela":
        count += 1
        print("counter aumentato di 1")
    
print("in emptyTupla mela appare", count , "volte/a")

print("--------------------------------------------------------------")