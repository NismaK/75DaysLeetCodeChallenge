class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Calculate the sum of the first window
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        # Slide the window through the array
        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, window_sum)
        
        # Return the maximum average
        return max_sum / k