class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        def generaterow(row):
            ans = 1
            ansRow = []
            ansRow.append(1)
            for c in range(1,row):
                ans *= (row - c)
                ans //= c
                ansRow.append(ans)
            return ansRow

        ans = []
        for i in range(1,numRows+1):
            temp = generaterow(i)
            ans.append(temp)
        return ans




