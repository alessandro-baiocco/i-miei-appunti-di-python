
# 09 if
# 1 - if semplice
# 2 - operatori di comparazione
# 3 - elif else
# 4 - operatori logici and e or
# 5 - versione short hand
# 6 - if innestati
c = 15
X = 5
Y = 10
Z = 5

if X < 10:
    print("X è minore di 10")
    print("X è minore di questo numero")
    print("miao")
print("non sono nell'if")

if Y == 10:
    print("Y è uguale a 10")

if Z != 10:
    print("Z è diversa a 10")
elif x == 10:
    print("ma X è uguale a 10")
else:
    print("Z è uguale a 10")


if 10 <= c <= 30:
    print("c è compreso tra 10 e 30")
if  c > 10 and c < 30:
    print("c è compreso tra 10 e 30")
    
    
if x > 10 and y > 10: 
    print("x è y maggiori di 10") 
else:
    print("y o x minore di 10")
    
if Z > 10 or c > 10:
    print("z o c maggiori di 10")
else:
    print("z e c entrambe minore di 10")
    
    
if not(X < 10):
    print("x non è minore di 10")