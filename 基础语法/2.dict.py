# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/9/27 09:46

if __name__ == '__main__':
    try:
        map = dict()
        map["AAA"] = 8
        map["AAB"] = 8
        map["AAC"] = 8
        map["AAD"] = 8
        map["AAA"] = 8
        pass
        del map["BBB"]
        pass
        map.clear()

        print(map["AAA"])
    except:
        print(1)
        print(len(map))
        print(type(map))
        print(str(map))
        print(map.popitem())
        print(map.values())
        map2 = map.copy()
        try:
            map.update(map2)
        except:
            pass

        print(122131, end=',')
        print(122131, end=',')
