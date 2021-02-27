import time
import random

'''
Iterujemy po liście od indeksu 1 (drugi element), zapamiętujemy jego wartość i kolejno porównujemy z poprzednimi 
elementami. Jeśli wartość zapamiętanego elementu jest mniejsza od kolejnego przyrównanego elementu, przyrównany element
przesuwamy o jedno miejsce do przodu na liście. Jeśli zapamiętany element jest większy wstawiamy go w miejsce o indeksie
i - 1. 
'''

array = [random.randrange(0, 10000) for _ in range(20)]
print(array)

t0 = time.time()

for i in range(1, len(array)):
    value = array[i]
    j = i - 1
    while j >= 0 and value < array[j]:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = value

t1 = round(time.time() - t0, 6)
print(f"Answer: {array}")
print(f"Computed in: {t1}")
