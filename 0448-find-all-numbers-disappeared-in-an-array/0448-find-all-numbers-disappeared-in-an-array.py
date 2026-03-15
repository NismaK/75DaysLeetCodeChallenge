class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        y=len(nums)
        final=[]
        z=set(nums)
        for i in range(1,y+1):
            if i in z:
                continue
            else:
                final.append(i)
        return final

        