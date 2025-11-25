ulice = ["Jagodowa","Lipowa","Kwiatowa","Kasztanowa","Polna"]

for ulice in ulice:
    for blok in range(1,6):
        for mieszkanie in range (1,11):
            print(f'{ulice} {blok}/{mieszkanie}')