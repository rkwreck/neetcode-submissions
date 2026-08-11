class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        output = []
        dict_ = {} # for the subbuckets 

        for word in strs:
            key = tuple(sorted(word)) # sorted always returns a list, convert to tuple since dict keys    can't be lists
            
            if key not in dict_:
                dict_[key] = []  # create a new sublist 
            
            #regardless, add the current word 
            dict_[key].append(word)


        for bucket in dict_.values():
            output.append(bucket)
        
        return output






























        # output = []

        # # make it easier by sorting by length
        # strs = sorted(strs, key=len)

        # # use a sliding window approach 
        # left = 0
        # right = 1 

        # while (right <= len(strs)):
        #     sublist = []

        #     word = strs[left] 
        #     sublist.append(word)

        #     while ((right <= len(strs)-1) and (left < right) and (len(strs[left]) == len(strs[right]))):
        #         if sorted(list(strs[left])) == sorted(list(strs[right])):
        #             sublist.append(strs[right])
                
        #         right += 1
            
        #     output.append(sublist)
        #     left = right
        #     right += 1

        # return output 
























                

            

        