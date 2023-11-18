

#||----------------------------------------------------------------------------------||
#||----------------------------------------------------------------------------------||
#|| documentazione presa da qui --> https://codegrind.it/esercizi/python/ciclo-for/  ||
#||----------------------------------------------------------------------------------||
#||----------------------------------------------------------------------------------||


# Tracce
# 🍰 Esercizio 1
# Scrivere un programma che utilizzi un loop for per stampare ogni elemento di una lista.

print("esercizio 1")

arrEx1 = [ 7, 6, 1, 2, 1 ]

for num1 in arrEx1:
    print(num1)
print("---------------------------------------------")
# 🍰 Esercizio 2
# Scrivere un programma che utilizzi un loop for per stampare tutti i numeri da 1 a 10.

print("esercizio 2")

for x in range(1 , 11):
    print(x)



print("---------------------------------------------")
# 🍰 Esercizio 3
# Scrivere un programma che utilizzi un loop for per sommare tutti i numeri in una lista.

print("esercizio 3")


arrEx3   = [ 7, 0, 1, 7, 5 ]
numEx3 = 0
for num3 in arrEx3:
    numEx3 += num3

print(numEx3)

print("---------------------------------------------")
# 🍰 Esercizio 4
# Scrivere un programma che utilizzi un loop for per stampare tutti i numeri pari da 1 a 20.

print("esercizio 4")

for x in range (2 , 22 , 2):
    print(x)

print("---------------------------------------------")    
# 🍰 Esercizio 5
# Scrivere un programma che utilizzi un loop for per stampare tutte le lettere di una stringa.

print("esercizio 5")

strEx5 = "stampa questo"

for let in strEx5:
    print(let)

print("---------------------------------------------")
# 🍰 Esercizio 6
# Scrivere un programma che utilizzi un loop for per stampare tutte le chiavi di un dizionario

print("esercizio 6")

dictEx6 = {
  "United States": "Washington D.C.", 
  "Italy": "Rome", 
  "England": "London"
}

for key in dictEx6:
    print(key)

print("---------------------------------------------")
# 🍰 Esercizio 7
# Scrivere un programma che utilizzi un loop for per stampare tutte le coppie chiave-valore di un dizionario.

print("esercizio 7")

dictEx7 = {
    "age": 29 , 
    "pi greco" : 3.14 , 
    "primi": [2, 3, 5, 7]
}

for key in dictEx7:
    print(key + " " + str(dictEx7[key]))
    
print("---------------------------------------------")
# 🍰 Esercizio 8
# Scrivere un programma che utilizzi un loop for per stampare tutte le lettere di ogni stringa in una lista.

print("esercizio 8")

arrEx8 = ["pippo" , "franco" , "gianni"]
for stringa in arrEx8:
    for let in stringa:
        print(let)


print("---------------------------------------------")
# 🍰 Esercizio 9
# Scrivere un programma che utilizzi un loop for per contare quante volte una lettera compare in una stringa.

print("esercizio 9")

print("inserisci una frase")
strEx9 = input()

volteInEx9 = 0

print("inserisci una lettera")
trovareInEx9 = input()

for let in strEx9:
    if let == trovareInEx9:
        volteInEx9 += 1
        

print("la lettera " + trovareInEx9 + " è stata trovata " + str(volteInEx9) + " volte")
        

print("---------------------------------------------")
# 🍰 Esercizio 10
# Scrivere un programma che utilizzi un loop for per calcolare la media di una lista di numeri.

print("esercizio 10")

arrEx10   = [ 5, 2, 1, 3, 5 ]
numEx10 = 0
arrayLength = 0

for num10 in arrEx10:
    numEx10 += num10
    arrayLength += 1
    

print(numEx10 / arrayLength)