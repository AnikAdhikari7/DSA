"""
Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.

Examples:

    Input: nums = [10, 5, 2, 7, 1, 9],  k=15

    Output: 4

    Explanation: The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], which has a length of 4. This sub-array starts at index 1 and ends at index 4, and the sum of its elements (5 + 2 + 7 + 1) equals 15. Therefore, the length of this sub-array is 4.

    ---

    Input: nums = [-3, 2, 1], k=6

    Output: 0

    Explanation: There is no sub-array in the array that sums to 6. Therefore, the output is 0.
"""

# Longest Subarray with sum K | [Positives and Negatives]
def getLongestSubarrayPosNeg(arr, k):
    n = len(arr)

    preSumMap = {}
    sum = 0
    maxLen = 0

    for i in range(n):
        sum += arr[i]

        if sum == k:
            maxLen = max(maxLen, i + 1)

        rem = sum - k
        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxLen = max(maxLen, length)

        if sum not in preSumMap:
            preSumMap[sum] = i

    return maxLen


# Longest Subarray with given Sum K(Positives)
def getLongestSubarrayPos(arr, k):
    n = len(arr)

    left, right = 0, 0
    sum = arr[0]
    maxLen = 0

    while right < n:
        while left <= right and sum > k:
            sum -= arr[left]
            left += 1

        if sum == k:
            maxLen = max(maxLen, right - left + 1)

        right += 1
        if right < n: sum += arr[right]

    return maxLen

if __name__ == "__main__":
    # a = [-1, 1, 1]
    # k = 1
    a = [2, 3, 5, 1, 9]
    k = 10
    length = getLongestSubarrayPos(a, k)
    print(f"The length of the longest subarray is: {length}")