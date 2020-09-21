n=input( )
i=0
s=''
try:
    n=int(n)
except:
    print('Invalid input')
if 1<=n<=150:
    while i<n:
        s=s+str(i)
        i=i+1
print(s)
