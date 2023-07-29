
# 06 stringhe
# 1 - creare una stringa, parlare di apici doppi singoli
# 2 - mandare a schermo stringa e variabile stringa
# 3 - stringe multi riga """prova"""
# 4 - trattare stringe come array (prendere carattere, lenght , loop)

# 5 - prendere parte di stringa str[:5] str[:2] str[-5:-2]
# 6 - modificare stringa con upper() lower() strip() e replace()
# 7 - concatenare stringhe
# 8 - usare format() per combinare stringhe e numeri
# 9 - escape dei caratteri


x = """ciao
    ciao"""
y = 'ciao sono luca'

# print(x[0])
print(x[:3])
print(y[2:7])

for carattere in "computer":
    print(carattere)
    
z = " ciao sono giorgio"

print(z.lower())
print(z.strip())
print(z.replace("o", "w"))

prova = "ciao sono luca e sono nato il {}"
eta = 23

print(prova.format(eta))

sec = "ciao sono luca e sono nato il {2} , peso {0} e altezza {1}"

print(sec.format(15 , 65 , 1.70))

terzo = "ciao sono luca e sono \"figo\""

print(terzo)
