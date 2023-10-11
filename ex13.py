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

def medians(m):
    if m.__len__()==0:
        return 0
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
def modes(number):
    if number.__len__()==0:
        return 0
    s={}
    for i in number:
        if not i in s:
            s[i]=1
        else:
            s[i]+=1
            ds=max(s.values())
    value = {i for i in s if s[i]==int(ds)}
    return value


if __name__=='__main__':
    print(cal([])==0)
    print(cal([2,4,6,8,10])==30)
    print(cal([1,2])==3)
    print(calpro([2,3])==6)
    print(averages([2,2,2])==2)
    print(averages([1,2,3])==4)
    print(averages([0,0,0])==0)
    print(medians([])==None)
    print(medians([1,2,3])==2)
    print(medians([3,7,10,4,1,9,6,5,2,8])==5.5)
    print(medians([3,7,10,4,1,9,6,2,8])==6)
    print(modes([1,2,2,3,3,200,200,200,200,1,2])==3)
    print(modes([1, 2, 3, 4, 4]))
#%%
#%%
