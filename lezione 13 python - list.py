# 13 list
# 1 - collezioni di dati ordinate , indicizzate , modificabili e permettono duplicati
# 2 - creare una lista con tipi uguali o mischiati
# 3 - vediamo len() , type() e list()

# 4 - accedere agli elementi della lista , singolo , range , negativo 
# 5 - modificare elementi: singolo , range 
# 6 - inserire elementi con append() , insert() , extend()
# 7 - rimuovere elementi con remove(), pop() , del() , clear()
# 8 - ciclare elementi con for in , per indice , while e short hand
# 9 - list comprehension
# 10 - modificare l'ordine: asc , desc , reverse
# 11 - copiare una list con copy()
# 12 - unire più liste insieme: +, append(), extend()

valori = [10 , 65 , 23 , 54 , 21]
altrivalori = [ 30 , 27 , 59 , 76]
città = list(("milano" , "roma" , "napoli"))
valori2 = [95 , 82 , 659 , 8081 ,73521098]


print("--------------------------------type-------------------------------")
print(type(valori))
print("--------------------------------len-------------------------------")
print(len(valori))
print("--------------------------------list-------------------------------")
print(list(valori))
print("--------------------------------index[0]-------------------------------")
print(valori[0])
print(valori[-1])
print(valori[1:4])
print("--------------------------------change index-------------------------------")
valori[0] = 89
valori[1:3] = 78 , 32
print(valori)
print(valori[0])
valori[0:4] = [666]
print(valori)
print("--------------------------------add elements-------------------------------")
valori.append("culo")
print(valori)
valori.insert(1 , 999)
print(valori)
valori.extend(altrivalori)
print("valori" , valori)
print("altri valori" , altrivalori)
print("--------------------------------remove elements-------------------------------")
valori.remove(666)
print(valori)
valori.pop() #puoi usare l'indice in pop(x)
print(valori)
città.clear()
print("città =" ,città)

# del città 
# print("after del città =",città) (del elimina proprio la variabile è da errore)

print("--------------------------------for-------------------------------")
for x in altrivalori:
    print(x)
print("-------------")
for i in range(len(altrivalori)):
    print(altrivalori[i])
print("--------------------------------while-------------------------------")
n = 0 
while n < len(altrivalori):
    print(altrivalori[n])
    n += 1
print("--------------------------------for short hand------------------------")
[print(numero) for numero in valori if numero != "culo"]
print("-----------------------for short hand riassegna------------------------")
altrivalori = ["empty" for num in altrivalori if num != 30]
print(altrivalori)
print("-----------------------order------------------------")
valori2.sort()
print(valori2)
valori2.sort(reverse=True)
print(valori2)
print("-----------------------copy------------------------")
valori = valori2
valori[0] = 89
print(valori2)
valori3 = list(valori)
print(valori3)
print("-----------------------union------------------------")
print(valori3 + valori)
for number in valori3:
    valori.append(number)
print(valori)



