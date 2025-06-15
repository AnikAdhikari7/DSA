def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while arr[i] <= pivot and i < high:
            i += 1
        
        while arr[j] > pivot and j > low:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j


def quick_sort(arr, low, high):
    if low < high:
        pIndex = partition(arr, low, high)
        quick_sort(arr, low, pIndex - 1)
        quick_sort(arr, pIndex + 1, high)


n = int(input('What will be the length of the array? '))

arr = [n] * n

for i in range(n):
    arr[i] = int(input())

quick_sort(arr, 0, len(arr) - 1)
print(arr)