count={}
list=list()
res={}
i=1
inp=input('Enter the file name: ')
fh=open(inp) #fh here is file handlder opening the file with name as inp
for line in fh: #travering with variable 'line' in the file with handler fh
    line=line.split()
    list=list+line
    list.sort()
for word in list: #counting the occurance of words in the file
    if word not in count:
        count[word]=1
    else:
        count[word]=count[word]+1
print(count) #a dictionary is then created with record of words and count of occurance of those words
for key in count:
    if count[key] > 1: #searching for the words that occurered more than once in the file
        print('found',key)
        res[i]=key #saving this multiple occured words and it's count in another dictionary 'res'
        i=i+1
print(res)
