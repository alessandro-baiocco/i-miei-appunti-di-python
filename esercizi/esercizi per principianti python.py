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



print("---------------------------------------------------------------------------")
# 🍰 Esercizio 5
# Scrivi un semplice programma che, data una lista di numeri, sommi tra loro tutti gli elementi.
# Suggerimento: anche se esiste la funzione sum() per risolvere l'esercizio potresti usare il ciclo for.


print("---------------------------------------------------------------------------")
# 🍰 Esercizio 6
# Scrivi un programma "moltiplicatore" che, data una lista di numeri, moltiplichi tra loro tutti gli elementi.




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
