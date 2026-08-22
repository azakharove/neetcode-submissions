class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        if n == 0:
            return False
        while n != 1:
            sum = 0
            dig = [int(digit) for digit in str(n)]
            print(dig)
            for num in dig:
                sum += num ** 2
                print(sum)
            if sum == 1:
                return True
            if sum in seen:
                return False
            seen.add(sum)
            n = sum
        if n == 1:
            return True