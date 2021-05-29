class Solution:
    def isPalindrome(self, s: str) -> bool:
        sliceGroup = []
        for slice in s :
            if(slice.isalnum() == True):
                sliceGroup.append(slice.lower())
        for slice in range(0, int(len(sliceGroup)/2)):
            if (sliceGroup[slice] != sliceGroup[len(sliceGroup)-1-slice]) :
                return False        
        return True

print(Solution.isPalindrome(Solution, "race a car"))