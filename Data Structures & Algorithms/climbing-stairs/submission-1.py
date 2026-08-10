class Solution:
    def climbStairs(self, n: int) -> int:

        # at every step you either climb 1 or 2 stairs
        # for each step, you now have to evaluate what all possible options are after that
        # add one to your total counter for each possibility 
        # we can store each option in an array? i'm actually not sure how you write a memoization in code 
        # base case: you take 0 steps 

        # LEARNING: 
        # to memoize, create a CACHE at -1
        cache = [-1] * n

        def dp(i): # one dimensional, so just pass in i
            # base case: we've reached the top 
            if (i == n):
                return 1 # we've reached a valid path 

            # base case: we're going beyond the top 
            if (i > n):
                return 0 # we've reached an invalid path 


            # otherwise: we still have stairs left to climb ! yahoo! 
            # obviously, i < n at this point
            # so we just need to check if we need to redo the calculation or not
            if (cache[i] != -1):
                return cache[i]

            # now, i'm currently on step i
            # either take 1 step from here, to land me on i + 1
            # or take 2 steps from here, to land me on i + 2 
            # and then calculate the routes from here
            # so that's what this means: 
            cache[i] = dp(i + 1) + dp(i + 2) # add it to the cache since it doesn't already exist 

            return cache[i]

        return dp(0)