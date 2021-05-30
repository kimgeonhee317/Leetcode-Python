import collections
from typing import Collection


class Solution:
    def isPalindrome(self, s: str) -> bool:

        sliceGroup: Deque = collections.deque()

        for slice in s: #preprocessing for alphanumeric transition
            if slice.isalnum():
                sliceGroup.append(slice.lower())

        while len(sliceGroup)>1:
            if sliceGroup.popleft() != sliceGroup.pop():
                return False
        return True

print(Solution.isPalindrome(Solution, "asa"))
