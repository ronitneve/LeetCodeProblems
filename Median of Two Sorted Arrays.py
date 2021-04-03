from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newList = [*nums1, *nums2]
        newList.sort()
        length = len(newList)
        if (length %2 == 0) : 
            return (newList[int(length/2) - 1] + newList[int(length/2)]) / 2
        else:
            return newList[int(length/2)]



if __name__ == "__main__":
    l1 = [1, 2]
    l2 = [4, 5, 3]
    driver = Solution()
    print(driver.findMedianSortedArrays(l1,l2))