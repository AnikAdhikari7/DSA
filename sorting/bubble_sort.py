def bubble_sort(arr, n):
    for i in range(n-1, -1, -1):
        swapped = False
        
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break


n = int(input('What will be the length of the array? '))

arr = [n] * n

for i in range(n):
    arr[i] = int(input())

bubble_sort(arr, n)
print(arr)
