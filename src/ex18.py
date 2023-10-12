"""
Exercise 18 : Buy 8 get 1 free
"""


def get_cost_of_coffee(unit, price):
    free = unit // 9
    paid = unit - free
    return paid * price
    pass

def get_cost_of_coffee_2(unit, price):
    free = unit // 9
    paid = unit - free
    return paid * price
    pass
