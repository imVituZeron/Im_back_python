s1 = {1,2,2,3,4,5}
s2 = {4,5,6,7,8,9}
s3 = s1 | s2 # union
s4 = s1 & s2 # items in both
s5 = s1 - s2 # Items that exist only in left
s6 = s1 ^ s2 # Items that not exist in both
print(s3)
print(s4)
print(s5)
print(s6)