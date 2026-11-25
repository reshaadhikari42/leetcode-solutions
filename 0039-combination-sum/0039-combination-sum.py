class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        subset, res = [], []
        
        def dfs(i, currSum):
            if currSum == target:
                res.append(subset.copy())
                return

            if i == len(candidates) or currSum > target:
                return

            subset.append(candidates[i])
            dfs(i, currSum + candidates[i])  #include candidates[i]

            subset.pop()
            dfs(i+1, currSum) #exclude candidates[i]

        dfs(0, 0)
        return res
            
