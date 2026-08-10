class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # put everything into a set 
        # if the set length is greater than the og nums length
        # we have a duplicate 

        nums_set = set(nums)
        # print("nums set:")
        # print(nums_set)

        if (len(nums_set) < len(nums)):
            return True; 

        return False; 
        