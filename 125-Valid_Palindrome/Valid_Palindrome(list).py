class Solution:
    def isPalindrome(self, s: str) -> bool:
        sliceGroup = []
        for slice in s: #preprocessing for alphanumeric transition
            if slice.isalnum():
                sliceGroup.append(slice.lower())

        while len(sliceGroup)>1:
        # python pop() : The argument passed to the method is optional. 
        # If not passed, the default index -1 is passed as an argument (index of the last item)
            if sliceGroup.pop(0) != sliceGroup.pop(): # first slice and last slice is popped
                return False
        return True

print(Solution.isPalindrome(Solution, "race a car"))
