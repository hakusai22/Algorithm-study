# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/7/7 21:21
from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for d in dictionary:
            trie.insert(d)
        words = sentence.split(" ")
        return " ".join(trie.find_sp(word) for word in words)


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for w in word + "#":
            if w not in node:
                node[w] = {}
            node = node[w]

    def find(self, word):
        node = self.root
        for i in range(len(word)):
            if "#" in node:
                if self.find(word[i:]):
                    return True
            if word[i] in node:
                node = node[word[i]]
            else:
                return False
        return "#" in node

    def find_sp(self, word: str) -> str:
        node = self.root
        for i in range(len(word)):
            if "#" in node:
                return word[:i]
            if word[i] in node:
                node = node[word[i]]
            else:
                break
        return word
