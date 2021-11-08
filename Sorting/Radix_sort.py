def key_positions(seq, key):    
    k = key(max(seq, key=key)) + 1
    C = [0] * k
    for a in seq:
        C[key(a)] = C[key(a)] + 1
    sums = 0
    for i in range(k):
        C[i], sums = sums, sums + C[i]
    return C
def sorted_array(seq, key):
    """sorting an array using counting sort"""
    B = [0] * len(seq)
    P = key_positions(seq, key)
    for a in seq:
        B[P[key(a)]] = a
        P[key(a)] += 1
    return B

def radix_sort(numbers, d):
    """takes a sequence of natural numbers called numbers and uses counting sort 
    iteratively to sort the sequence up to the d-th digit from the right. 
    The argument d is a positive (and thus non-zero) integer."""
    B = numbers
    for index in range(d): 
        whole_digit_num = numbers[index]
        B = sorted_array(B, lambda whole_digit_num: whole_digit_num//(10**index) % 10)
        
    return B

# -------------test1------------
print(radix_sort([329, 457, 657, 839, 436, 720, 355], 3))
# --------------------------------------------------------
# -------------test2--------------------------
print(radix_sort([329, 457, 657, 839, 436, 720, 355], 1))
# ---------------------------------------------------------