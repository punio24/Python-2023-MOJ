for i in range(12):
    print(i)

for i in range(3, 12): # do 12 pozycji, ale wypada 11 bo w paythonie zawsze zaczynamy od 0 i do 11 jest 12 pozycji
    print(i)

for i in range(3, 12, 2):   ## trzeci element co o ile robimy krok
    print(i)

for c in "Ala ma kota":
    print(c)

for i in range(10):
    print(i)
else:
    print("Koniec")

for i in range(10):
    print(i)
    if i > 6:
        break
else:
    print("Koniec")

# zadanie

liczba = input("podaj liczbe: ")
suma_cyfr = 0
for cyfra in liczba:
    suma_cyfr += int(cyfra)
print (f"Suma cyfr liczby {liczba} wynosi: {suma_cyfr}")

### albo:
n = int(input("Podaj liczbę:"))
print(f'Podałeś liczbę {n}')

suma = 0
while n > 0:
    suma += n % 10
    n //= 10

print(suma)