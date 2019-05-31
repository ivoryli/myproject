def list_sort(L):
    for x in range(len(L) - 1):
        for y in range(x + 1,len(L)):
            if L[x] > L[y]:
                L[x],L[y] = L[y],L[x]
L = [2,5,9,1,11,18,21,4]
list_sort(L)
print(L)