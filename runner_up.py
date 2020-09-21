n = input('n')
n=int(n)
m=0
if 2<=n<=10:
    arr = map(int,input('v').split())
    ls=list(arr)
    ls.sort(reverse=True)
    #print(max(ls))
    for i in ls:
        if -100<=i<=100:
            if max(ls)>i:
                m=i
                break
        else:
            break
else:
    print('out of range')
print(m)
