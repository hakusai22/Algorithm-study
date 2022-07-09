# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/7/8 07:58
import collections
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        st = set(wordList)
        if endWord not in st:
            return 0
        m = len(beginWord)

        queue = collections.deque()
        queue.append((beginWord, 1))

        visited = set()
        visited.add(beginWord)

        while queue:
            cur, step = queue.popleft()
            if cur == endWord:
                return step

            for i in range(m):
                for j in range(26):
                    tmp = cur[:i] + chr(97 + j) + cur[i + 1:]
                    if tmp not in visited and tmp in st:
                        queue.append((tmp, step + 1))
                        visited.add(tmp)

        return 0


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    print(arr[:1])
    print(arr[2:])
