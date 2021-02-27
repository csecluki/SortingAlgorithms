import random
import time

'''
Iterując po liście szukamy najmniejszej liczby (zapamiętujemy jej indeks), po dojściu do końca listy najmniejszą liczbę
zamieniamy miejscami z pierwszą nieposortowaną liczbą (indeks tej liczby to numer iteracji). Jest to w pewien sposób
odwrotność sortowania bubble sort, gdzie posortowane liczby znajdują się na początku, a nie końcu listy
'''

array = [random.randrange(0, 10000) for _ in range(20)]
print(array)

t0 = time.time()
for i in range(len(array)):
    min_index = i
    for j in range(min_index + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
t1 = round(time.time() - t0, 6)

print(f"Answer: {array}")
print(f"Computed in: {t1}")
