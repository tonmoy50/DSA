class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = list()
        max_area = 0
        for i,height in enumerate(heights):
            if len(stack):
                if stack[-1][1] <= height:
                    stack.append([i, height])
                else:
                    idx = i
                    while stack and stack[-1][1] > height:
                        idx, h = stack.pop()
                        max_area = max(max_area, (i-idx)*h)
                    stack.append([idx, height])

            else:
                stack.append([i, height])
        if stack:
            for i, height in stack:
                max_area = max(max_area, (len(heights) - i)*height)

        return max_area