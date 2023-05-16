'''
Author: hakusai
Date: 2023-04-16 22:25:14
LastEditors: Do not edit
LastEditTime: 2023-04-18 00:15:22
FilePath: /Algorithm-study/每日一题_Py3/2023-04/17_2409. 统计共同度过的日子数.py
'''

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        a=max(arriveAlice,arriveBob)
        b=min(leaveAlice,leaveBob)
        days=(31,28,31,30,31,30,31,31,30,31,30,31)
        x=sum(days[:int(a[:2])-1])+int(a[3:])
        y=sum(days[:int(b[:2])-1])+int(b[3:])
        return max(y-x+1,0)
    
