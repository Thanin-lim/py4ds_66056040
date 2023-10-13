"""
Execise 8
"""


def write_to_file(filename, message):
    f = open(filename, 'w')
    f.write(message)
    # fix : complete this
    pass


def read_from_file(filename):

    f = open(filename, 'r')
    return f.read()
    # fix : complete this
    pass


def append_to_file(filename, message):
    f = open(filename, 'a')
    f.write(message)
    # fix : complete this
    pass

