

# 10 - while
# 1 - cosa sono i loop/cicli
# 2 - sintassi del while
# 3 - break , continue , else


x = ["roma" , "milano" , "napoli"]
y = "ciao"

i = 1
while i < 10:
    i+= 1
    if i == 3:
        continue
    if i == 7:
        break
    print(i)
else:
    print("il loop è finito")
    

