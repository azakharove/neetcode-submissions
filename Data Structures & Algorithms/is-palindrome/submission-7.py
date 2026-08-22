class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(filter(str.isalnum, s))
        print(s)
        s2 = s[::-1]
        print(s2)
        return s == s2
