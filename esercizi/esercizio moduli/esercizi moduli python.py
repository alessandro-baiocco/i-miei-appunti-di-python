#||----------------------------------------------------------------------------------------||
#||----------------------------------------------------------------------------------------||
#|| documentazione presa da qui --> https://codegrind.it/esercizi/python/moduli            ||
#||----------------------------------------------------------------------------------------||
#||----------------------------------------------------------------------------------------||



print("-------------------------------------------------------------------------------------------")
# Esercizio 1
# Importa il modulo math e calcola la radice quadrata di 16.
import math

print(math.sqrt(16))



print("-------------------------------------------------------------------------------------------")
# Esercizio 2
# Importa il modulo random e genera un numero casuale compreso tra 1 e 10..
import random

print(random.randint(1 , 10))


print("-------------------------------------------------------------------------------------------")
# Esercizio 3
# Crea un nuovo file Python chiamato mio_modulo.py e definisci una funzione chiamata somma che prende 
# due argomenti e restituisce la loro somma. 
# Poi importa il modulo nel tuo programma principale e usa la funzione somma.
import mio_modulo as my

print(my.somma(3 , 4))



print("-------------------------------------------------------------------------------------------")
# Esercizio 4
# Crea un nuovo file Python chiamato altro_modulo.py e 
# definisci una variabile chiamata lista_numeri che contiene una lista di numeri interi. 
# Poi importa il modulo nel tuo programma principale e stampa la lista.
import altro_modulo as my2

print(my2.listaNumeriInteri)

print("-------------------------------------------------------------------------------------------")
# Esercizio 5
# Importa il modulo os e stampa la directory di lavoro corrente.
import os

print(os.getcwd())


print("-------------------------------------------------------------------------------------------")
# Esercizio 6
# Importa il modulo datetime e stampa la data e l'ora corrente.
import datetime

now = datetime.datetime.now()
print(now)


print("-------------------------------------------------------------------------------------------")
# Esercizio 7
# Crea un nuovo file Python chiamato esempio_pacchetto.py e mettilo in una cartella chiamata mio_pacchetto. 
# All'interno di esempio_pacchetto.py, importa il modulo mio_modulo dal primo esercizio e usa la funzione somma.
# Poi importa il pacchetto nel tuo programma principale e usa la funzione somma.
import mio_pacchetto.esempio_pacchetto as mypack
print(mypack.mio_modulo.somma(8 , 9))


print("-------------------------------------------------------------------------------------------")
# Esercizio 8
# Importa il modulo csv e apri il file dati.csv 
# che contiene una tabella di dati separati da virgola. Poi leggi il contenuto del file e stampalo.

# import csv 

# with open('dati.csv', 'r') as file:
#     lettore = csv.reader(file)
#     for riga in lettore:
#         print(riga)




print("-------------------------------------------------------------------------------------------")
# Esercizio 9
# Importa il modulo json e crea un dizionario con alcune chiavi e valori. 
# Poi serializza il dizionario in formato JSON e stampalo.

import json as js

myDict = {"nome" : "franco" , "cognome" : "rossi" , "eta" : 21}
myJson = js.dumps(myDict)

print(myJson)


