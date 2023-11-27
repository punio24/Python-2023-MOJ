s = 'Ala ma {0} kotów'.format(5)
s

'Ala ma ' + str(5) + ' kotów'

s = 'Ala ma {0} kot{1}'.format(5, 'ów')
s

s = 'Ala ma {0} kot{1}'.format(4, 'y')
s

f'Pi to jest mniej więcej {3.1415926:.3}'  # :.3 tu interesuja mn ie tylko 3 znaki dziesietne

for i in range(12):
    print(f'{i:2}')

for i in range(12):
    print(f'{i:02}')

from math import pi
pi

f'{pi:.3}'
f'{pi:.3f}'  # f znaczy 3 znaki po przecinku
f'{pi-3:.3f}'
f'{12:3d}'
f'{12:03d}'
f'{pi:<30.2f}'
f'{pi:>30.2f}'
f'{pi:->30.2f}'
f'{pi:^30.2f}'
f'{"-"*10}HELLO{"-"*10}'
f'{"HELLO":-^25s}'


### zadanie choinka

wysokosc = int (input("Podaj wysokość choinki: "))
szerokosc = 1
for i in range (wysokosc):
    print (f'{"*"*szerokosc:^{wysokosc*2}}')
    szerokosc += 2
print (f'{"*":^{wysokosc*2}}')
print (f'{"***":^{wysokosc*2}}')

#### drugi sposob na choinke
level = int(input("Poziomy:").strip())
S = ' '
G = '*'
for i in range(level):
    poziom = S * (level-i-1) + (2 * i + 1) * G
    print(poziom)
for i in range(2):
    poziom = S * (level-i-1) + (2 * i + 1) * G
    print(poziom)