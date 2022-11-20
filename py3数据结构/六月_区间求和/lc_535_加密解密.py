# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/29 08:17


import hashlib


class Codec:
    def __init__(self):
        self.map = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        _md5 = hashlib.md5()
        _md5.update(longUrl.encode("utf-8"))
        res = _md5.hexdigest()
        self.map[res] = longUrl
        return f"http://tinyurl.com/{res}"

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.map[shortUrl.split("/")[-1]]
