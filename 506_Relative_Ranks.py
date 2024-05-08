# https://leetcode.com/problems/relative-ranks/description/

from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
            
        # Enumerate the scores with indices
        indexed_scores = list(enumerate(score))

        # Sort by score DESC
        indexed_scores.sort(key=lambda x: x[1], reverse=True)
        
        # Initialize the result array with the same size as the score
        result = [None] * len(score)
        
        # Assign ranks based on the sorted order
        for rank, (index, _) in enumerate(indexed_scores):
            if rank == 0:
                result[index] = "Gold Medal"
            elif rank == 1:
                result[index] = "Silver Medal"
            elif rank == 2:
                result[index] = "Bronze Medal"
            else:
                # rank + 1 because rank is zero-indexed
                result[index] = str(rank + 1)  

        return result