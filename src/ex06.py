"""
Execise 6
"""


def ordinal_suffix(num):
    con=str(num)
    s=con[-2:]
    print(s)
    if s =='1':
        st=con+"st"
        return st
    elif s =='01':
        st=con+"st"
        return st
    elif s=='2':
        nd=con+'nd'
        return nd
    elif s=='3':
        rd=con+'rd'
        return rd
    else:
        th=con+'th'
        return th
    # FIX : complete this
    pass

#%%
