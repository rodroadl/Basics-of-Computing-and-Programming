def max_abs_val(lst):
    for i in range(len(lst)):
        lst[i] = abs(lst[i])
    return max(lst) 