# 21 moduli
# 1 - cos'e un modulo
# 2 - creare un modulo
# 3 - funzioni variabili in un mofulo
# 4 - creare un alias
# 5 - moduli built in (piattaforme , math)
# 6 - funzione dir()
# 7 - importare solo una parte del modulo

import mioModulo as mm # esempio di alias
import platform
import math
# from mioModulo import persona1 (per importare solo una parte del modulo)

print("un modulo è un file contenente delle funzioni e variabili(come le librerie java)")

x = mm.persona1["nome"]
mm.saluta(x)

print(x)


y = platform.system()

print(y)

print(math.floor(2.2151251))



print("qui dir() -->" , dir(math))




