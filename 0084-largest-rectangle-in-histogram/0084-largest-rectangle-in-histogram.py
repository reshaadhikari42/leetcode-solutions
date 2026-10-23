class Solution:
    '''
in order to complete it in linear time, we have to use stacks. monotonic decreasing stack
my idea is use two stacks: left and right. we also use two arrays: leftBoundary and rightBounday
we add [heights[i], index] in stack and while popping we fill the boundary arrays
we do this twice in linear time for both left and right

after that we have left and right boundary for each bar so we clculate the area. this isn't super intuitive..
this should be linear but implementing can't be so easyy... lets try.
'''
    def largestRectangleArea(self, heights: list[int]) -> int:
        left_stack = []
        right_stack = [] #last element is the biggest at first
        left_boundary =  [0]*len(heights)
        right_boundary = [0]*len(heights)

        #first right bounday
        for i in range(len(heights)-1,-1,-1):
            if not right_stack or (right_stack and heights[i] > right_stack[-1][0]):
                right_boundary[i] = i
                right_stack.append([heights[i], i])
            else:
                while right_stack and heights[i] <= right_stack[-1][0]:
                    height, pos = right_stack.pop()
                right_boundary[i] = pos
                right_stack.append([heights[i], pos])

        #now left boundary
        for i in range(len(heights)):
            if not left_stack or (left_stack and left_stack[-1][0] < heights[i]):
                left_stack.append([heights[i],i])
                left_boundary[i] = i
            else:
                while left_stack and left_stack[-1][0] >= heights[i]:
                    height, pos = left_stack.pop()
                left_boundary[i] = pos
                left_stack.append([heights[i],pos])

    #now we have both left and right boundary
        max_area = 0
        for i in range(len(heights)):
            max_area = max(max_area, (right_boundary[i] - left_boundary[i] + 1)*heights[i])

        return max_area