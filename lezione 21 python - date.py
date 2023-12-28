# 22 date
# 1 - importare modulo dateteime
# 2 - creare un oggetto data con now() e data predefinita
# 3 - il metodo strtime per formattare la data 
# 4 - parametri formattazione data
#  %a  giorno della settimana, abbreviato
#  %A  giorno della settimana, intero
#  %w numero del giorno della settimana da 0 a 6, dove 0 è Sunday
#  %d numero del giorno del mese da 1 a 31  
#  %b nome del mese abbreviato
#  %B nome del mese intero
#  %m numero del mese da 1 a 12
#  %y anno abbreviato (20)
#  %Y anno intero (2020)
#  %H ora da 00 a 23
#  %I  ora da 00 a 12
#  %p AM/PM  
#  %M minuti da 00 a 59
#  %S secondi da 00 a 59
#  %f microsecondi da 000000 a 999999  
#  %z UTC offset 
#  %Z Time zone
#  %j numero del giorno nell'anno da 001 a 366
#  %U Numero della settimana dell'anno, domenica è il primo giorno della settimana, da 00 a 53
#  %W Numero della settimana dell'anno, lunedì è il primo giorno della settimana, da 00 a 53
#  %c versione locale di data e ora  
#  %x versione locale della data  
#  %X versione locale dell'ora  
# 5 - esempi formatazione data

import datetime

adesso = datetime.datetime.now()

print(adesso)


ora1 = datetime.datetime(2012 , 6 , 17)

print(ora1)

print(adesso.strftime("%B"))
print(adesso.strftime("%d/%m/%Y"))