ilość_osób=int(input("Podaj ilość osób: "))
ilość_potraw=int(input("Podaj ilość potraw: "))

suma = 0
i = 0

while i < ilość_potraw:
    cena = float(input("Podaj cena: "))
    suma += cena
    i += 1

średnia = suma / ilość_potraw
na_osobę = suma / ilość_osób

print(f"Średnia cena zamówionej potrawy: {round(średnia, 2)}")
print(f"Kwota na osobę:{round(na_osobę,2)}")