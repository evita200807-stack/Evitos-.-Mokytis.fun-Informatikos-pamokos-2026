"""
Sekundės į valandas, minutes ir sekundes

Užduotis:
Įvesk sekundžių skaičių ir paversk į:
- valandas
- minutes
- likusias sekundes

Pvz. 135:
- 0 val
- 2 min
- 15 sek

Pvz. 4953:
- 1 val
- 22 min
- 33 sek
"""
sekundes = int(input("Įvesk sekundžių skaičių: "))
valandos = sekundes // 3600 valandos = sekundes % 3600 
minutes = valandos // 60 sekundes = valandos % 60 
print(valandos, "val") 
print(minutes, "min")
 print(sekundes, "sek")
