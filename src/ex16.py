"""
Exercise 16
"""



def mode(num):
    n_len = len(num)
    if n_len == 0:
        return None
    max_count = 0
    element_having_max_freq = 0
    for i in range(0, n_len):
        count = 0
        for j in range(0, n_len):
            if num[i] == num[j]:
                count += 1
        if count > max_count:
            max_count = count
            element_having_max_freq = num[i]

    return element_having_max_freq

#%%
