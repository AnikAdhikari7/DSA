def selection_sort(arr, n):
    for i in range(n-1):
        mini = i

        for j in range(i+1, n):
            if arr[j] < arr[mini]:
                mini = j

        if min != i:
            arr[mini], arr[i] = arr[i], arr[mini]


n = int(input('What will be the length of the array? '))

arr = [n] * n

for i in range(n):
    arr[i] = int(input())

selection_sort(arr, n)
print(arr)
