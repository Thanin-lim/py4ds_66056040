def cal(list_data):
    if list_data.__len__()==0:
        return 0
    else:
        total=0
        for i in list_data:
            total=total+i
        return total



def calpro(list_pro):
    if list_pro.__len__()==0:
        return 0
    else:
        totalpro=1
        for i in list_pro:
            totalpro=totalpro*i
        return totalpro

def averages(list_avg):
    if list_avg.__len__()==0:
        return 0
    else:
        avge=len(list_avg)
        totals=0
        for i in list_avg:
            totals=totals+i
        totals=totals/avge
        return totals

def mediens(m):
    if m.__len__()==0:
        return 0
    else:
        s=sorted(m)
        a=len(m)//m
        print(a)

if __name__=='__main__':
    print(cal([])==0)
    print(cal([2,4,6,8,10])==30)
    print(cal([1,2])==3)
    print(calpro([2,3])==6)
    print(averages([2,2,2])==2)
    print(averages([1,2,3])==4)
    print(averages([0,0,0])==0)
    print(mediens([20,3,10]))
#%%
#%%
