l = [3, 5, 6, 7]
l

l[1]   # wyjdzie 5 bo w Pythonie liczymy od 0, zatem 5 liczb
l[0]
len(l) # ile ma lista elementow
l[0:2] # tu do rozwiniecia temat
l[1:2]
l[1:]
l[:2]
l[-1]
l[2:-1] # bedzie od 3go elementu, nie uwzgledniajac ostatniego
l[-4]
l[1:-1] + l[0:-1]

for i in range(len(l)):
    print(l[i])
# to jest to samo ale prosciej zapisane:

for i in l:
    print(i)

l * 4

l.index('3')  # Błąd
l.index(3)    # pyta o argument na ktorej pozycji jest 3, a poniewaz jej nie ma to zwraca 0

l[1] = 17
l
del l[3]
l
l.append(19)
l
l += ['A', 'B']
l
l.pop() # usuwa domyslnie ostatnia pozycje na najwyzszym indexie
l

" - ".join(["Ala", "ma", "kota"]) # rozdziela liste myslnikiem, jakikolwiek znak mozna dac
"".join(["Ala", "ma", "kota"])  # skleja liste
" ".join(["Ala", "ma", "kota"]) # skleja liste spacjami
s2 = '.|.'
s2.join(["Ala", "ma", "kota"]) # rozdziela .|.

'.' in s2

l.insert(2, 100) # wstawienie 100 na pozycji 2

# ZADANIE:
napisy = []

while True:
    napis = input("Wprowadź dowolne słowo: ")

    if not napis:
        break

    napisy.append(napis)

print(napisy)