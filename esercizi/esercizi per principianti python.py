#||----------------------------------------------------------------------------------------||
#||----------------------------------------------------------------------------------------||
#|| documentazione presa da qui --> https://www.programmareinpython.it/esercizi-python/    ||
#||----------------------------------------------------------------------------------------||
#||----------------------------------------------------------------------------------------||




# 🍰 Esercizio 1
# Scrivi un programma che chieda due numeri all'utente tramite la funzione input e mostri il più grande tra i due utilizzando la funzione print.
# Per quanto Python disponga di una funzione max(), siete invitati ad utilizzare le istruzioni istruzioni if, elif ed else per la scrittura dell'algoritmo.

# try:
#     print("inserisci 2 valori")
#     num1Exe1 = int(input())
#     num2Exe1 = int(input())
    
#     def numeroMaggiore(int1 , int2):
#         if int1 > int2:
#             print(int1)
#         else:
#             print(int2)
#     numeroMaggiore(num1Exe1 , num2Exe1)
# except:
#     print("puoi inserire solo numeri interi")
    



print("---------------------------------------------------------------------------")
# 🍰 Esercizio 2
# Scrivi un programma che chieda tre numeri a, b, c all'utente e mostri il più grande tra loro.

# try:
    
#     print("inserisci 3 valori")
#     num1Exe2 = int(input())
#     num2Exe2 = int(input())
#     num3Exe2 = int(input())
    
#     print(max(num1Exe2 , num2Exe2 , num3Exe2))
        
# except:
#     print("puoi inserire solo numeri interi")




print("---------------------------------------------------------------------------")
# 🍰 Esercizio 3
# Scrivi un programma che, data una lista di numeri, fornisca in output il maggiore tra tutti gli elementi della lista.
#p.s. per non abusare della funzione max() utilizzaro un ciclo for

userValuesExe3 = []

# try:
#     print("inserisci tutti i valori che vuoi inserisci 0 per uscire")
#     while True:
#         newValueExe3 = int(input())
#         if newValueExe3 == 0:
#             break
#         else:
#             userValuesExe3.append(newValueExe3)
# except:
#     print("puoi inserire solo numeri")
    
# higherValue = 0
# for num in userValuesExe3:
#     if num > higherValue:
#         higherValue = num

# print("il numero più grande è", higherValue)
    
    


print("---------------------------------------------------------------------------")
# 🍰 Esercizio 4
# Scrivi un programma che chieda all'utente una stringa composta da un solo carattere e dica se si tratta di una vocale oppure no.

vocali = ["a" , "e" , "i" , "o" , "u"]

# print("inserisci una lettera se inserisci una parola verrà presa la prima lettera")
# str1Exe4 = input()
# if str1Exe4[0] in vocali:
#     print("si, è una vocale")
# else:
#     print("no, non è una vocale")





print("---------------------------------------------------------------------------")
# 🍰 Esercizio 5
# Scrivi un semplice programma che, data una lista di numeri, sommi tra loro tutti gli elementi.
# Suggerimento: anche se esiste la funzione sum() per risolvere l'esercizio potresti usare il ciclo for.

userValuesExe5 = []

# try:
#     print("inserisci tutti i valori che vuoi inserisci 0 per uscire")
#     while True:
#         newValueExe5 = int(input())
#         if newValueExe5 == 0:
#             break
#         else:
#             userValuesExe5.append(newValueExe5)
# except:
#     print("puoi inserire solo numeri")
    
# totalValueExe5 = 0
# for num in userValuesExe5:
#     totalValueExe5 += num

# print("il totale è ", totalValueExe5)


print("---------------------------------------------------------------------------")
# 🍰 Esercizio 6
# Scrivi un programma "moltiplicatore" che, data una lista di numeri, moltiplichi tra loro tutti gli elementi.
userValuesExe6 = []

# try:
#     print("inserisci tutti i valori che vuoi inserisci 0 per uscire")
#     while True:
#         newValueExe6 = int(input())
#         if newValueExe6 == 0:
#             break
#         else:
#             userValuesExe6.append(newValueExe6)
# except:
#     print("puoi inserire solo numeri")
    
# totalValueExe6 = 1
# for num in userValuesExe6:
#     totalValueExe6 *= num
    
# print("il totale è ", totalValueExe6)




print("---------------------------------------------------------------------------")
# 🍰 Esercizio 7
# Scrivi un programma che a partire da un elemento e una lista di elementi dica in output se l'elemento passato sia presente o meno nella lista.
# Qualora l'elemento sia presente nella lista, il programma dovrà comunicarci l'indice dell'elemento tramite il metodo index.
  
# try:
#     val1Exe7 = int(input()) 
#     valuesExe7 = [8 , 6 , 2512 , 1 , 3 , 42 , 51 , 54367 , 24]

#     for x, val in enumerate(valuesExe7):
#         if val == val1Exe7:
#             print(val , "è presente in posizione" , x)
# except:
#     print("puoi inserire solo numeri interi")


    

print("---------------------------------------------------------------------------")
# 🍰 Esercizio 8
# Scrivi una semplice funzione che, data una lista di numeri, fornisca in output un istogramma basato su questi numeri, usando asterischi per disegnarlo.
# Data ad esempio la lista [3, 7, 9, 5], la funzione dovrà produrre questa sequenza:
# ***
# *******
# *********
# *****

intValuesExe8 = [4 , 3 , 7 , 4]
strExe8 = ""
for n in intValuesExe8:
    for x in range(n):
        strExe8 += "*"
    print(strExe8)
    strExe8 = ""

        

print("---------------------------------------------------------------------------")
# 🍰 Esercizio 9
# Scrivi una funzione che restituisca la lunghezza di una stringa o lista passata come parametro. 
# In sostanza, seppur presente, provate a scrivere la nostra versione della funzione len!

# str1Exe9 = input()
# strLengthExe4 = 0

# for letter in str1Exe4:
#     strLengthExe4 += 1
    
# print(strLengthExe4)
    


print("---------------------------------------------------------------------------")
# 🍰 Esercizio 10
# Scrivi una funzione che data in ingresso una lista A contenente n parole, 
# restituisca in output una lista B di interi che rappresentano la lunghezza delle parole contenute in A.
# Questo esercizio può essere risolto anche usando una list comprehension.

wordsExe10 = ["ciao" , "franco" , "coso" , "mario" , "genoveffa"]
wordsLenExe10 = []

for word in wordsExe10:
    wordsLenExe10.append(len(word))
    
print(wordsLenExe10)
    

print("---------------------------------------------------------------------------")
# 🍰 Esercizio 11
# Scrivi una funzione che, data una stringa come parametro, restituisca un dizionario rappresentante la "frequenza di comparsa" di ciascun carattere componente la stringa.
# Per fare un esempio, data una stringa "ababcc", otterremo in risultato {"a": 2, "b": 2, "c": 2}

# str1Exe11 = input()
# dict1Exe11 = {}

# for letter in str1Exe11:
#     if letter in dict1Exe11:
#         dict1Exe11[letter] += 1
#     else:
#         dict1Exe11[letter] = 1

# print(dict1Exe11)
    

print("---------------------------------------------------------------------------")
# 🍰 Esercizio 12
# Scrivi una funzione che, dato in ingresso un valore espresso in metri, 
# mandi in print l'equivalente in miglia terrestri, iarde, piedi e pollici. Come risolverai questo esercizio?

# try:
#     print("inserire un valore in metri")
#     num1Exe12 = int(input())
#     print(num1Exe12, "metri equivale a :" , num1Exe12 / 1609 ,"miglia terrestri")
#     print(num1Exe12, "metri equivale a :" , num1Exe12 * 1.094 ,"iarde")
#     print(num1Exe12, "metri equivale a :" , num1Exe12 * 3.281 ,"piedi")
#     print(num1Exe12, "metri equivale a :" , num1Exe12 * 39,37 ,"miglia terrestri")
# except:
#     print("puoi inserire solo numeri interi")




print("---------------------------------------------------------------------------")
# 🍰 Esercizio 13
# Scrivi una semplice funzione che converta un dato numero di giorni, ore e minuti, passati dall'utente tramite funzione input, in secondi.

# try: 
#     print("inserire numero giorni")
#     daysExe13 = int(input())
#     print("inserire numero di ore")
#     hoursExe13 = int(input())
#     print("inserire numero minuti")
#     minutsExe13 = int(input())
    
#     totalSecondExe13 = 0
#     totalSecondExe13 += (daysExe13 * 86400)
#     totalSecondExe13 += (hoursExe13 * 3600)
#     totalSecondExe13 += (minutsExe13 * 60)
#     print("numero totale di secondi :",totalSecondExe13)
    
# except:
#     print("puoi inserire solo numeri interi")
    

print("---------------------------------------------------------------------------")
# 🍰 Esercizio 14

# Scrivi una funzione che, a scelta dell'utente, calcoli l'area di:
# un cerchio
# un quadrato
# un rettangolo
# un triangolo
# Sentitevi liberi di estendere le potenzialità della funzione quanto meglio credete!


import math 
# try:
#     print("inserire tipo di forma 1 per il cerchio |2 per triangolo | 3 per quadrato | 4 per rettangolo")
#     typeForm = input()
#     if typeForm == "1":
#         print("inserire raggio ")
#         baseForm = int(input())
#     elif typeForm == "2" or typeForm == "3" or typeForm == "4":
#         print("inserire base")
#         baseForm = int(input())
#         print("inserire altezza")
#         heightForm = int(input())
        
#     if typeForm == "1":
#         print("l'area del cerchio è :", math.pi * pow(baseForm , 2))  
#     elif typeForm == "2":
#         print("l'area del triangolo è :", baseForm * heightForm / 2)    
#     elif typeForm == "3" or typeForm == "4":
#         print("l'area è :", baseForm * heightForm) 
#     else:
#         print("forma non trovata")   
        
    
# except:
#     print("hai inserito un valore non valido")




print("---------------------------------------------------------------------------")
# 🍰 Esercizio 15
# Un indirizzo MAC (Media Access Control address) è un indirizzo univoco associato dal produttore, a un chipset per comunicazioni wireless (es WiFi o Bluetooth),
# composto da 6 coppie di cifre esadecimali separate da due punti.
# Un esempio di MAC è 02:FF:A5:F2:55:12.
# Scrivi una funzione genera_mac() che generi degli indirizzi MAC pseudo casuali utilizzando il modulo random.
from random import randint
macAdressChar = ["0" , "1" , "2" , "3" , "4", "5", "6", "7", "8", "9", "A" , "B" , "C" , "D" , "E" , "F"]


def genera_mac():
    macAdress = ""
    for num in range(12):
        randomValue = randint(0 , 15)
        macAdress += macAdressChar[randomValue]
        if (num + 1) %2  == 0 and num != 11:
            macAdress += ":"
    return macAdress
   
   
   
print(genera_mac())
        
    
    


print("---------------------------------------------------------------------------")
# 🍰 Esercizio 16
# Scrivi una funzione che fornisca in output il nome del Sistema Operativo utilizzato con eventuali relative informazioni sulla release corrente.
# Suggerimento: per risolvere questo esercizio potreste dover utilizzare una libreria! ;)

import os 
import platform

def ilMioSO():
    print(os.name)
    print(platform.system())
    print(platform.release())
    
    
ilMioSO()
    


print("---------------------------------------------------------------------------")
# 🍰 Esercizio 17
# Scrivi una funzione che, dato un carattere in ingresso, restituisca in output il codice ASCII associato al carattere passato.
# Anche in questo caso, usare una libreria potrebbe facilitare la risoluzione dell'esercizio!

# charExe17 = input("inserire un carattere:")

# def foundASCII(str):
#     asciiCode = ord(str[0])
#     return asciiCode

# print(foundASCII(charExe17))


print("---------------------------------------------------------------------------")
# 🍰 Esercizio 18
# Un numero perfetto è un numero naturale uguale alla somma dei suoi divisori positivi, 
# escluso sé stesso. Scrivi una funzione che verifichi se un numero è perfetto oppure no.

# num1Exe18=int(input("Enter the number: "))  
# sumExe18=0  
# for i in range(1,num1Exe18):  
#     if (num1Exe18%i==0):  
#         sumExe18=sumExe18+i  
# if(sumExe18==num1Exe18):  
#     print("il numero inserito è perfetto")  
# else:  
#     print("il numero inserito non è perfetto")  

print("---------------------------------------------------------------------------")
# 🍰 Esercizio 19
# Scrivi una funzione che aggiunga ad una lista 10 colori inseriti dall'utente. 
# Il programma deve poi chiedere all'utente di inserire una lettera e mostrare in output solo i colori nella lista che iniziano con quella lettera.
# Suggerimento: potresti usare la funzione range e il metodo startswith().

# colorListExe19 = []

# for i in range(0,11): 
#     if i >= 10:
#         charExe19 = input("inserisci una lettera:")
#         for color in colorListExe19:
#             if color.startswith(charExe19[0]):
#                 print(color)
#         break
#     colorListExe19.append(input('inserisci il colore numero ' + str(i + 1)))
     
    

print("---------------------------------------------------------------------------")
# 🍰 Esercizio 20
# Scrivi una funzione che prenda una serie di input dall'utente utilizzando 
# un ciclo while e li stampi con la funzione print senza andare a capo. 
# Il ciclo while si deve interrompere quando l'utente preme INVIO senza scrivere nulla.

# str1Exe20 = ""

# while True:
#     inputExe20 = input("inserire qualcosa")
#     if inputExe20 == "":
#         break
#     str1Exe20 += inputExe20

# print(str1Exe20)



print("---------------------------------------------------------------------------")
# 🍰 Esercizio 21
# Scrivi una funzione che accetti una lista di dizionari rappresentante una scuola. 
# Ogni dizionario rappresenta uno studente e contiene nome, cognome, classe e voti. 
# La funzione deve stampare un elenco di tutti gli studenti e calcolare la media dei voti di ciascuno.

# dictListExe21 = [
#     {"nome": "mario" , "cognome":"rossi" , "storia" : 8, "italiano":2 , "matematica": 7 , "classe" : "A1"},
#     {"nome": "mario" , "cognome":"rossi" , "storia" : 9, "italiano":6 , "matematica": 9 , "classe" : "B1"},
#     {"nome": "mario" , "cognome":"rossi" , "storia" : 1, "italiano":2 , "matematica": 7 , "classe" : "B1"},
#     {"nome": "mario" , "cognome":"rossi" , "storia" : 0, "italiano":2 , "matematica": 2 , "classe" : "B2"},
#     {"nome": "mario" , "cognome":"rossi" , "storia" : 5, "italiano":2 , "matematica": 1 , "classe" : "B2"},
#     {"nome": "mario" , "cognome":"rossi" , "storia" : 2, "italiano":1 , "matematica": 7 , "classe" : "A3"},
#     {"nome": "mario" , "cognome":"rossi" , "storia" : 8, "italiano":10 , "matematica": 9 , "classe" : "B3"},
#     {"nome": "mario" , "cognome":"rossi" , "storia" : 4, "italiano":4 , "matematica": 4 , "classe" : "C1"},
#     {"nome": "mario" , "cognome":"rossi" , "storia" : 8, "italiano":8 , "matematica": 8 , "classe" : "C1"},
#     ]


# def calcolaMediaTutti(arr):
#     for i in range(0 , len(arr)):
#         print("nome:", arr[i]["nome"])
#         print("cognome:",arr[i]["cognome"])
#         print("classe:",arr[i]["classe"])
#         totVotiExe21 = arr[i]["storia"] + arr[i]["italiano"] + arr[i]["matematica"]
#         print("media:", (totVotiExe21/3))

# calcolaMediaTutti(dictListExe21)



print("---------------------------------------------------------------------------")
# 🍰 Esercizio 22
# Scrivi un programma che crei un file CSV per memorizzare in un dizionario i dati degli utenti registrati su un sito web. 
# I dati richiesti per ogni utente sono: username, password, email e data di registrazione. 
# Il programma deve permettere di salvare le informazioni nel file, leggere i dati e stamparli a schermo.


import csv

def creaFileCsv(dizionario, nome_file):
    with open(nome_file, 'w', newline='') as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(['username', 'password', 'email', 'data_registrazione'])
        for utente in dizionario.values():
            writer.writerow([utente['username'], utente['password'], utente['email'], utente['data di registrazione']])

def leggiFileCsv(nome_file):
    with open(nome_file, 'r') as file_csv:
        reader = csv.reader(file_csv)
        for row in reader:
            print(row)


utenti = {
    1:{"username":"coso", "password":"1234", "email":"wfafawf@gmail.com" , "data di registrazione":"16/01/1990"}, 
    2:{"username":"coso1","password": "1234","email": "sfawfwf@gmail.com" ,"data di registrazione":"17/03/1990"}, 
    3:{"username":"coso3","password": "1234","email": "wutgdfkkyf@gmail.com" ,"data di registrazione":"19/09/1990"}, 
    4:{"username":"coso2","password": "1234","email": "cxdfbbswf@gmail.com" ,"data di registrazione":"22/02/1993"}, 
    5:{"username":"coso4","password": "1234","email": "u5kiedrgwf@gmail.com" ,"data di registrazione":"16/05/1999"}, 
    6:{"username":"coso5","password": "1234","email": "wwqsavawvawf@gmail.com" ,"data di registrazione":"09/10/1991"}, 
}


creaFileCsv(utenti, 'utenti.csv')

leggiFileCsv('utenti.csv')




    

print("---------------------------------------------------------------------------")
# 🍰 Esercizio 23
# Scrivi una funzione che permetta di inserire una canzone e salvarla in un file di testo. Il programma deve chiedere all'utente di inserire il titolo e il testo della canzone, e poi salvare quest'ultimo in un file intitolato titolo_canzone.txt.
# Suggerimento: dovrai utilizzare l'istruzione with.

print("---------------------------------------------------------------------------")
# 🍰 Esercizio 24
# Scrivi una funzione che crei una tupla contenente i nomi dei pianeti del sistema solare, la loro tipologia (gassoso o roccioso) e il numero di satelliti naturali conosciuti. Il programma deve quindi stampare a schermo il contenuto della tupla e il numero totale di satelliti.
print("---------------------------------------------------------------------------")
# 🍰 Esercizio 25
# Scrivi una funzione che prenda come argomento un set di sport preferiti dall'utente e stampi un messaggio di testo che indica se si tratta di uno sport di squadra o individuale.
# Suggerimento: per valutare la stringa inserita potrebbe essere utile utilizzare il metodo lower.
