#||------------------------------------------------------------------------------------||
#||------------------------------------------------------------------------------------||
#|| documentazione presa da qui --> https://codegrind.it/esercizi/python/ciclo-while/  ||
#||------------------------------------------------------------------------------------||
#||------------------------------------------------------------------------------------||


# Tracce
# 🍰 Esercizio 1
# Stampare i numeri interi da 1 a 10 usando un loop while.

# print("esercizio 1")
# i1 = 0

# while i1 < 10:
#     i1 += 1
#     print(i1)

print("-------------------------------------------------------------------------------")


# 🍰 Esercizio 2
# Calcolare la somma dei primi n numeri interi positivi usando un loop while. L'utente deve inserire il valore di n.
print("esercizio 2")


nArray = [float(input()) , float(input()) , float(input())]
i2 = 0
numEx2 = 0

while i2 < 3:
    numEx2 += nArray[i2]
    i2 += 1

print(numEx2)

print("-------------------------------------------------------------------------------")
# 🍰 Esercizio 3
# Stampare i numeri pari da 2 a 10 usando un loop while.
print("esercizio 3")


i3 = 0

while i3 < 9:
    i3 += 2
    print(i3)


print("-------------------------------------------------------------------------------")
# 🍰 Esercizio 4
# Chiedere all'utente di indovinare un numero intero casuale compreso tra 1 e 10. Continuare a chiedere all'utente di indovinare finché non indovina il numero corretto. Usare un loop while.
print("esercizio 4")


i4 = 0
inputNum1 = float(input())

while i4 > 0:
    if(inputNum1 == 5):
        print("esatto")
        i +=1
    else:
        print("wrong")
        inputNum1 = float(input())

rand = randrange(10)
print(rand)


print("-------------------------------------------------------------------------------")
# 🍰 Esercizio 5
# Chiedere all'utente di inserire una stringa. Stampare la stringa al contrario usando un loop while.
print("esercizio 5")


str1Ex5 = input()
i5 = len(str1Ex5) - 1
s1 = ""

while i5 >= 0:
    s1 = s1 + str1Ex5[i5]
    i5 -= 1

print(s1)

print("-------------------------------------------------------------------------------")
# 🍰 Esercizio 6
# Stampare i numeri da 10 a 1 usando un loop while.
print("esercizio 6")


i6 = 10

while i6 > 0:
    print(i6)
    i6 -= 1 

print("-------------------------------------------------------------------------------")
# 🍰 Esercizio 7
# Calcolare il fattoriale di un numero intero positivo n usando un loop while.
print("esercizio 7")

res1Ex7 = 1
i7 = 2
floorToReach = int(input())


if 3 < floorToReach < 11:
    while i7 <= floorToReach:
        res1Ex7 *= i7
        i7 += 1   
print(res1Ex7)


print("-------------------------------------------------------------------------------")
# 🍰 Esercizio 8
# Chiedere all'utente di inserire una lista di numeri interi. Stampare la somma di tutti i numeri usando un loop while.
print("esercizio 8")

listEx8 = [int(input()) , int(input()) , int(input()) , int(input()) , int(input())]
i8 = len(listEx8) -1
resultEx8 = 0 

while i8 >= 0:
    resultEx8 =  resultEx8 + listEx8[i8]
    i8 -= 1

print(resultEx8)

print("-------------------------------------------------------------------------------")
# 🍰 Esercizio 9
# Chiedere all'utente di inserire una stringa. Stampare solo le consonanti della stringa usando un loop while.
print("esercizio 9")

i9 = 0
str1Ex9 = input()
splitted = list(str1Ex9)
floorToReach = len(splitted) 

while i9 < floorToReach:
    if(splitted[i9] == "a" or splitted[i9] == "e" or splitted[i9] == "i" or splitted[i9] == "o" or splitted[i9] == "u"):
        i9 += 1
    else:
        print(splitted[i9])
        i9 += 1

