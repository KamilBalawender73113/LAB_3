def zad9():

    imie = str(input("Podaj imie: "))
    print(f"Witaj {imie}")

    wiek = int(input("Podaj wiek: "))
    print(f"Witaj {wiek}")

    nazwisko = str(input("Podaj nazwisko: "))
    print(f"Witaj {nazwisko}")

    inicjaly = imie[0].upper() + nazwisko[0].upper()
    print(f"Inicjaly: {inicjaly}")

    lancuch = str(input("Podaj lancuch: "))
    for i in range(5):
        print(lancuch * 5)

    ciag = imie + nazwisko
    print(ciag)

    dlugosc = int(round(len(ciag)/2,0))
    print(ciag[0:dlugosc])


zad9()