l = list(range(5, 10))
print(l)
try:
    i = int(input("podaj indeks "))
    print(f'Pod indeksem {i} jest element {l[i]}')
except IndexError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print("InException")
    print(e)
else:
    print("Koniec")
finally:
    print("Finally")


# kazdy blad ktory moze wystapic, powinien byc pisany w bloku osobno, czyli except jeden po drugim. na koncu powwinismy dawac
# exception, bo na poczatku zawsze wystapi i inne bledy ktore moga wystapic, nie zostana zwrocone w komunikacie