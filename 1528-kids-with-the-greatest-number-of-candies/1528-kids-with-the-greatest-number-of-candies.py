class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        highest = max(candies)
        resultList = []
        for i in candies:
            if i + extraCandies >= highest:
                resultList.append(True)
            else:
                resultList.append(False)
        return resultList
