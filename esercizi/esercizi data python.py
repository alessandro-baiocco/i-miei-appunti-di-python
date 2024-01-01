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
data1 = datetime.datetime.strptime(data1, "%d/%m/%Y")

nomeMese = data1.strftime("%B")
print("Il nome del mese corrispondente è:", nomeMese)

print("------------------------------------------------------------------------------------------------------------")
# 🍰 Esercizio 3
# Scrivi un programma che prende in input due date e calcola la differenza in giorni tra le due.

data2 = input("Inserisci una data (gg/mm/aaaa): ")
data2 = datetime.datetime.strptime(data2, "%d/%m/%Y")
data3 = input("Inserisci una data (gg/mm/aaaa): ")
data3 = datetime.datetime.strptime(data3, "%d/%m/%Y")

differenza = data2 - data3
print("la differenza in giorni e di : ", differenza)


print("------------------------------------------------------------------------------------------------------------")
# 🍰 Esercizio 4
# Scrivi un programma che prende in input una data e un numero di giorni, e calcola la data che viene dopo quella data del numero di giorni specificato.

data4 = input("Inserisci una data (gg/mm/aaaa): ")
numeroDiGiorni = int(input("Inserisci un numero di giorni "))
data4 = datetime.datetime.strptime(data4, "%d/%m/%Y")
print(data4 + datetime.timedelta(days= numeroDiGiorni))


print("------------------------------------------------------------------------------------------------------------")
# 🍰 Esercizio 5
# Scrivi un programma che stampa tutti i giorni di un determinato mese e anno.

import calendar

anno = int(input("Inserisci l'anno: "))
mese = int(input("Inserisci il mese (1-12): "))

cal = calendar.monthcalendar(anno, mese)
for settimana in cal:
    for giorno in settimana:
        if giorno != 0:
            print(giorno)


print("------------------------------------------------------------------------------------------------------------")
# 🍰 Esercizio 6
# Scrivi un programma che prende in input una data in formato "gg/mm/aaaa" e verifica se l'anno è bisestile o meno.

data5 = input("Inserisci una data (gg/mm/aaaa): ")
data5 = datetime.datetime.strptime(data5, "%d/%m/%Y")


if calendar.isleap(data5.year):
    print("l'anno è bisestile")
else:
    print("l'anno non è bisestile")


print("------------------------------------------------------------------------------------------------------------")
# 🍰 Esercizio 7
# Scrivi un programma che prende in input due date e stampa tutte le date comprese tra le due (inclusi i bordi).

data6 = input("Inserisci una data (gg/mm/aaaa): ")
data6 = datetime.datetime.strptime(data6, "%d/%m/%Y")
data7 = input("Inserisci una data (gg/mm/aaaa): ")
data7 = datetime.datetime.strptime(data7, "%d/%m/%Y")

delta = datetime.timedelta(days=1)

while data6 <= data7:
    print(data6.strftime("%d/%m/%Y"))
    data6 += delta

print("------------------------------------------------------------------------------------------------------------")
# 🍰 Esercizio 8
# Scrivi una funzione che prenda in input due date come oggetti datetime e restituisca il numero di giorni trascorsi tra di esse.

data8 = input("Inserisci una data (gg/mm/aaaa): ")
data8 = datetime.datetime.strptime(data8, "%d/%m/%Y")
data9 = input("Inserisci una data (gg/mm/aaaa): ")
data9 = datetime.datetime.strptime(data9, "%d/%m/%Y")

delta2 = datetime.timedelta(days=1)
numeroDiGiorni = 0

while data8 <= data9:
    numeroDiGiorni += 1
    data8 += delta2
print(numeroDiGiorni)

print("------------------------------------------------------------------------------------------------------------")
# 🍰 Esercizio 9
# Scrivi una funzione che prenda in input una data come oggetto datetime e restituisca il giorno della settimana corrispondente come stringa.

data10 = input("Inserisci una data (gg/mm/aaaa): ")
data10 = datetime.datetime.strptime(data10, "%d/%m/%Y")

giornoDellaSettimana = data10.strftime("%A")

print(giornoDellaSettimana)


print("------------------------------------------------------------------------------------------------------------")
# 🍰 Esercizio 10
# Scrivi una funzione che prenda in input una data come oggetto datetime e restituisca il numero della settimana corrispondente nell'anno.

data11 = input("Inserisci una data (gg/mm/aaaa): ")
data11 = datetime.datetime.strptime(data11, "%d/%m/%Y")

numeroDellaSettimana = data11.strftime("%W")

print(numeroDellaSettimana)


print("------------------------------------------------------------------------------------------------------------")