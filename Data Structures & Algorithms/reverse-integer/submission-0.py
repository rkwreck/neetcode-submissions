class Solution:
    def reverse(self, x: int) -> int:
        min = -(2**31)
        max = (2**31) - 1

        num = ""
        exp = 1 

        x_list = list(str(x))
        sign = False

        for char in x_list[::-1]:
            if char == "-":
                sign = True 
            else:
                num += char
            if (int(num) < min) or (int(num) > max):
                print("in else statement")
                return 0 
    
        if (sign):
            return -1 * int(num)
        return int(num)
    