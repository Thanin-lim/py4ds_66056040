"""
Exercise 13
"""


def calc_sum(num):
    if num.__len__()==0:
        return 0
    elif num.__len__()>1:
        sums=sum(num)
        return sums


    pass


def calc_prod(num):
    c=1
    for i in num:
        c=(c*i)
    return c

    pass

#%%
