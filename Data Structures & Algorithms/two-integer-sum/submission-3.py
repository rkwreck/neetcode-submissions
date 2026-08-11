class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # to account for duplicates we want to build the hashset as we go 
        # a hashset also can't provide us info on indices so it's not the way to go
        # use a dict instead with key as num and value as index (since we want the index and values can be returned)

        dict_ = {} 
        
        #hashset = set(nums)


        for i in range(len(nums)):
            j = target - nums[i]
            if (j in dict_):
                return [dict_[j], i] # not [i, dict_[j]], because dict_[j] is always the index i stored earlier
                #k = nums.index(j)
                #return [i, k]

            dict_[nums[i]] = i # otherwise add the (key=num, value=index) into the dict for later

            #hashset.add(nums[i])
    
        return [0]