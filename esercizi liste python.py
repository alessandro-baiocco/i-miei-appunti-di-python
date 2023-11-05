#||----------------------------------------------------------------------------------------||
#||----------------------------------------------------------------------------------------||
#|| documentazione presa da qui --> https://codegrind.it/esercizi/python/liste             ||
#||----------------------------------------------------------------------------------------||
#||----------------------------------------------------------------------------------------||

# altrivalori = [ 30 , 27 , 59 , 76]
# città = list(("milano" , "roma" , "napoli"))
# valori2 = [95 , 82 , 659 , 8081 ,73521098]

# 🍰 Esercizio 1
# Creare una lista vuota e assegnarla a una variabile.

emptyList = []
print(emptyList)

print("---------------------------------------------------------------------------")
# 🍰 Esercizio 2
# Creare una lista di numeri interi da 1 a 5 e assegnarla a una variabile.

valori = [4 , 3 , 5 , 4 , 1]
print(valori)


print("---------------------------------------------------------------------------")
# 🍰 Esercizio 3
# Accedere all'elemento con indice 2 della lista precedente.

print(valori[2])

print("---------------------------------------------------------------------------")
# 🍰 Esercizio 4
# Aggiungere un nuovo elemento "6" alla lista precedente.

valori.append(6)
print(valori)

print("---------------------------------------------------------------------------")
# 🍰 Esercizio 5
# Rimuovere l'elemento con indice 3 dalla lista precedente.

del valori[3]
print(valori)

print("---------------------------------------------------------------------------")
# 🍰 Esercizio 6
# Creare una nuova lista che contenga solo i primi tre elementi della lista precedente.

valori2 = valori[0:3]
print(valori2)



print("---------------------------------------------------------------------------")
# 🍰 Esercizio 7
# Creare una nuova lista che contenga gli elementi con indici dispari della lista precedente.
valori3 = []

i = 0
while i < len(valori):
    if i % 2 != 0:
        valori3.append(valori[i])
    i += 1
    
print(valori3)
    

print("---------------------------------------------------------------------------")
# 🍰 Esercizio 8
# Ordinare la lista precedente in ordine decrescente.
valori.sort(reverse= True)
print(valori)

print("---------------------------------------------------------------------------")
# 🍰 Esercizio 9
# Contare quante volte l'elemento "2" appare nella lista precedente.
valori.append(2)
valori.append(2)
valori.append(2)

print(valori)
count = 0
for num in valori:
    if num == 2:
        count += 1
        print("counter aumentato di uno")
print("il numero 2 è presente " , count , " volte")
