count={}
list=list()
res={}
i=1
inp=input('Enter the file name: ')
fh=open(inp)
for line in fh:
    line=line.rstrip()
    line=line.split()
    list=list+line
    list.sort()
for word in list:
    count[word]=count.get(word,0)+1 #searching for the 'word' in 'list' if not then putting it in dictionary 'count' with value '0'
    #if found the word then incrementing the counter by 1
print(count)
for key in count:
    if count[key] > 1:
        print('found',key)
        res[i]=key
        i=i+1
print(res)
