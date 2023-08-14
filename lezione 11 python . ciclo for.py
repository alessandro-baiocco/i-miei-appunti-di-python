# 11 - for 
# 1 - sintassi from 
# 2 - esempio con stringa, lista , range
# 3 - break, continuo , else


lista_città = ["milano" , "roma" , "napoli"]
stringa = "anguria"

for città in lista_città: # in città ci può essere tutto è solo un parametro
    print(città)

for letter in stringa: 
    print(letter)
    
for x in range(6): 
    if x == 2:
        continue
    if x == 4:
        break
    print(x)
else:
    print("ho finito")

for riga in range(6): 
    for colonna in range(10):
        print("( y: " + str(riga) + " | x: " + str(colonna) + ")")


