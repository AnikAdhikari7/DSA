# first approach using sum of n natural number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nSum = (len(nums) * (len(nums) + 1)) // 2
        numsSum = 0
        
        for i in nums:
            numsSum += i

        return nSum - numsSum


# second and better approach using xor (bitwise operation / bit manipulation)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor1, xor2 = 0, 0

        for i, val in enumerate(nums):
            xor1 = xor1 ^ (i + 1)
            xor2 = xor2 ^ val

        return xor1 ^ xor2