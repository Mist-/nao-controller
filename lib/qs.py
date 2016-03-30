class Solution:

    def __init__(self):
        pass

    def solve(self, A):
        self.qs(A, 0, len(A) - 1)
        print A
        pass

    def qs(self, A, left, right):
        if left >= right:
            return
        key = A[left]
        i = left
        j = right
        while i < j:
            while i < j and A[j] > key:
                j -= 1
            A[i] = A[j]
            while i < j and A[i] <= key:
                i += 1
            A[j] = A[i]
        A[i] = key
        self.qs(A, left, i - 1)
        self.qs(A, i + 1, right)

Solution().solve([2, 5, 6, 5, 10, 8])