from functools import lru_cache
class Solution:
    @lru_cache(maxsize = None)
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n - 1 >= 0 and n - 2 >= 0:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
        else:
            return 1