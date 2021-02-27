import random
import time

'''
Sortowanie rekurencyjne, "divide and conquer"; Dzielimy listę na połówki, dopóki nie otrzymamy list jednoelementowej,
następnie "łączymy" wszystkie listy w jedną, wiedząc, że najmniejsza liczba w każdej z list znajduje się na początku.
Taka sytuacja umożliwia nam tworzenie posortowanych list porównując tylko kolejne liczby z łączonych list
'''


def megre_sort(array):
    # podział list na pół, jeśli lista jest więcej niż jednoelementowa
    if len(array) > 1:
        middle = len(array) // 2

        left = array[:middle]
        right = array[middle:]

        megre_sort(left)
        megre_sort(right)

        # zerowanie indeksów list
        i = j = k = 0

        # dopóki długość list left i right przewyższa kolejno wartość indeksu "i" i "j", dostawiamy kolejne liczby do
        # posortowanej listy, następnie zwiększamy indeks "k" posortowanej listy
        while len(left) > i and len(right) > j:
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        # jeśli pozostają elementy tylko z jednej z list, dodajemy je kolejno do posortowanej listy
        while len(left) > i:
            array[k] = left[i]
            i += 1
            k += 1
        while len(right) > j:
            array[k] = right[j]
            j += 1
            k += 1


to_sort = [random.randrange(0, 10000) for _ in range(20)]
print(to_sort)

t0 = time.time()
megre_sort(to_sort)
t1 = round(time.time() - t0, 4)

print(f"Answer: {to_sort}")
print(f"Computed in: {t1}")
