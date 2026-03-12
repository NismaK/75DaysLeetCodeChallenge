class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sat=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    sat.append(i)
                    sat.append(j)
        return sat

        