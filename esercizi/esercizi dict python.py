#||------------------------------------------------------------------------------------||
#||------------------------------------------------------------------------------------||
#|| documentazione presa da qui --> https://codegrind.it/esercizi/python/dict          ||
#||------------------------------------------------------------------------------------||
#||------------------------------------------------------------------------------------||



print("------------------------------------------------------------------------")
# 🍰 Esercizio 1
# Creare un dizionario vuoto e assegnarlo a una variabile.
emptyDict = {}

print(emptyDict)


print("------------------------------------------------------------------------")
# 🍰 Esercizio 2
# Creare un dizionario con le seguenti chiavi e valori: "nome" : "Mario", "cognome" : "Rossi", "età" : 30.
dict1 = {
    "nome" : "mario" , 
    "cognome" : "rossi" , 
    "eta"  : 30
    }
print(dict1)


print("------------------------------------------------------------------------")
# 🍰 Esercizio 3
# Accedere al valore dell'elemento con chiave "età" del dizionario precedente.

print(dict1["eta"])

print("------------------------------------------------------------------------")
# 🍰 Esercizio 4
# Aggiungere un nuovo elemento "email" con valore "mario.rossi@email.com" al dizionario precedente.

dict1["email"] = "mario.rossi@email.com"
print(dict1)

print("------------------------------------------------------------------------")
# 🍰 Esercizio 5
# Rimuovere l'elemento con chiave "cognome" dal dizionario precedente.
dict1.pop("cognome")
print(dict1)

print("------------------------------------------------------------------------")
# 🍰 Esercizio 6
# Creare una nuova lista che contenga solo le chiavi del dizionario precedente.

list1 = dict1.keys()
print(list1)

print("------------------------------------------------------------------------")
# 🍰 Esercizio 7
# Creare una nuova lista che contenga solo i valori del dizionario precedente.
list2 = dict1.values()
print(list2)
print("------------------------------------------------------------------------")
# 🍰 Esercizio 8
# Aggiornare il valore dell'elemento con chiave "età" del dizionario precedente a 35.

dict1["eta"] = 35
print(dict1["eta"])

print("------------------------------------------------------------------------")
# 🍰 Esercizio 9
# Contare il numero di elementi nel dizionario precedente.

print(len(dict1))