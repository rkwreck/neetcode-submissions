class Solution:

    def __init__(self):
        self.sizes = []

    def encode(self, strs: List[str]) -> str:
        self.sizes = []
        output = ""

        # account for empty edge case
        if len(strs) == 0: 
            return output 


        for string in strs:
            output += string 

            # but now also build the sizes list
            self.sizes.append(len(string))
        
        return output 


    def decode(self, s: str) -> List[str]:
        # if s == "" or s==" ":
        #     return [""]

        output = []
        counter = 0
        for size in self.sizes:
            # print("this is counter: ")
            # print(counter)
            # print("this is extract:")
            # print(s[counter:size:])
            # print("this is size")
            # print(size)

            output.append(s[counter:counter + size:])
            counter += size 
        
        return output 

        
