# 14 tuple
# 1 - collezioni di dati ordinate , indicizzate, non modificabili e permettono duplicati
# 2 - creare una tupla normale e con un valore , singole e mischiate 
# 3 - vediamo len() , type() e tuple()

# 4 - accedere agli elementi della lista , singolo , range , negativo
# 5 - verificare se un elemento esiste
# 6 - modificare e inserire: non è possibile se non con escamotage
# 7 - inserire elementi con append() , insert() , extend()
# 8 - rimuovere elementi con escamotage oppure cancellare tutto con del()
# 9 - spacchettare una tupla (unpack) normale e con *
# 10 - ciclare elementi
# 11 - unire tuple con join()
# 12 - metodi count() e index()

prima = ("milano" , "roma" , "napoli")
seconda = ("pippo" , True , 45)
terza = ("franco",)

print("--------------------------------type-------------------------------")
print(type(terza))
print("--------------------------------len-------------------------------")
print(len(prima))
print("--------------------------------list-------------------------------")
print(list(prima))
print("--------------------------------accedere-------------------------------")
print(prima[0:])
print(prima[0:2])
if "roma" in prima:
    print("si c'e")
print("--------------------------------change-------------------------------")
y = list(prima)
y.remove("roma")
prima = tuple(y)
print(prima)

(x , y , z) = seconda
print(x)
print(y)
print(z)

