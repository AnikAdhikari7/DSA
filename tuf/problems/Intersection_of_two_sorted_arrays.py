def find_intersection(arr1, arr2):
    i, j = 0, 0
    intersection = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            intersection.append(arr1[i])
            i, j = i + 1, j + 1

    return intersection


arr1 = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

union = find_intersection(arr1, arr2)

print("Intersection of arr1 and arr2 is:")
print(*union)