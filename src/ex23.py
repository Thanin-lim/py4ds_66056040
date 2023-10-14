"""
Exercise 23 : 99 Bottles of Beer on the Wall
"""


def bottles_of_beer(param):
    result = ''
    if param != 1:
        result += str(param) + ' bottles of beer on the wall,\n'
        result += str(param) + ' bottles of beer.\n'
        result += 'Take one down, pass it around,\n'
        if (param - 1) == 1:
            result += '1 bottle of beer on the wall.\n'
        else:
            result += str(param - 1) + ' bottles of beer on the wall.\n'
    else:
        result += '1 bottle of beer on the wall,\n'
        result += '1 bottle of beer.\n'
        result += 'Take one down, pass it around,\n'
        result += 'No more bottles of beer on the wall!\n'
    return result
    # fix : complete this
    pass

def loop_bottles_of_bears(bottle):
    while bottle > 0:
        print(bottles_of_beer(bottle))
        bottle -= 1


if __name__ == '__main__':
    loop_bottles_of_bears(5)
