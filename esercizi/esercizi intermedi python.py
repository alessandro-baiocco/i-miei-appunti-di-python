#||----------------------------------------------------------------------------------------||
#||----------------------------------------------------------------------------------------||
#|| documentazione presa da qui --> https://www.programmareinpython.it/esercizi-python/    ||
#||----------------------------------------------------------------------------------------||
#||----------------------------------------------------------------------------------------||
# Esercizio 001
# Il Linguaggio dei Furfanti In Svezia, i bambini giocano spesso utilizzando un linguaggio un po' particolare detto rövarspråket, 
# che significa "linguaggio dei furfanti":consiste nel raddoppiare ogni consonante di una parola e inserire una "o" nel mezzo. 
# Ad esempio la parola "mangiare" diventa "momanongogiarore".
# Scrivi una funzione in grado di tradurre una parola o frase passata tramite input in rövarspråket. Dopo aver tradotto una frase, 
# il programma dovrà chiedere all'utente se intende tradurne un'altra, e in caso di risposta positiva, 
# dovrà attendere l'inserimento di una nuova parola da parte dell'utente.


vocali = ["a" , "e" , "i" , "o" , "u" , " "]
str2Exe1 = ""


while True:
    str1Exe1 = input("scrivi una frase o parola premi invio senza niente per uscire \n")
    if str1Exe1 == "":
        break
    else:
        for char in str1Exe1:
            if char not in vocali:
                str2Exe1 += (char + "o" + char)
            else:
                str2Exe1 += char
    print(str2Exe1)
    str2Exe1 = ""

print("---------------------------------------------")

# Esercizio 002
# Reverser
# Scrivi una funzione a cui passerai come parametro una stringa, 
# e che manderà in print una versione inversa (al contrario) della stessa stringa. Ad esempio "abcd" diventerà "dcba".
# Suggerimento: per risolvere questo esercizio in modo compatto potresti usare lo slicing.

def reverse(str):
    revStr = str[::-1]
    return revStr

print(reverse("the cat is on the table"))




print("---------------------------------------------")

# Esercizio 003
# Palindromo... o non Palindromo?
# Scrivi una funzione a cui viene passata una parola e riconosce se si tratta di un palindromo 
# (parole che si leggono uguali anche al contrario) oppure no.


def palindromo(str):
    revStr = str[::-1]
    if revStr == str:
        print("si è una parola palindroma")
    else:
        print("non è una parola palindroma")

palindromo("nove")


print("---------------------------------------------")

# Esercizio 004
# Generatore di Password
# Scrivi una funzione generatrice di password.
# La funzione deve generare una stringa alfanumerica di 8 caratteri qualora 
# l'utente voglia una password semplice, e di 20 caratteri ASCII qualora desideri una password più complicata.
import random, string
from random import randint
choiseExe4 = input("che tipo di password vuoi 1| per una password semplice 2| per una complessa\n")

passWord = ""

if choiseExe4 == "1":
    passWord += ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8))
elif choiseExe4 == "2":
    passWord += ''.join(chr(randint(33 , 127)) for _ in range(20))
    
print(passWord)










print("---------------------------------------------")

# Esercizio 005
# Poesia Elettronica
# Scrivi una semplice funzione rimario, a cui viene passato un elenco di parole 
# come parametro e che riceva una parola inserita dall'utente tramite la funzione input.
# La funzione rimario dovrà confrontare la parola inserita dall'utente con quelle presenti nell'elenco passato, 
# alla ricerca di rime, intese come parole le cui ultime 3 lettere siano uguali alla parola inserita dall'utente.
# Le rime dovranno essere quindi mostrate in output utilizzando il metodo join.

parole = ["rose" , "fiori" , "autobus" , "arancione" , "pose" , "cose" , "amore" , "stazione" ]

word1Exe5 = input("scrivi una parola\n")


def makeARime(str):
    for word in parole:
        if str[-3:-1] == word[-3:-1]:
            print(word)

makeARime(word1Exe5)








print("---------------------------------------------")

# Esercizio 006
# La Libreria
# Scrivi una funzione vendi_libri(), che aiuti nella gestione della vendita di libri in una libreria:
# Controlla se il libro richiesto è presente sugli scaffali della libreria
# Qualora il libro sia presente, ne decrementa il numero di copie (eventualmente rimuovendo il titolo) 
# e ci segnala che la vendita ha avuto successo
# Se il libro non è disponibile, viene messo in un elenco di libri da ordinare e ci viene comunicato che la vendita non ha avuto successo
# La funzione deve restituire valore booleanoTrue o False in base all'esito della vendita.

deposito = {"libro 1" : 4 , "libro 2" : 0 , "libro 3" : 1}
daAcquistare = {}


def vendi_libri():
    while True:
        inputExe8 = input("che libro vuoi comprare? libro 1 , libro 2 , libro 3\n")
        if inputExe8 == "":
            break
        if deposito[inputExe8] > 0:
            deposito[inputExe8] -= 1
            print("l'acquisto è avvenuto con successo")
            return True
        else:
            print("il libro non è presente in deposito")
            if inputExe8 is daAcquistare:
                daAcquistare[inputExe8] += 1
                return False
            else:
                daAcquistare[inputExe8] = 1
                return False


vendi_libri()


print("---------------------------------------------")

# Esercizio 007
# Crittografia ROT-13
# Il ROT-13 è un semplice cifrario monoalfabetico, in cui ogni lettera del messaggio da cifrare 
# viene sostituita con quella posta 13 posizioni più avanti nell'alfabeto.
# Scrivi una semplice funzione in grado di criptare una stringa passata, 
# o decriptarla se la stringa è già stata precedentemente codificata.

alfabeto = ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" ,"n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" ,"w", "x" , "y" , "z" ]


while True:
    input1Exe7 = input("inserire la parola da cifrare o decifrare\n")
    input2Exe7 = input("1| cifrare o 2| decifrare \n")
    newWord = ""
    if input1Exe7 == "":
        break
    if input2Exe7 == "1":
        for letter in input1Exe7:
            index = alfabeto.index(letter)
            if index >= 13:
                newWord += alfabeto[index - 13]
            else:
                newWord += alfabeto[index + 13]
        print("newWord")
    elif input2Exe7 == "2":
        for letter in input1Exe7:
            index = alfabeto.index(letter)
            if index < 13:
                newWord += alfabeto[index + 13]
            else:
                newWord += alfabeto[index - 13]
    print(newWord)
            
            
        



                                                                                       



print("---------------------------------------------")

# Esercizio 008
# Il Peso di una Cartella
# Scrivi una funzione che calcoli la somma (espressa in MB) delle dimensioni dei file presenti 
# nella cartella di lavoro utilizzando il modulo os.


import os


input1Exe8 = input("inserire un percorso\n")

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size / 1000000

print(get_size(input1Exe8), 'Mb')


print("---------------------------------------------")

# Esercizio 009
# Il Postino
# Scrivi una funzione "postino" che sia in grado di spedire delle eMail tramite Gmail.
# Suggerimento: puoi usare il modulo smtplib.
import smtplib
from dotenv import load_dotenv
load_dotenv()



# def sendMail():
#     oggetto = input("inserire oggetto mail\n")
#     contenuto = input("inserire messaggio mail\n")
#     messaggio = oggetto + contenuto
#     email = smtplib.SMTP("smtp.gmail.com" , 587)
#     email.ehlo()
#     email.starttls()
#     email.login(os.getenv("MY_MAIL"), os.getenv("MY_PASS_MAIL"))
#     email.sendmail(os.getenv("MY_MAIL"), os.getenv("MY_MAIL"), messaggio)
#     email.quit()
    
# sendMail()


print("---------------------------------------------")

# Esercizio 010
# La Cercatrice
# Scrivi una funzione "cercatrice" che scansioni un dato percorso di sistema alla ricerca di file di tipo pdf tramite il modulo os. 
# La funzione dovrà avere le seguenti caratteristiche:
# Il percorso fornito dovrà essere anzitutto validato, in quanto deve portare a una cartella esistente
# La funzione dovrà fornire un elenco dei file pdf (con/relativo/percorso) man mano che questi vengono trovati
# In fine la funzione dovrà fornire in output il totale dei file .pdf che sono stati trovati durante la scansione.


input1Exe10 = input("inserire un percorso\n")

def get_pdfs(start_path = '.'):
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            if ".pdf" in f:
                print(os.path.join(dirpath, f))
                
                
get_pdfs(input1Exe10)


print("---------------------------------------------")

# Esercizio 011
# Il Salvatore
# Scrivi una funzione "file_backup" che sia in grado di effettuare copie di backup di determinati tipi di file, con le seguenti caratteristiche:
# Percorso da scansionare, di backup e tipologia di file da copiare dovranno essere passati dall'utente tramite input
# Il programma dovrà verificare la presenza o meno di una cartella di backup al percorso fornito, 
# e qualora questa non fosse presente dovrà crearla
# La funzione dovrà anche gestire l'eventuale scelta da parte dell'utente, di un percorso da scansionare che non esiste
# Suggerimento: potresti importare i moduli os e shutil.

import shutil

def file_backup():
    percorso = input("Inserisci il percorso : ")
    if not os.path.isdir(percorso):
        print(f"Il percorso inserito '{percorso}' risulta non essere un percorso idoneo. Verifica e riprova, grazie.\n")
        return file_backup()
    estensione = input("Che tipologia di file desideri salvare? [esempio: .jpg .pdf .epub]:\n ")
    backup_folder = input("Inserisci la cartella dove desideri salvare i tuoi file:\n ")
    if not os.path.isdir(backup_folder):
      	 os.makedirs(backup_folder)
    contatore = 0
    print(f"Sto effettuando la scansione di '{percorso}' alla ricerca di file '{estensione}'\n")
    for dirpath, dirnames, filenames in os.walk(percorso):
        for f in filenames:
            if f.endswith(estensione):
                match = os.path.join(dirpath,f)
                print(f"Trovato file {estensione}: {match}")
                shutil.copy(match,backup_folder)
                contatore += 1
    print("Copia Terminata")
    print(f"Ho trovato '{contatore}' files con estensione {estensione}, ora disponibili anche in '{backup_folder}'")

# file_backup()

print("---------------------------------------------")

# Esercizio 012
# Funzione Fattoriale Ricorsiva
# Scrivi una funzione ricorsiva che calcola il fattoriale di un numero dato.
try:
    def calcola_fattoriale():
        input1Exe12 = int(input("inserisci un numero\n"))
        fattoriale = 1
        for n in range(1 , input1Exe12 + 1):
            fattoriale *= n
        return fattoriale
except:
    print("inserisci un numero intero")
    calcola_fattoriale()
    
    
print(calcola_fattoriale())
    

        

    



print("---------------------------------------------")

# Esercizio 013
# La Successione di Fibonacci
# Nella Successione di Fibonacci, ciascun numero è la somma dei due numeri che lo precedono, ad esempio:
# 1, 1, 2, 3, 5, 8, 13 (...)
# Scrivi una funzione ricorsiva che restituisce in output i numeri della successione di Fibonacci, 
# entro una soglia specifica impostata dall'utente.

try:
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return (fibonacci(n-1) + fibonacci(n-2))
        
    
    input1Exe13 = int(input("Inserisci la lungezza della serie che desideri vedere\n"))
    serieFibonacci = ""

    for num in range(1, input1Exe13+1):
        serieFibonacci += str(fibonacci(num)) + "|"

    print(serieFibonacci)
except:
    print("inserisci un valore intero")    
    



print("---------------------------------------------")

# Esercizio 014
# Il Cifrario di Cesare
# Il Cifrario di Cesare è un algoritmo di crittografia che consiste nello spostare ciascuna lettera di una certa quantità di posti nell'alfabeto. 
# Per utilizzarlo, si sceglie una chiave che rappresenta il numero di posti di cui ogni lettera dell'alfabeto verrà spostata: 
# ad esempio, se si sceglie una chiave di 3, la lettera A diventerà D, la lettera B diventerà E e così via. Per decifrare un messaggio cifrato 
# con il cifrario di Cesare bisogna conoscere la chiave utilizzata e spostare ogni lettera indietro di un 
# numero di posti corrispondente alla chiave.
# Scrivi una funzione che riceva come argomento una stringa e un numero e applichi il Cifrario di Cesare alla stringa spostandosi nell'alfabeto di tante posizioni quante dice il numero.

