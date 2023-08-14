
#||----------------------------------------------------------------------------------------||
#||----------------------------------------------------------------------------------------||
#|| documentazione presa da qui --> https://codegrind.it/esercizi/python/condizionali-if/  ||
#||----------------------------------------------------------------------------------------||
#||----------------------------------------------------------------------------------------||


# Tracce
# 🍰 Esercizio 1
# Scrivere un programma che chiede all'utente di inserire un numero e stampa "Il numero è positivo" se il numero è maggiore di zero, altrimenti stampa "Il numero è negativo".

# num1Es1 = input()
# num2Es1 = float(num1Es1)


# if num2Es1 > 0:
#     print("il numero è positivo")
# else:
#     print("il numero è negativo")


# 🍰 Esercizio 2
# Scrivere un programma che chiede all'utente di inserire due numeri e stampa "Il primo numero è maggiore" se il primo numero è maggiore del secondo, "Il secondo numero è maggiore" se il secondo numero è maggiore del primo, altrimenti stampa "I numeri sono uguali".

# num1Es2 = float(input())
# num2Es2 = float(input())

# if num1Es2 > num2Es2:
#     print("il primo numero è maggiore")
# elif (num1Es2 == num2Es2):
#     print("i numeri sono uguali")
# else:
#     print("il secondo numero è maggiore")


# 🍰 Esercizio 3
# Scrivere un programma che chiede all'utente di inserire una stringa e stampa "La stringa è vuota" se la stringa è vuota, altrimenti stampa "La stringa non è vuota".

# str1Es3 = input("")

# if (str1Es3 == "" ):
#     print("la stringa è vuota")
# else:
#     print("la stringa non è vuota")


# 🍰 Esercizio 4
# Scrivere un programma che chiede all'utente di inserire un numero e stampa "Il numero è pari" se il numero è pari, altrimenti stampa "Il numero è dispari".

# num1Es4 = float(input())

# if num1Es4 % 2 == 0:
#     print("il numero è pari")
# else:
#     print("il numero è dispari")
    
# 🍰 Esercizio 5
# Scrivere un programma che chiede all'utente di inserire una lettera e stampa "La lettera è una vocale" se la lettera è una vocale (a, e, i, o, u), altrimenti stampa "La lettera non è una vocale".
# str1Es5 = input("")

# if str1Es5 == "a" or str1Es5 == "e" or str1Es5 == "i" or str1Es5 == "o" or str1Es5 == "u":
#     print("è una vocale")
# else:
#     print("non è una vocale")

# 🍰 Esercizio 6
# Scrivere un programma che chiede all'utente di inserire un numero e stampa "Il numero è compreso tra 1 e 10" se il numero è compreso tra 1 e 10, altrimenti stampa "Il numero non è compreso tra 1 e 10".
# num1Es6 = float(input())

# if 0 < num1Es6 < 11:
#     print("il num è compreso tra 1 e 10")
# else:
#     print("il num non è compreso tra 1 e 10")
    
# 🍰 Esercizio 7
# Scrivere un programma che chieda all'utente di inserire un numero intero. Se il numero è maggiore di 10, stampare "Il numero è maggiore di 10". Se il numero è uguale a 10, stampare "Il numero è uguale a 10". Se il numero è minore di 10, stampare "Il numero è minore di 10".

# num1Es7 = float(input())

# if num1Es7 > 10:
#     print("il numero è maggiore di 10")
# elif (num1Es7 == 10):
#     print("il numero è uguale a 10")
# else:
#     print("il  numero è minore di 10")

# 🍰 Esercizio 8
# Scrivere un programma che chieda all'utente di inserire un carattere. Se il carattere è una vocale (a, e, i, o, u), stampare "Il carattere inserito è una vocale". Se il carattere è una consonante isAlpha(), stampare "Il carattere inserito è una consonante". Se il carattere non è una lettera, stampare "Il carattere inserito non è una lettera".

# str1Es8 = input()

# if str1Es8.isalpha():
#     if str1Es8 == "a" or str1Es8 == "e" or str1Es8 == "i" or str1Es8 == "o" or str1Es8 == "u":
#         print("la lettera è una vocale")
#     else:
#         print("la lettera non è una vocale")
# else:
#     print("non è una lettera o frase")

# 🍰 Esercizio 9 (difficile)
# Scrivere un programma che chieda all'utente di inserire tre numeri interi. Il programma deve verificare se i tre numeri formano un triangolo rettangolo. Se i tre numeri formano un triangolo rettangolo, stampare "I tre numeri formano un triangolo rettangolo". Altrimenti, stampare "I tre numeri non formano un triangolo rettangolo".

a = float(input())
b = float(input())
c = float(input())

if pow(a , 2) + pow(b , 2) == pow(c , 2) or pow(c , 2) + pow(b , 2) == pow(a , 2) or pow(a , 2) + pow(c , 2) == pow(b , 2):
    print(" i tre numeri formano un triangolo rettangolo")
else:
    print(" i tre numeri non formano un triangolo rettangolo")