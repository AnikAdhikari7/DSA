class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posIndex, negIndex = 0, 1
        ans = [0] * len(nums)

        for i in nums:
            if i > 0:
                ans[posIndex] = i
                posIndex += 2
            else:
                ans[negIndex] = i
                negIndex += 2

        return ans