def lcs(s1, s2):
    """constructing lcs"""
    table = [[0] * (len(s2) + 1) for _ in range(len(s1)+1)]
    for i, v in enumerate(s1, start=1):
        for j, value in enumerate(s2, start=1):
            if v == value:
                table[i][j] = 1 + table[i - 1][j - 1] #diagonal
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    i = len(table) - 1
    j = len(table[0]) - 1
    result = ""
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            result += s1[i - 1]
            j -= 1
            i -= 1
        else:
            if table[i - 1][j] > table[i][j - 1]:
                i -= 1
            else:
                j -= 1

    return (result)[::-1]
# ------------test1------------------------------------
s1 = "Look at me, I can fly!"
s2 = "Look at that, it's a fly"
print(lcs(s1, s2))
# ------------------------------------------------------