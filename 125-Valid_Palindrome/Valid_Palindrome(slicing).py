class Solution:
    def isPalindrome(self, s: str) -> bool:
        sliceGroup = []
        for slice in s: #preprocessing for alphanumeric transition
            if slice.isalnum():
                sliceGroup.append(slice.lower())

        if(sliceGroup != sliceGroup[::-1]): # ::-1 means reverse
            return False
        return True


print(Solution.isPalindrome(Solution, "race a car"))
