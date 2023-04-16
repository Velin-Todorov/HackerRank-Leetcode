def rec(s: str) -> str:

    if len(s) == 1:
        return s
    
    return s[-1] + rec(s[:-1])


s = 'apa'
s2 = 'bear'

res2 = rec(s2)

print(res2)
