x = input('x')
x=int(x)
y = input('y')
y=int(y)
z = input('z')
z=int(z)
n = input('n')
n=int(n)
list1= [i for i in range(x+1)]
list2 =[i for i in range(y+1)]
list3 =[i for i in range(z+1)]
Flist=[]
Tlist=[[i,j,k] for i in list1 for j in list2 for k in list3]
#print(Tlist)
for val in Tlist:
    if sum(val)==n:
        continue
    else:
        Flist.append(val)
print(Flist)
