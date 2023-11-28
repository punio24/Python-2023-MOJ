range(10)

list(range(10))

(x * x for x in range(10))

[x for x in range(10)]      # generatpor

[x * x for x in range(10)]      # generator mnozenia kazdej liczby z zakresu przez te liczbe

[x for x in range(10) if x % 2 == 0]        # generator mnozenia tylko liczb parzystych przez nia sama

[x * x for x in range(10) if x % 2 == 0]        # modulo, tylko dla liczb parzystych od 0 do 10
[x * x for x in range(10) if x % 2 != 0]        # modulo, tylko dla liczb NIEparzystych od 0 do 10

[(x, y, x * y) for x in range(3) for y in range(4)] # mnozenie przez te sama liczbe , na III miejscu wynik. Z dwuch zakresow
                                                    # (0-3) oraz (0-4)

{x for x in range(10)}

{x // 2 for x in range(10)}

{x: x * x for x in range(10) if x % 2 == 0}     # wynik z dana liczba pomnozana przez te liczbe, ktra jest parzysta w ciagu

# ZADANIE
[x+6 for x in range (5)]
# ZADANIE 2
t = [(x, str(x)) for x in range(15)]        # czyli reprezentacja dwuch typow danych, liczby i i liczby jako znaku pisanego z zakresu 15
print(t)                                    # gdzie pamietamy ze 15 zawsze od 0, czyli 0-14
# ZADANIE 3
[x.upper() for x in s.keys() if s[x]>5000]
