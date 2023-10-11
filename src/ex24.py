"""
Exercise 24 : Every 15 minutes, ante meridiem (am) and post meridiem (pm)
ante : before
post : after
meridiem : midday
"""


def get_time_every_15_min():
    meridims=['am','pm']
    hours=['12','1','2','3','4','5','6','7','8','9','10','11']
    minit=['00','15','30','45']
    for a in meridims:
        for h in hours:
            for m in minit:
                print(h+":"+m+" "+a)

    # TODO : complete this
    pass
