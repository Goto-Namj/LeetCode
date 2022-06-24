class Solution:
    def append_sort(self, list_, item):
        for i in range(len(list_)):
            if item < list_[i]:
                continue
            else:
                list_.insert(i, item)
                return list_
        list_.append(item)
        return list_
        
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        index_ = 0
        used_heights = []
        for i in range(1, len(heights)):
            index_ = i
            if heights[i-1] >= heights[i]:
                continue
            else:
                if ladders > 0:
                    ladders -= 1
                    used_heights = self.append_sort(used_heights, heights[i] - heights[i-1])
                else:
                    used_heights = self.append_sort(used_heights, heights[i] - heights[i-1])
                    height = used_heights.pop()
                    bricks -= height
                    if bricks < 0:
                        index_ -= 1
                        break
        return index_


s = Solution()
result = s.furthestBuilding(heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1)
print(result)