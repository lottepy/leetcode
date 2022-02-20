class Solution:
        # Method 2: Greedy     
        # Method 2: Greedy     
        def maxArea(self, height: list[int]) -> int:
            def container(lower, higher):
                res = height[lower] * abs(lower - higher)  
                while lower != higher:
                    if lower < higher:
                        lower += 1
                    else:
                        lower -= 1 
                    if height[lower] > height[higher]:
                        lower, higher = higher, lower 
                    res = max(res, height[lower] * abs(lower - higher))
                return res  

            if height[0] < height[-1]:
                return container(0, len(height) - 1)
            else:
                return container(len(height) - 1, 0)   