import random
import time

'''
"divide and conquer"; Wybieramy jeden element - pivot (tu: ostatni element listy), następnie porównujemy kolejno
wszystkie elementy z pivotem. Elementy mniejsze pozostają przed pivotem, większe po pivocie. W rezultacie pivot znajduje
się na właściwym miejscu. Schemat powtarzamy dla wycinków list mniejszych i większych od pivota
'''


def partition(array, low, high):
    # i wskazuje na którym miejscu ostatecznie wyląduje pivot
    i = low - 1
    pivot = array[high]

    for j in range(low, high):
        if pivot > array[j]:
            # pivot większy od kolejnego elementu -> jego ostateczny indeks się przesuwa
            i += 1
            # uszeregowanie mniejszych/większych elementów od pivota
            array[i], array[j] = array[j], array[i]

    # wstawiamy pivota na właściwe miejsce
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)

        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)


to_sort = [random.randrange(0, 10000) for _ in range(20)]
print(to_sort)

t0 = time.time()
quick_sort(to_sort, 0, len(to_sort) - 1)
t1 = round(time.time() - t0, 6)

print(f"Answer: {to_sort}")
print(f"Computed in: {t1}")
