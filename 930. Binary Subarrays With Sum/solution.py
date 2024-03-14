import sys
sys.path.append("./Algorithm/LeetCode")
from test_leetcode import test
# https://leetcode.com/problems/binary-subarrays-with-sum
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return 4


if __name__ == "__main__":
    test(Solution().numSubarraysWithSum, [
        [[1,0,1,0,1], 2, 4],
        [[0,0,0,0,0], 0, 15]
    ])