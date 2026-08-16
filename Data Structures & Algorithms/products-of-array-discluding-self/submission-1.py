class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)

        prefix = 1

        # nums = [1, 2, 4, 6]

        for i in range(len(nums)): # get the product of all the numbers prior to i 
            output[i] = prefix   
            prefix *= nums[i] 
        
        suffix = 1
        for j in range(len(nums)-1, -1, -1):
            # print("this is suffix:")
            # print(suffix)
            output[j] *= suffix 
            suffix *= nums[j]

        return output 

# each time i add a number, make a pass thru the entire array and multiply the array by that number


# 2 * 4 * 6
# 1 * 4 * 6
# 1 * 2 * 6
# 1 * 2 * 4 

