def lcs(s1, s2, cache=None):
    if cache is None:
        cache = [[None] * (len(s2) + 1) for _ in range(len(s1)+1)]
    if cache[len(s1)][len(s2)] != None:
        return cache[len(s1)][len(s2)] 
    if s1 == '' or s2 == '':
        return ''
    elif s1[-1] == s2[-1]: # Last chars match
        cache[len(s1)][len(s2)] = lcs(s1[:-1], s2[:-1], cache) + s1[-1]
        
        return cache[len(s1)][len(s2)]
    else:
       # Drop last char of each string in turn.
       # Choose best outcome. 
        soln1 = lcs(s1[:-1], s2, cache)
        soln2 = lcs(s1, s2[:-1], cache)
        value = max([soln1, soln2], key=len)
        cache[len(s1)][len(s2)] = value
        return value
# --------test1----------------------------
# A simple test that should run without caching
s1 = "abcde"
s2 = "qbxxd"
lcs_string = lcs(s1, s2)
print(lcs_string)
# -------------------------------------------------