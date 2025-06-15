def insertion_sort(arr, n):
    for i in range(len(arr)):
        j = i

        while(j > 0 and arr[j-1] > arr[j]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1


n = int(input('What will be the length of the array? '))

arr = [n] * n

for i in range(n):
    arr[i] = int(input())

insertion_sort(arr, n)
print(arr)
