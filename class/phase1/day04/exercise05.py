L = [12,59,84,17,26,51,36,72]

max = L[0]
min = L[0]
# for x in L:
#     if max < x:
#         max = x

for i in range(1,len(L)):
    if max < L[i]:
        max = L[i]

for i in range(1,len(L)):
    if min > L[i]:
        min = L[i]

print(min)
print(max)



