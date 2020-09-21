fname=input('Enter the file name: ')
fh=open(fname)
count={}
for line in fh:
    wlist=line.split()
    for words in wlist:
        count[words]=count.get(words,0)+1
print(count)
bigCount=None
bigWord=None
for word,times in count.items():
    if bigWord is None or times>bigCount:
        bigWord=word
        bigCount=times
print(bigWord,bigCount)
