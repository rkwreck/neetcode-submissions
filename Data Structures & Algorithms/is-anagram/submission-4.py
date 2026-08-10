class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # convert both strings to sorted lists
        # if the lists are the same then it's an anagram

        s_list = sorted(list(s))
        t_list = sorted(list(t))


        if (s_list == t_list):
            return True

        return False 
        