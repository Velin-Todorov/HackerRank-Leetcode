#!/usr/bin/python3

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:

        dct = {}

        for i in range(len(score)):
            current_grade = score[i][k]

            if current_grade not in dct:
                dct[current_grade] = score[i]
        
        srted = list(sorted(dct.values(), key=lambda x: -x[k]))

        return srted


