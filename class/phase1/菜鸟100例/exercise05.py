# L = [1]
# L = [1,1]
# L = [1,2,1]
# L = [1,3,3,1]
# L = [1,4,6,4,1]
# L = [1,5,10,10,5,1]

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
    def __init__(self):
        self.L = []
        self.L_all = []
    def L_more(self,times):
        fun_L = self.L[:]
        L_start = 0
        self.L.clear()
        for item in fun_L:
            self.L.append(L_start + item)
            L_start = item
        self.L.append(1)
        times -= 1
        self.L_all.append(self.L[:])
        if times <= 0:
            return
        self.L_more(times)

st = Solution()
st.L_more(5)
print(st.L_all)