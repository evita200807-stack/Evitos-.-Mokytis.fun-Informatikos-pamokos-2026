"""
Trikampio tikrinimas

Užduotis:
Įvesk 3 kraštines a, b, c ir patikrink,
ar galima sudaryti trikampį.

Taisyklė:
a + b > c
a + c > b
b + c > a
"""

a = int(input("Įvesk kraštinę a: ")) 
b = int(input("Įvesk kraštinę b: ")) 
c = int(input("Įvesk kraštinę c: "))
a + b > c and a + c > b and b + c > a: 
 print("Galima sudaryti trikampį") 
else:
     print("Negalima sudaryti trikampio")
