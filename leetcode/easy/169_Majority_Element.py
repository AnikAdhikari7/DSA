# Brute Force
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i in nums:
            count = 0

            for j in nums:
                if j == i:
                    count += 1

            if count > (len(nums) // 2):
                return i

        return -1


# Better Approach
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}

        for i in nums:
            hashMap[i] = hashMap.get(i, 0) + 1

        for key, val in hashMap.items():
            if val > (len(nums) // 2):
                return key

        return -1


# Optimal Solution
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        val = 0
        cnt = 0

        for i in nums:
            if cnt == 0:
                val = i
                cnt += 1
            elif val == i:
                cnt += 1
            else:
                cnt -= 1

        if cnt <= 0:
            return -1
        
        count = 0
        
        for i in nums:
            if val == i:
                count += 1

        if count > (len(nums) // 2):
            return val

        return -1


