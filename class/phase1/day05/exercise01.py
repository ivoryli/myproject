L1 = list(range(1,11))
L2 = [x for x in L1 if x % 2 ==1]
L3 = [x for x in L1 if x % 2 ==0]
L4 = [x for x in L1 if x >3]
print("%r \n%r \n%r"%(L2,L3,L4))