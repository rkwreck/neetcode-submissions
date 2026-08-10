class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # first we can just sort the list
        nums_ = sorted(nums)

        # the majojrity element must be at the n/2 index
        return nums_[len(nums_)//2]