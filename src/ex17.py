"""
Exercise 17
"""
import random


def roll_dice(n):
    f=0
    for i in range(n):
        f+=random.randint(1,6)
    return f
    pass

#%%
