class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def generateRow(row):
            ansRow = [1]

            ans = 1

            for col in range(1, row):
                ans *= (row - col)
                ans //= col

                ansRow.append(ans)

            return ansRow

        ans = []

        for row in range(1, numRows + 1):
            ans.append(generateRow(row))

        return ans