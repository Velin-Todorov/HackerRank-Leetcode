class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        
        new_arr = [first]

        for i in range(len(encoded)):
            new_arr.append(encoded[i] ^ new_arr[i])

        
        return new_arr