# Problem Link : https://leetcode.com/problems/design-hashmap/
# Problem Number : 706
# Problem Tag : Hash Map
# Author : Cinmoy Das (github : https://github.com/cinmoy98)
# Date : 29/04/2022

# Approach 1 --> Hashmap
# Time-complexity--> O(n), Space-Compllexity--> O(1)
################################################################

class MyHashMap:

    def __init__(self):
        self.HashMap = [-1]*1000001

    def put(self, key: int, value: int) -> None:
        self.HashMap[key] = value

    def get(self, key: int) -> int:
        if self.HashMap[key]==-1:
            return -1
        else:
            return self.HashMap[key]

    def remove(self, key: int) -> None:
        self.HashMap[key]=-1