import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        
        #special to space, lower
        sliceGroup=[]
        for idx, char in enumerate(paragraph):
            if not re.match("[a-zA-Z ]", char):
                sliceGroup.append(" ")
                continue    
            sliceGroup.append(char.lower())
        sliceGroup = ''.join(sliceGroup).split()

        # preprocessing for banned
        sliceBannedGroup = ''.join(banned).lower().split()
        # counter
        counter, value = 0, ""
        for slice in sliceGroup:
            if banned.count(slice) != 0:
                continue
            if counter < sliceGroup.count(slice):
                counter = sliceGroup.count(slice)
                value = slice
        #print(counter, value)
        return value

#paragraph = "Bob"
#banned = []
#paragraph = "a, a, a, a, b,b,b,c, c"
#banned = ["a"]
#paragraph = "Bob hit a ball, the hit BALL flew far after it was hit." 
#banned = ["hit"]
paragraph = "Bob. hIt, baLl"
banned = ["bob", "hit"]
print(Solution.mostCommonWord(Solution, paragraph, banned))

