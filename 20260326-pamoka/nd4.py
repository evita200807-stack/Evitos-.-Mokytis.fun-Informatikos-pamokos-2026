"""
Dviženklio skaičiaus analizė

Užduotis:
Įvesk skaičių ir nustatyk ar jis dviženklis:
- jei skaičius nėra dviženklis išvesk "Skaičius nėra dviženklis"
- jei skaičius yra dviženklis, tuomet reikia:
    - nustatyti ar skaičius lyginis, ar nelyginis
    - ištraukti dešimčių skaitmenį
    - ištraukti vienetų skaitmenį
    - rasti jų sumą
    - pasakyti, kuris didesnis
    - sukurti atvirkštinį skaičių (apsukti skaitmenis)
    

Pvz.:

Įvesk skaičių: 23
Įvestas skaičius: 23
Skaičius yra dviženklis
Skaičius yra nelyginis
Dešimčių skaitmuo: 2
Vienetų skaitmuo: 3
Skaitmenų suma: 5
Didesnis yra vienetų skaitmuo: 3
Atvirkštinis skaičius: 32

''' 



Įvesk skaičių: 74
Įvestas skaičius: 74
Skaičius yra dviženklis
Skaičius yra lyginis
Dešimčių skaitmuo: 7
Vienetų skaitmuo: 4
Skaitmenų suma: 11
Didesnis yra dešimčių skaitmuo: 7
Atvirkštinis skaičius: 47


Įvesk skaičių: 5
Įvestas skaičius: 5
Skaičius nėra dviženklis

"""

skaicius = int(input("Įvesk skaičių: ")) 
if 10 <= skaicius <= 99: 
    print(f"Įvestas skaičius: {skaicius}") 
    print("Skaičius yra dviženklis") 
    if skaicius % 2 == 0: 
        print("Skaičius yra lyginis") 
    else: 
        print("Skaičius yra nelyginis")
     desimtys = skaicius // 10 vienetai = skaicius % 10 
     print(f"Dešimčių skaitmuo: {desimtys}")
     print(f"Vienetų skaitmuo: {vienetai}") 
     print(f"Skaitmenų suma: {desimtys + vienetai}") 
      if desimtys > vienetai: 
        print(f"Didesnis yra dešimčių skaitmuo: {desimtys}") 
        elif vienetai > desimtys: 
            print(f"Didesnis yra vienetų skaitmuo: {vienetai}")
             else:
             print("Skaitmenys yra lygūs") atvirkstinis = vienetai * 10 + desimtys 
             print(f"Atvirkštinis skaičius: {atvirkstinis}") 
             else:
             print("Skaičius nėra dviženklis")
