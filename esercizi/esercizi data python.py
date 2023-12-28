#||------------------------------------------------------------------------------------||
#||------------------------------------------------------------------------------------||
#|| documentazione presa da qui --> https://codegrind.it/esercizi/python/date          ||
#||------------------------------------------------------------------------------------||
#||------------------------------------------------------------------------------------||

import datetime
# 🍰 Esercizio 1
# Scrivi un programma che stampa la data e l'ora corrente.
ora = datetime.datetime.now()
print(ora)


print("------------------------------------------------------------------------------------------------------------")
# 🍰 Esercizio 2
# Scrivi un programma che prende in input una data in formato "gg/mm/aaaa" e stampa il nome del mese corrispondente.
data1 = input("Inserisci una data (gg/mm/aaaa): ")
data1 = datetime.datetime.strptime(data, "%d/%m/%Y")

nomeMese = data1.strftime("%B")
print("Il nome del mese corrispondente è:", nomeMese)

print("------------------------------------------------------------------------------------------------------------")
# 🍰 Esercizio 3
# Scrivi un programma che prende in input due date e calcola la differenza in giorni tra le due.
print("------------------------------------------------------------------------------------------------------------")
# 🍰 Esercizio 4
# Scrivi un programma che prende in input una data e un numero di giorni, e calcola la data che viene dopo quella data del numero di giorni specificato.
print("------------------------------------------------------------------------------------------------------------")
# 🍰 Esercizio 5
# Scrivi un programma che stampa tutti i giorni di un determinato mese e anno.
print("------------------------------------------------------------------------------------------------------------")
# 🍰 Esercizio 6
# Scrivi un programma che prende in input una data in formato "gg/mm/aaaa" e verifica se l'anno è bisestile o meno.
print("------------------------------------------------------------------------------------------------------------")
# 🍰 Esercizio 7
# Scrivi un programma che prende in input due date e stampa tutte le date comprese tra le due (inclusi i bordi).
print("------------------------------------------------------------------------------------------------------------")
# 🍰 Esercizio 8
# Scrivi una funzione che prenda in input due date come oggetti datetime e restituisca il numero di giorni trascorsi tra di esse.
print("------------------------------------------------------------------------------------------------------------")
# 🍰 Esercizio 9
# Scrivi una funzione che prenda in input una data come oggetto datetime e restituisca il giorno della settimana corrispondente come stringa.
print("------------------------------------------------------------------------------------------------------------")
# 🍰 Esercizio 10
# Scrivi una funzione che prenda in input una data come oggetto datetime e restituisca il numero della settimana corrispondente nell'anno.
print("------------------------------------------------------------------------------------------------------------")