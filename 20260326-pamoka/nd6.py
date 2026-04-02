"""
Keliamieji metai

Užduotis:
Įvesk metus ir nustatyk ar jie keliamieji.

Metai keliamieji jei:
- dalinasi iš 400
arba
- dalinasi iš 4, bet nesidalina iš 100
"""
metai = int(input("Įveskite metus: ")) 
if (metai % 400 == 0) or (metai % 4 == 0 and metai % 100 != 0):
     print("Metai yra keliamieji") 
else: 
    print("Metai yra nekeliamieji")
