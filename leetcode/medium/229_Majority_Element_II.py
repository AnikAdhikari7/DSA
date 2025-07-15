class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        el1 = el2 = float('-inf')
        cnt1 = cnt2 = 0

        for num in nums:
            if cnt1 == 0 and num != el2:
                el1 = num
                cnt1 += 1
            elif cnt2 == 0 and num != el1:
                el2 = num
                cnt2 += 1
            elif el1 == num: cnt1 += 1
            elif el2 == num: cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        ans = []

        cnt1 = cnt2 = 0

        for num in nums:
            if num == el1: cnt1 += 1
            if num == el2: cnt2 += 1

        if cnt1 > len(nums) // 3: ans.append(el1)
        if cnt2 > len(nums) // 3: ans.append(el2)

        return ans