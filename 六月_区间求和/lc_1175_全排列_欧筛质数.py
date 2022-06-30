# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/30 08:37

MOD = int(1e9) + 7


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        return Solution.factorial(cnts := Solution.euler(n)) * Solution.factorial(n - cnts) % MOD

    # 欧式筛统计素数个数
    @staticmethod
    def euler(x):
        is_prime = [True] * (x + 1)
        is_prime[1] = False
        count = 0
        prime = [0] * (x + 1)
        for i in range(2, x + 1):
            if is_prime[i]:
                count += 1
                prime[count] = i
            j = 1
            while j <= count and i * prime[j] <= x:
                is_prime[i * prime[j]] = False
                if not i % prime[j]:
                    break
                j += 1
        return count

    @staticmethod
    @lru_cache(None)
    def factorial(x):
        return 1 if x <= 1 else x * Solution.factorial(x - 1) % MOD
