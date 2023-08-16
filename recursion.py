# Given an unsorted array arr[] of size N.
# Rotate the array to the left (counter-clockwise direction) by D steps, where D is a positive integer. 


class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):
        # self = Solution()
        # #Your code here
        # if(D==0):
        #     return A
        # temp = A.pop(0)
        # A.append(temp)
        # return self.rotateArr(A,D-1,N)
        if(D==0):
            return A
        l1 = list()
        for i in range(D,N,1):
            l1.append(A[i])
        return l1
        
N = int(input())
arr = list()
for i in range(N):
     x = int(input())
     arr.append(x)
print("Enter the step")
D = int(input())
ans = Solution().rotateArr(arr,D,N)
print(ans)
