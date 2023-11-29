import sys

f = None

try:
    f = open('plik.txt', 'a')
    f.write("Hello\n")
except Exception as e:
    print("Bląd")
    print(type(e))
    print(e)
finally:
    if f is not None:
        f.close()

#  f = open('plik.txt', 'a')   a -append dopisuje, w- write zapisuje, czyli nadpisze jak w Linuxie

# https://docs.python.org/3/library/contextlib.html
# konteksty   __enter__() and __exit__()

# ZADANIE: dodatki z czego skorzystac
#import os
#print(os.getcwd())
#Help | Edit Custom Properties
#ide.browser.jcef.gpu.disable=true

# na poziomie terminala: (venv) PS C:\Users\localadmin\Desktop\MOJ\15_Pliki_tekstowe> python .\write_check.py .\data\foods.csv
# C:\Users\localadmin\Desktop\MOJ\15_Pliki_tekstowe

import csv
import os
import sys
print(os.getcwd())
tab = '\t'
n = 0
with open(sys.argv[1]) as csvfile:
    for line in csvfile:
        print(f'{n:03d} {tab.join(line.strip().split(","))}')
        n +=1

# albo:

import csv
import os
print(os.getcwd())
tab = '\t'
n = 0
with open('data\\foods.csv') as csvfile:
    for line in csvfile:
        print(f'{n:03d} {tab.join(line.strip().split(","))}')
        n +=1


