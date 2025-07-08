def printLeaders(arr, n):
    ans = []

    max_ele = arr[n-1]
    ans.append(arr[n-1])

    for i in range(n-2, -1, -1):
        if arr[i] > max_ele:
            max_ele = arr[i]
            ans.append(max_ele)

    return ans


# Main function
if __name__ == '__main__':
    # Array Initialization
    n = 6
    arr = [10, 22, 12, 3, 0, 6]

    ans = printLeaders(arr, n)

    for i in range(len(ans)-1, -1, -1):
        print(ans[i], end=" ")

    print()