class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_ = {}
        for num in nums:
            dict_[num] = 1 + dict_.get(num, 0) # add one to her current frequency

        # create new buckets 
        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])
        
        # fill in these buckets
        # buckets hold each number's frequency 
        for num, freq in dict_.items():
            buckets[freq].append(num)
        
        output = []
        for i in range(len(buckets)-1, 0, -1): # most freq to last freq, so iterate from end

            # for each bucket label, keep adding that number to our output
            # once we've reached length k, we know we have the k most elements 
            for bucket in buckets[i]: # for each bucket label 
                output.append(bucket)
                if len(output) == k:
                    return output

        return output  
