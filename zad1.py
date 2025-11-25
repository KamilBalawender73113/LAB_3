paliwo= 100
paliwo_zużyte_na_s= 10
czas= 0

while paliwo >= 0:
    print(f"Stan samolotu: paliwo {paliwo}l, czas {czas}s")
    paliwo -= paliwo_zużyte_na_s
    czas += 1
else:
    print("Koniec lotu.")
