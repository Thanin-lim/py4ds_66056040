"""
Exercise 15
"""


def median(m):
    if m.__len__()==0:
        return None
    s=sorted(m)
    a=len(s)
    f=(a//2)
    # d=a%f
    l=s[f]
    if a%2==0:
        k=(a//2-1)
        ll=k+a%f
        ls=s[ll]
        summary=(l+ls)/2
        return summary
    else:
        return l
    pass
