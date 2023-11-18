# 20 scope
# 1 - cos'e lo scope
# 2 - scope locale
# 3 - keyword global 

print("lo scope è la disponibilita delle variabili")

y = 100 # esempio di scope globale(disponibile fuori dall funzione)

def funzione():
    global y 
    x = 400 # esemprio di scope locale(disponibile solo dentro la funzione)
    y = 200 #cosi cambiamo la y all'esterno della funzione
    print("x :",  x , "Y :" , y)

print(y)
funzione()