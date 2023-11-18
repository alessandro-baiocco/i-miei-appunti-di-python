
#||------------------------------------------------------------------------------------||
#||------------------------------------------------------------------------------------||
#|| documentazione presa da qui --> https://codegrind.it/esercizi/python/set           ||
#||------------------------------------------------------------------------------------||
#||------------------------------------------------------------------------------------||


# 🍰 Esercizio 1
# Creare un set vuoto e assegnarlo a una variabile.
emptySet = set()
print(emptySet)



print("-----------------------------------------------------------------------------")
# 🍰 Esercizio 2
# Creare un set contenente i seguenti elementi: "mela", "banana", "kiwi", "mela".

prima = {"mela" , "banana" , "kiwi" , "mela"}

print(prima) #il set non accetta duplicati


print("-----------------------------------------------------------------------------")
# 🍰 Esercizio 3
# Aggiungere l'elemento "pesca" al set precedente.

prima.add("pesca")
print(prima)

print("-----------------------------------------------------------------------------")
# 🍰 Esercizio 4
# Rimuovere l'elemento "mela" dal set precedente.

prima.remove("mela")
print(prima)
print("-----------------------------------------------------------------------------")
# 🍰 Esercizio 5
# Verificare se l'elemento "ananas" è presente nel set precedente.
for ele in prima:
    if(ele == "ananas"):
        print("ananas è presente")


print("-----------------------------------------------------------------------------")
# 🍰 Esercizio 6
# Creare un nuovo set contenente gli elementi "banana", "kiwi" e "arancia".

seconda = {"banana" , "kiwi" , "arancia"}
print(seconda)


print("-----------------------------------------------------------------------------")
# 🍰 Esercizio 7
# Creare un set contenente i numeri interi da 1 a 5 ricavati da un range().

numberset = set(range(1 ,6))
print(numberset)
print("-----------------------------------------------------------------------------")
# 🍰 Esercizio 8 (difficile)
# Creare un nuovo set contenente i numeri pari del set precedente.
numberset2 = set()
for num in numberset:
    if num % 2 != 0:
        numberset2.add(num)
        
        
numberset3 = numberset2.symmetric_difference(numberset)
        

print(numberset3)