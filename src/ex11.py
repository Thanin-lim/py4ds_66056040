"""
Exercise 11
"""


def get_hr_min_sec(time):
    sec=time%60
    mi=(time//60)%60
    hours=time//3600
    t=' '
    if time ==0:
        return '0s'
    if sec>0:
        t=str(sec)+"s"
    if mi>0:
        t=str(mi)+"m "+t
    if hours>0:
        t=str(hours)+'h '+t
    return t.strip()


#%%
