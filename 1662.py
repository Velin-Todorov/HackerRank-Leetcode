def climbStairs(n: int, count = 0) -> int:
        
        if n == 0:
            return count
        
        if n > 2:
            count += 1
            climbStairs(n - 2, count)
        
        elif n >= 1:
            count += 1
            climbStairs(n - 1, count) 
        
        return count

climbStairs(2)
