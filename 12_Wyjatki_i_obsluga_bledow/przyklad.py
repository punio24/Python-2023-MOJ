l = list(range(5, 10))
print(l)
i = int(input("podaj indeks "))
print(f'Pod indeksem {i} jest element {l[i]}')

# ZADANIE:

try:
    i = int(input("Podaj liczbe :"))
    suma_cyfr = sum(int(a) for a in str(i))
    print("Suma cyfr", suma_cyfr)
except ValueError as e:
    print("zla liczba, podaj kolejna:")
    print(e)
except Exception as a:
    print(e)
else:
    print("Koniec")
finally:
    print("Finaly")

# ZADANIE z brake'iem

liczba = 0
while True:
    try: liczba = input("Podaj liczbę naturalną: ")
         liczba = int(liczba)
    except ValueError as e:
        print (f"{liczba} nie jest liczbą!")
    else:
        break

suma = 0
i = liczba
while i > 0:
    suma += i%10
    i //= 10
print (f'Suma cyfr podanej liczby {liczba} wynosi {suma}')

# syntsax erro, sprawdzic wciecia kodu

