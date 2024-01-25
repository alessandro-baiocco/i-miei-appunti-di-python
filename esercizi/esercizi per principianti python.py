#||----------------------------------------------------------------------------------------||
#||----------------------------------------------------------------------------------------||
#|| documentazione presa da qui --> https://www.programmareinpython.it/esercizi-python/    ||
#||----------------------------------------------------------------------------------------||
#||----------------------------------------------------------------------------------------||




# 🍰 Esercizio 1
# Scrivi un programma che chieda due numeri all'utente tramite la funzione input e mostri il più grande tra i due utilizzando la funzione print.
# Per quanto Python disponga di una funzione max(), siete invitati ad utilizzare le istruzioni istruzioni if, elif ed else per la scrittura dell'algoritmo.

try:
    print("inserisci 2 valori")
    num1Exe1 = int(input())
    num2Exe1 = int(input())
    
    def numeroMaggiore(int1 , int2):
        if int1 > int2:
            print(int1)
        else:
            print(int2)
    numeroMaggiore(num1Exe1 , num2Exe1)
except:
    print("puoi inserire solo numeri interi")
    



print("---------------------------------------------------------------------------")
# 🍰 Esercizio 2
# Scrivi un programma che chieda tre numeri a, b, c all'utente e mostri il più grande tra loro.

try:
    
    print("inserisci 3 valori")
    num1Exe2 = int(input())
    num2Exe2 = int(input())
    num3Exe2 = int(input())
    
    print(max(num1Exe2 , num2Exe2 , num3Exe2))
        
except:
    print("puoi inserire solo numeri interi")




print("---------------------------------------------------------------------------")
# 🍰 Esercizio 3
# Scrivi un programma che, data una lista di numeri, fornisca in output il maggiore tra tutti gli elementi della lista.
#p.s. per non abusare della funzione max() utilizzaro un ciclo for

userValuesExe3 = []

try:
    print("inserisci tutti i valori che vuoi inserisci 0 per uscire")
    while True:
        newValueExe3 = int(input())
        if newValueExe3 == 0:
            break
        else:
            userValuesExe3.append(newValueExe3)
except:
    print("puoi inserire solo numeri")
    
higherValue = 0
for num in userValuesExe3:
    if num > higherValue:
        higherValue = num

print("il numero più grande è", higherValue)
    
    


print("---------------------------------------------------------------------------")
# 🍰 Esercizio 4
# Scrivi un programma che chieda all'utente una stringa composta da un solo carattere e dica se si tratta di una vocale oppure no.

vocali = ["a" , "e" , "i" , "o" , "u"]

print("inserisci una lettera se inserisci una parola verrà presa la prima lettera")
str1Exe4 = input()
if str1Exe4[0] in vocali:
    print("si, è una vocale")
else:
    print("no, non è una vocale")





print("---------------------------------------------------------------------------")
# 🍰 Esercizio 5
# Scrivi un semplice programma che, data una lista di numeri, sommi tra loro tutti gli elementi.
# Suggerimento: anche se esiste la funzione sum() per risolvere l'esercizio potresti usare il ciclo for.

userValuesExe5 = []

try:
    print("inserisci tutti i valori che vuoi inserisci 0 per uscire")
    while True:
        newValueExe5 = int(input())
        if newValueExe5 == 0:
            break
        else:
            userValuesExe5.append(newValueExe5)
except:
    print("puoi inserire solo numeri")
    
totalValueExe5 = 0
for num in userValuesExe5:
    totalValueExe5 += num

print("il totale è ", totalValueExe5)


print("---------------------------------------------------------------------------")
# 🍰 Esercizio 6
# Scrivi un programma "moltiplicatore" che, data una lista di numeri, moltiplichi tra loro tutti gli elementi.
userValuesExe6 = []

try:
    print("inserisci tutti i valori che vuoi inserisci 0 per uscire")
    while True:
        newValueExe6 = int(input())
        if newValueExe6 == 0:
            break
        else:
            userValuesExe6.append(newValueExe6)
except:
    print("puoi inserire solo numeri")
    
totalValueExe6 = 1
for num in userValuesExe6:
    totalValueExe6 *= num
    
print("il totale è ", totalValueExe6)




print("---------------------------------------------------------------------------")
# 🍰 Esercizio 7
# Scrivi un programma che a partire da un elemento e una lista di elementi dica in output se l'elemento passato sia presente o meno nella lista.
# Qualora l'elemento sia presente nella lista, il programma dovrà comunicarci l'indice dell'elemento tramite il metodo index.
    

print("---------------------------------------------------------------------------")
# 🍰 Esercizio 8
# Scrivi una semplice funzione che, data una lista di numeri, fornisca in output un istogramma basato su questi numeri, usando asterischi per disegnarlo.
# Data ad esempio la lista [3, 7, 9, 5], la funzione dovrà produrre questa sequenza:
# ***
# *******
# *********
# *****

print("---------------------------------------------------------------------------")
# 🍰 Esercizio 9
# Scrivi una funzione che restituisca la lunghezza di una stringa o lista passata come parametro. In sostanza, seppur presente, provate a scrivere la nostra versione della funzione len!
print("---------------------------------------------------------------------------")
# 🍰 Esercizio 10
# Scrivi una funzione che data in ingresso una lista A contenente n parole, restituisca in output una lista B di interi che rappresentano la lunghezza delle parole contenute in A.
# Questo esercizio può essere risolto anche usando una list comprehension.
    

print("---------------------------------------------------------------------------")
# 🍰 Esercizio 11
# Scrivi una funzione che, data una stringa come parametro, restituisca un dizionario rappresentante la "frequenza di comparsa" di ciascun carattere componente la stringa.
# Per fare un esempio, data una stringa "ababcc", otterremo in risultato {"a": 2, "b": 2, "c": 2}

print("---------------------------------------------------------------------------")
# 🍰 Esercizio 12
# Scrivi una funzione che, dato in ingresso un valore espresso in metri, mandi in print l'equivalente in miglia terrestri, iarde, piedi e pollici. Come risolverai questo esercizio?


print("---------------------------------------------------------------------------")
# 🍰 Esercizio 13
# Scrivi una semplice funzione che converta un dato numero di giorni, ore e minuti, passati dall'utente tramite funzione input, in secondi.
    

print("---------------------------------------------------------------------------")
# 🍰 Esercizio 14

# Scrivi una funzione che, a scelta dell'utente, calcoli l'area di:
# un cerchio
# un quadrato
# un rettangolo
# un triangolo
# Sentitevi liberi di estendere le potenzialità della funzione quanto meglio credete!

print("---------------------------------------------------------------------------")
# 🍰 Esercizio 15
# Un indirizzo MAC (Media Access Control address) è un indirizzo univoco associato dal produttore, a un chipset per comunicazioni wireless (es WiFi o Bluetooth), composto da 6 coppie di cifre esadecimali separate da due punti.
# Un esempio di MAC è 02:FF:A5:F2:55:12.
# Scrivi una funzione genera_mac() che generi degli indirizzi MAC pseudo casuali utilizzando il modulo random.
print("---------------------------------------------------------------------------")
# 🍰 Esercizio 16
# Scrivi una funzione che fornisca in output il nome del Sistema Operativo utilizzato con eventuali relative informazioni sulla release corrente.
# Suggerimento: per risolvere questo esercizio potreste dover utilizzare una libreria! ;)
    

print("---------------------------------------------------------------------------")
# 🍰 Esercizio 17
# Scrivi una funzione che, dato un carattere in ingresso, restituisca in output il codice ASCII associato al carattere passato.
# Anche in questo caso, usare una libreria potrebbe facilitare la risoluzione dell'esercizio!

print("---------------------------------------------------------------------------")
# 🍰 Esercizio 18
# Un numero perfetto è un numero naturale uguale alla somma dei suoi divisori positivi, escluso sé stesso. Scrivi una funzione che verifichi se un numero è perfetto oppure no.

print("---------------------------------------------------------------------------")
# 🍰 Esercizio 19
# Scrivi una funzione che aggiunga ad una lista 10 colori inseriti dall'utente. Il programma deve poi chiedere all'utente di inserire una lettera e mostrare in output solo i colori nella lista che iniziano con quella lettera.
# Suggerimento: potresti usare la funzione range e il metodo startswith().
    

print("---------------------------------------------------------------------------")
# 🍰 Esercizio 20
# Scrivi una funzione che prenda una serie di input dall'utente utilizzando 
# un ciclo while e li stampi con la funzione print senza andare a capo. 
# Il ciclo while si deve interrompere quando l'utente preme INVIO senza scrivere nulla.

print("---------------------------------------------------------------------------")
# 🍰 Esercizio 21
# Scrivi una funzione che accetti una lista di dizionari rappresentante una scuola. Ogni dizionario rappresenta uno studente e contiene nome, cognome, classe e voti. La funzione deve stampare un elenco di tutti gli studenti e calcolare la media dei voti di ciascuno.

print("---------------------------------------------------------------------------")
# 🍰 Esercizio 22
# Scrivi un programma che crei un file CSV per memorizzare in un dizionario i dati degli utenti registrati su un sito web. I dati richiesti per ogni utente sono: username, password, email e data di registrazione. Il programma deve permettere di salvare le informazioni nel file, leggere i dati e stamparli a schermo.

    

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
