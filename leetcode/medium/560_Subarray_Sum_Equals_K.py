class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hMap = defaultdict(int)
        hMap[0] = 1

        preSum = cnt = 0

        for n in nums:
            preSum += n
            diff = preSum - k
            cnt += hMap[diff]
            hMap[preSum] += 1

        return cnt