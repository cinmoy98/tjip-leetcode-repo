# Problem Link : https://leetcode.com/problems/detect-squares/
# Problem Number : 2013
# Problem Tag : Hash Map
# Author : Cinmoy Das (github : https://github.com/cinmoy98)
# Date : 29/04/2022

# Approach 1 --> Hashmap
# Time-complexity--> O(n), Space-Compllexity--> O(1)
################################################################


class DetectSquares:

    def __init__(self):
        self.pointDict = {}

    def add(self, point: List[int]) -> None:
        if (point[0],point[1]) not in self.pointDict:
            self.pointDict[(point[0],point[1])]=1
        else:
            self.pointDict[(point[0],point[1])]+=1

    def count(self, point: List[int]) -> int:
        cnt=0
        for pt in self.pointDict:
            if point[0]==pt[0] or (abs(point[0]-pt[0])!=abs(point[1]-pt[1])):
                continue
            if (pt[0],point[1]) in self.pointDict and (point[0],pt[1]) in self.pointDict:
                cnt += (self.pointDict[(pt[0],point[1])]*self.pointDict[(point[0],pt[1])]*self.pointDict[(pt[0],pt[1])])
        return cnt
