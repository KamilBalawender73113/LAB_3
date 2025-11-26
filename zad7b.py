studenci = int(input("Podaj liczbę studentów: "))

suma = 0
i = 0

while True:
    punkty=float(input("Podaj liczbę punktów zdobytych przez studenta: "))
    if punkty < 0 or punkty > 100:
        print("Punkty poza zakresem")
        continue
    suma += punkty
    i += 1

    if i == studenci:
        break

srednia = suma / punkty
print(f"Średnia punktów: {round(srednia, 2)}")