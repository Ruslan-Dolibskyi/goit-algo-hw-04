import random
import timeit


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


def tim_sort(arr):
    return sorted(arr) 


# Creating datasets of different sizes
small_dataset = [random.randint(0, 100) for _ in range(100)]
medium_dataset = [random.randint(0, 100) for _ in range(1000)]
large_dataset = [random.randint(0, 100) for _ in range(10000)]

# Timing the sorting algorithms on different datasets
times = {}
for dataset_size, dataset in [("Small", small_dataset), ("Medium", medium_dataset), ("Large", large_dataset)]:
    times[f'Insertion Sort ({dataset_size})'] = timeit.timeit(lambda: insertion_sort(dataset.copy()), number=1)
    times[f'Merge Sort ({dataset_size})'] = timeit.timeit(lambda: merge_sort(dataset.copy()), number=1)
    times[f'Tim Sort ({dataset_size})'] = timeit.timeit(lambda: tim_sort(dataset.copy()), number=1)

print(times)
