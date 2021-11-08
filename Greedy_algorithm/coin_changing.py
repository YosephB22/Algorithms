from collections import defaultdict
def change_greedy(amount, coinage):
    """
    takes an integer amount of money in some units (call them "cents" if you like) 
    plus a list of integer coin values (in an arbitrary order) and returns the breakdown 
    of that amount into coins as obtained by the greedy algorithm described in the lecture notes
    """
    counts = defaultdict(int)
    C = sorted(coinage)
    alist = []
    index = len(coinage) - 1
    imax = C[index]
    while amount > 0:
        while imax > amount:
            index -= 1
            if index < 0:
                return None
            imax = C[index]  
        counts[imax] += 1
        amount -= imax
    for value in counts:
        alist.append((counts[value], value))
    return alist

# ----------------test1-----------------------
print(change_greedy(82, [1, 10, 25, 5]))
# ---------------------------------------------
# ------------test2----------------------------
print(change_greedy(80, [1, 10, 25]))
# ---------------------------------------------