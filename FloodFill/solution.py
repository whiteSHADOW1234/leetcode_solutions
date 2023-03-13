from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        rows = len(image)
        cols = len(image[0])
        source = image[sr][sc]
        self.dfs(image, sr, sc, color, rows, cols, source)
        return image
    
    def dfs(self, image: List[List[int]], sr: int, sc: int, color: int, rows: int, cols: int, source: int):
        if sr < 0 or sr >= rows or sc < 0 or sc >= cols:
            return
        if image[sr][sc] != source:
            return
        
        image[sr][sc] = color

        self.dfs(image, sr+1, sc, color, rows, cols, source)
        self.dfs(image, sr-1, sc, color, rows, cols, source)
        self.dfs(image, sr, sc+1, color, rows, cols, source)
        self.dfs(image, sr, sc-1, color, rows, cols, source)
        





# Simplified the floodFill function
# class Solution:
#     def dfs(self, image: List[List[int]], sr: int, sc: int, source: int, color: int):
#         if image[sr][sc] == source and image[sr][sc] != color:
#             image[sr][sc] = color
#             if sr > 0:
#                 self.dfs(image, sr-1, sc, source, color)
#             if sr < len(image) - 1:
#                 self.dfs(image, sr+1, sc, source, color)
#             if sc > 0:
#                 self.dfs(image, sr, sc-1, source, color)
#             if sc < len(image[0]) - 1:
#                 self.dfs(image, sr, sc+1, source, color)
        
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#         if image[sr][sc] == color:
#             return image

#         self.dfs(image, sr, sc, image[sr][sc], color)
#         return image



# Simplified the dfs function
# class Solution:
#     def dfs(self, image, sr, sc, source, color):
#         if image[sr][sc] == source and image[sr][sc] != color:
#             image[sr][sc] = color
#             for nr, nc in [(sr-1, sc), (sr+1, sc), (sr, sc-1), (sr, sc+1)]:
#                 if 0 <= nr < len(image) and 0 <= nc < len(image[0]):
#                     self.dfs(image, nr, nc, source, color)
        
#     def floodFill(self, image, sr, sc, color):
#         if image[sr][sc] == color:
#             return image

#         self.dfs(image, sr, sc, image[sr][sc], color)
#         return image