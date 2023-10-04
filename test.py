def mediens(m):
    if m.__len__()==0:
        return 0
    s=sorted(m)
    a=len(s)
    f=(a//2)
    # d=a%f
    l=s[f]
    if a%f==0:
        k=(a//2-1)
        ll=k+a%f
        ls=s[ll]
        summary=(l+ls)/2
        return summary
    else:
        return l
print(mediens([10,11,12,13,14,15,18,19,30,22,50,223])==16.5)
print(mediens([])== None)


import numpy as np
xaa=np.array([10,11,12,13,14,15,18,19,30,22,50,223])
xas=sorted(xaa)
print('m',np.median(xas))
print(xas)

def modes(number):
    if number.__len__()==0:
        return 0
    s={}
    for i in number:
        # print(i)
        if not i in s:
            s[i]=1
            # print(s[i])
        else:
            s[i]+=1
            # print(s[i])
            for i in s:
                if i==max(s.values()):
                    print(s)
# def mode(arr):
#     if arr==[]:
#         return None
#     else:
#         print(max(set(arr)))
#         print(set(arr))
#         return max(set(arr), key=arr.count)


# print(mode([2,3,3,4,5,6,7,8,9]))

print(modes([2,3,3,4,5,6,7,8,9,9,9,10]))
#%%
