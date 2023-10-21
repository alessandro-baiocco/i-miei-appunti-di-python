
# 🍰 Esercizio 1
# Scrivi una funzione che prende una lista di numeri e restituisce la somma di tutti gli elementi.

valori = [10 , 65 , 23 , 54 , 21]

def esercizio_1(arr):
    totale = 0
    for n in arr:
        totale += n
    return totale

# print(esercizio_1(valori))


print("-------------------------------------------------------------------------------")
# 🍰 Esercizio 2
# Scrivi una funzione che prende una stringa e restituisce la stringa invertita.

def esercizio_2(str):
    return str[::-1]

# print(esercizio_2("hello world"))


print("-------------------------------------------------------------------------------")
# 🍰 Esercizio 3
# Scrivi una funzione che prende una lista di parole e restituisce una lista contenente solo le parole che iniziano con una lettera specificata.
parole = ["cosa" , "franco" , "tizio" , "citta" , "citofono"]
def esercizio_3(strArr , letter):
    finalArr = []
    for str in strArr:
        if(str[0] == letter):
            finalArr.append(str)
    return finalArr
            
# print(esercizio_3(parole , "c"))       


print("-------------------------------------------------------------------------------")
# 🍰 Esercizio 4
# Scrivi una funzione che prende una lista di numeri e restituisce una lista contenente solo i numeri pari.

def esercizio_4(arr):
    finalArr2 = []
    for n in arr:
        if(n % 2 == 0):
            finalArr2.append(n)
    return finalArr2

# print(esercizio_4(valori))
         



print("-------------------------------------------------------------------------------")
# 🍰 Esercizio 5
# Scrivi una funzione che prende una lista di parole e restituisce una lista contenente la lunghezza di ciascuna parola.

def esercizio_5(strArr):
    numArr2 = []
    for str in strArr:
        numArr2.append(len(str))
    return numArr2

# print(esercizio_5(parole))


    



print("-------------------------------------------------------------------------------")
# 🍰 Esercizio 6
# Scrivi una funzione che prende una lista di numeri e restituisce il valore massimo.
def esercizio_6(arr):
    finalNum = 0
    for n in arr:
        if n > finalNum:
            finalNum = n
    return finalNum

# print(esercizio_6(valori))




print("-------------------------------------------------------------------------------")
# 🍰 Esercizio 7
# Scrivi una funzione che prende una lista di parole e restituisce la parola più lunga.
print("-------------------------------------------------------------------------------")
# 🍰 Esercizio 8
# Scrivi una funzione che prende una lista di numeri e restituisce la media dei numeri.
print("-------------------------------------------------------------------------------")
# 🍰 Esercizio 9
# Scrivi una funzione che prende una lista di parole e restituisce una lista contenente solo le parole palindrome.
print("-------------------------------------------------------------------------------")
# 🍰 Esercizio 10
# Scrivi una funzione che prende una lista di numeri e restituisce una lista contenente solo i numeri maggiori di un valore specificato.
