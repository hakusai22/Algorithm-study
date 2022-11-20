# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/23 08:58
from collections import Counter
from typing import List


class Solution:
    def findSubstring(s: str, words: List[str]) -> List[int]:
        if not s or not words: return []
        one_word = len(words[0])
        all_len = len(words) * one_word
        n = len(s)
        words = Counter(words)
        res = []
        for i in range(0, n - all_len + 1):
            tmp = s[i:i + all_len]
            c_tmp = []
            for j in range(0, all_len, one_word):
                c_tmp.append(tmp[j:j + one_word])
            if Counter(c_tmp) == words:
                res.append(i)
        return res


if __name__ == '__main__':
    print(list(findSubstring("barfoothefoobarman", ["foo", "bar"])))
