# Largest Rectangle in Histogram.py
# Question: Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


#Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


#The largest rectangle is shown in the shaded area, which has area = 10 unit.

#For example,
#Given height = [2,1,5,6,2,3],
#return 10.
# Question from: https://oj.leetcode.com/problems/largest-rectangle-in-histogram/
# Sulotion:  
# Author: DongDing 
# Date: 2014/08/16
# Time complexity:  O(n) 
# space complexity:  O(n)  
# Tag: # Dynamic Programming # Stack # 
# Comment:

class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        if len(height) == 0:
            return 0
        
        result = 0
        left_list = [] #
        right_stack = [] #index
        left_list.append(-1)
        right_stack.append(0)
        for i in range(1,len(height)):
            if height[i-1] > height[i]:
                #conpute left boundary
                temp_left = left_list[i-1]
                while temp_left != -1:#height[i]<height[temp_left]:
                    if height[temp_left] < height[i]:
                        break                    
                    temp_left = left_list[temp_left]

                left_list.append(temp_left)
                #right boundary
                while right_stack and height[right_stack[-1]]>height[i]:
                    height_index = right_stack.pop()
                    left_index = left_list[height_index]
                    area = height[height_index] *  (i-1-left_index)
                    if result < area:
                        result = area                    
                    
                right_stack.append(i)
                
            elif height[i-1] < height[i]:
                #left boundary is determined
                left= i-1
                left_list.append(left)
                #right boundary
                right_stack.append(i)
                
            else:
                left = left_list[i-1]
                left_list.append(left)
                
                right_stack.append(i)
        while right_stack:
            height_index = right_stack.pop()
            left_index = left_list[height_index]
            area = height[height_index] *  (len(height)-1-left_index)      
            if result < area:
                result = area
            
        return result
    #def largestRectangleArea(self, height):
        ##DFS
        #self.height = height 
        #self.result = 0
        #self.dfs(0, len(height)-1)
        #return self.result
        
    #def dfs(self, left, right):        
        #if left == right:
            #area = self.height[left]
            #if area > self.result:
                #self.result = area 
            #return
        #min_index = self.findMin(left, right)
        #area = (right-left +1) * self.height[min_index]
        #if area > self.result:
            #self.result = area
        #if min_index != left:    
            #self.dfs(left, min_index-1)
        #if min_index != right:            
            #self.dfs(min_index+1, right)
        #return
        
        
        
        
        
    #def findMin(self,left,right):
        #if left == right:
            #return left
        #minx = self.height[left]
        #min_index = left
        #for i in range(left,right+1):
            #if self.height[i] < minx:
                #minx = self.height[i]
                #min_index = i
                
        #return min_index
 
 
 
height =  [4,2,0,3,2,5]
a = Solution()
print a.largestRectangleArea(height)

