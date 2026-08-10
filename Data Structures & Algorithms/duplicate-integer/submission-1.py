class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        for i in range(len(nums)):
            for j in range(len(nums)):
                print('this is j: ')
                print(j)
                if (i != j) & (nums[i] == nums[j]):
                    return True
        return False



        # for i in range(len(nums) - 1): 
        #     if nums[i] == nums[i + 1]:
        #         return True
        # return False 
