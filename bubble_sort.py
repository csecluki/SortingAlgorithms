import random
import time

'''
Bubble sort - porównujemy dwie kolejne, sąsiadujące ze sobą liczby (pierwsza z drugą, druga z trzecią itd.)
Jeśli pierwsza liczba z pary jest większa od drugiej, zamieniamy je miejscami, gdy jest równa lub mniejsza -
przechodzimy dalej. Ostatecznie, z każdą iteracją największa z nieposortowanych liczb ląduje na końcu nieposortowanej
listy
'''

array = [random.randrange(0, 10000) for _ in range(20)]
print(array)

t0 = time.time()
for j in range(len(array) - 1):
    for i in range(len(array) - 1 - j):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
t1 = round(time.time() - t0, 6)

print(f"Answer: {array}")
print(f"Computed in: {t1}")
