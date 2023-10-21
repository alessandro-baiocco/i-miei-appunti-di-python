# 17 - funzione
# 1 - cosa sono le funzioni
# 2 - creare una funzione
# 3 - chiamare una funzione

# 4 - parametri in funzione
# 5 - differenza tra argomenti e parametri
# 6 - arbistrary arguments ,keyword argumenst
# 7 - parametri di default
# 8 - return dei valori


print("1 - le funzioni sono un blocco di codice riutilizzabile che verrà eseguito solo richiamandolo")


def fai_qualcosa():
    print("2 , 3 - mi sto muovendo")
    print("non so più cosa fare")
    print("mi fermo")
    

fai_qualcosa()
fai_qualcosa()
fai_qualcosa()

def fai_addizione(num , num2):
    print("4 - ora li sommo")
    print(num + num2)
    print("mi fermo")
    
fai_addizione(5 , 8)


print("il parametro è la definizione generica che utiliziamo nel definire la variabile (num), l'argomento è ciò che noi inseriamo mentre il programma sta andanto (5)")

print("-----------------arbitrary arguments-------------------")

def non_so_cosa_scrivere(*params):
    print("stampo argomenti")
    print("1 : " + params[0] )
    if params[1]:
        print("altri : "  + params[1])
    
    
non_so_cosa_scrivere("afwg" , "asgwag")


print("-----------------------keyword arguments----------------------")

def inverti(primo , secondo):
    print("stampo argomenti")
    print("1 : " + primo )
    if secondo:
        print("altri : "  + secondo)
    
    
inverti(secondo= "rossi" , primo= "gianni")

print("--------------------default--------------------")


def default(primo = "qualcosa a caso"):
    print("stampo argomenti")
    print("1 : " + primo )
    
    
default()

print("---------------------return--------------------------------")


def ritorna(num , num2):
    print("aggiungo uno a l'altro")
    return num + num2


x = ritorna(3 , 5)
print(x)










