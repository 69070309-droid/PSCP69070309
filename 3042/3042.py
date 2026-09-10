"""SGDSGDSGSGSG"""
import math
witpern = int(input())
situp = int(input())
looknung = int(input())
ving = int(input())
witpern1 = int(input())
situp1 = int(input())
ving1 = int(input())
looknung1 = int(input())
a2 = math.ceil(witpern / witpern1)
b2 = math.ceil(situp / situp1)
c2 = math.ceil(ving / ving1)
d2 = math.ceil(looknung / looknung1)
a = [a2, b2 ,c2, d2]
print(f"{max(a)}")