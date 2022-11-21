# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/7/7 21:28
import collections
from typing import List


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # 字符串按字典序排列
        products.sort()
        # 构建Trie树
        trie = {}
        dic = collections.defaultdict(list)
        for word in products:
            root = trie
            for i, c in enumerate(word):
                dic[word[:i + 1]].append(word)
                if c not in root:
                    root[c] = {}
                root = root[c]
        res = []
        # 搜索
        for i, c in enumerate(searchWord):
            res.append(dic[searchWord[:i + 1]][:3])

        return res
