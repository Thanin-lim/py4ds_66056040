"""
Exercise 22 : Rock Paper Scissor
"""


def rps_check(name, name1):
    if name =='rock' and name1=='paper':
        return 'player two'
    elif name =='rock' and name1=='scissors':
        return 'player one'
    elif name =='paper' and name1=='scissors':
        return 'player two'
    elif name =='paper' and name1=='rock':
        return  'player one'
    elif name =='scissors' and name1=='rock':
        return 'player two'
    elif name =='scissors' and name1=='paper':
        return 'player one'
    else:
        return 'tie'

    # Fix : complete this
    pass
