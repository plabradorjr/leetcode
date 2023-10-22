class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ableToPlantCounter = 0
        prev = 0

        for hole in flowerbed:
            if hole == 1:
                if prev == 1: # can't plant on the previous!
                    ableToPlantCounter -= 1
                prev = 1
            if hole == 0:
                if prev == 1: # can't plant here
                    prev = 0
                else: 
                    ableToPlantCounter += 1
                    prev = 1 # the hole gets taken

        return ableToPlantCounter >= n

