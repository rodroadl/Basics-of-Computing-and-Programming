def avg_val(lst):
    sum_elem = 0
    for elem in lst:
        sum_elem += elem
    avg = sum_elem / len(lst)
    return avg