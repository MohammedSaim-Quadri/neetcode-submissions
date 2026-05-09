class Solution:
    def Insert(self, A, val):
        A.append(val)
        i = len(A) - 1

        while i>0 and A[(i-1//2)] > A[i]:
            A[(i-1)//2], A[i] = A[i] , A[(i-1)//2]
            i = (i-1)//2

    def Remove(self, A):
        if len(A) == 1:
            return A.pop()

        temp = A[0]
        A[0] = A.pop()
        n = len(A)
        i = 0

        while True:
            s= i
            l = 2*i+1
            r = 2*i+2

            if l<n and A[l]< A[s]:
                s = l
            if r<n and A[r] < A[s]:
                s = r

            if s==i:
                break
            else:
                A[i], A[s] = A[s], A[i]
                i = s
        return temp

    def lastStoneWeight(self, stones: List[int]) -> int:
        A=[]
        for stone in stones:
            self.Insert(A, -stone)

        while len(A) > 1:
            x = self.Remove(A)
            y = self.Remove(A)

            if x!=y:
                new_w = abs(x-y)
                self.Insert(A, -new_w)

        if len(A) == 1:
            return -A[0]
        else:
            return 0
        