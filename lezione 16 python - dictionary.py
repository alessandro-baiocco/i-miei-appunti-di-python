# 16 dictionary
# 1 - collezioni di dati ordinate , modificabili ma non permettono duplicati
# 2 - creare un dict
# 3 - vediamo len() , type()

# 4 - accedere agli elementi con [] , get() , keys() , values() , items() , controlare se chiave esiste
# 5 - modificare gli elementi con [] e update()
# 6 - aggiungere gli elementi con [] e update()
# 7 - rimuovere gli elementi con pop(key) , popitem() , clear() , del
# 8 - ciclare elementi: key, values, values() , keys() , items
# 9 - copiare dict con copy() e dict()
# 10 - dict annidati

prima = {
    "prima" : "milano" , 
    "seconda" :"roma" , 
    "terza" : "napoli"}
seconda = {1 : "pippo" , 
           2 : True , 
           3 : 45}
terza = { "coso" : "franco" ,}
quarta = {
    "nome" : "coso" , 
    "cognome" : "rossi" , 
    "eta"  : 30
#   "eta" : 50 la chiave non può essere duplicata 
    }

print("----------------------------------len----------------------------")
print(len(prima))
print("----------------------------------type----------------------------")
print(type(prima))
print("----------------------------------accedere agli elementi----------------------------")
print(prima["seconda"])
print(prima.get("prima"))

x = prima.keys()
y = prima.values()
z = prima.items()
print(x)
print(y)
print(z)


print("esiste" , "prima" in prima)
print("non esiste" , "aldo" in prima)

print("-------------------------------modificare gli elementi---------------------------------------")
seconda[1] = "pluto"
print(seconda[1])

seconda.update({1 : "boh"})
print(seconda[1])
print("-------------------------------aggiungere gli elementi---------------------------------------")

terza["colore"] = "blu"
print(terza)

terza.update({"marco" : "boh"})
print(terza)
print("-------------------------------rimuovere gli elementi---------------------------------------")


prima.pop("prima")
print(prima)


prima.popitem()
print(prima)

seconda.clear()
print(seconda)

try: 
    del seconda
    print(seconda)
except:
    print("seconda non esiste più")
    
print("------------------------------ciclare gli elementi---------------------------------------")

for chiave in quarta:
    print("chiave" , chiave)
    
for valore in quarta:
    print("valore" , quarta[valore])
    
for valore in quarta.values():
    print("valore" , valore)

for chiave in quarta.keys():
    print("chiave" , chiave)
    
for oggeto in quarta.items():
    print("oggeto" , oggeto)
    
print("------------------------------copiare gli elementi---------------------------------------")

a = quarta.copy()
print(a)
a = dict(quarta)
print(a)
print("------------------------------dict in dict---------------------------------------")

inception = {
    "nome" : "coso",
    "cognome" : "boh",
    "eta" : {
        "anni" : 25,
        "mesi" : 8,
        "giorni" : 15
    },
    "indirizzo" : {
        "citta" : "ancona",
        "cap" : 60027,
        "civico" : 21
    }
}

print(inception)
print(inception["indirizzo"]["civico"])

    
    


    






