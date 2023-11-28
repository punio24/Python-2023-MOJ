z = set(range(10))      # podbne do slownikow, ale tam pary sa rozdzielone, tu mamy zbior rozdzielony przecinkiem
z
z = {1, 2, 3, 4, 1, 2}  # 1 i 2 nie wysapi, bo jest juz na poczatku, wiec w zbirze nie powiel sie
z
z = {'a', 'b', 'c'}
z
'a' in z
'd' in z
'd' not in z
z2 = {'a', 'b', 'c', 'd'}
z < z2
z3 = {'d', 'e'}
z | z3      # suma zbioru
z & z2      # czesc wspolna czyli przeciecie
z & z3
z2 - z      # roznica
z2 ^ z3     # roznica symetryczna zboirow, z odjeta czescia wspolna

z3.add('z')     # dodanie zbioru z
z3

slownik = {z: 3}  # Błąd
fz = frozenset(z)
slownik = {fz: 3}
slownik


