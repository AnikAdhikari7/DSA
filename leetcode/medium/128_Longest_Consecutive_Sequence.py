class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        hashSet = set()
        longest = 1

        for n in nums:
            hashSet.add(n)

        for i in hashSet:
            if i - 1 not in hashSet:
                cnt = 1
                x = i

                while x + 1 in hashSet:
                    cnt += 1
                    x += 1
                
                longest = max(longest, cnt)

        return longest