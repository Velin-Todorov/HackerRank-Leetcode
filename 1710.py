from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sorted_arr = sorted(boxTypes, key=lambda x: -x[1])

        total = 0

        for i in sorted_arr:
            num_boxes = i[0]
            num_units = i[1]

            if truckSize == 0:
                return total

            if num_boxes <= truckSize:
                truckSize -= num_boxes
                total += (num_boxes * num_units)

            elif truckSize < num_boxes and truckSize != 0:
                total += (truckSize * num_units)
                truckSize -= truckSize

        return total