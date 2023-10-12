"""
Execise 10
"""


def find_and_replace(text, old_str, new_str):
    result = ''
    i = 0
    while i < len(text):
        if text[i:i + len(new_str)] == old_str:
            result += new_str
            i += len(old_str)
        else:
            result += text[i]
            i += 1
    return result
    # Fix : complete this
    pass
