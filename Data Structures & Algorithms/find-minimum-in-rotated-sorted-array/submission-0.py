class Solution:
    def findMin(self, nums: List[int]) -> int:

        # whatever half of the list is sorted in ascending order, never had the rotation point

        # the rotation point is when the maximum is right next to the minimum 

        output = nums[0]
        l = 0
        r = len(nums) - 1

        while (l <= r):
            if nums[l] < nums[r]: # is this entire slice still in ascending order ? 
                output = min(output, nums[l])  # nums[l] would be the smallest part of this slice
                break 
            
            midpoint = (l + r)//2
            output = min(output, nums[midpoint])

            if nums[midpoint] >= nums[l]: # figure out which half we need to keep checking
                l = midpoint + 1 
            else: 
                r = midpoint - 1 
            
        return output 